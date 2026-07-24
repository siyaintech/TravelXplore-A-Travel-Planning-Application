from flask import Flask, render_template, request, redirect, session, flash, jsonify
from itinerary import generate_itinerary
from itinerary import city_data
from budget import generate_pie_chart
from database import init_db, add_user, get_user, save_history, save_trip, get_user_trips, delete_trip, get_min_budget
import random
import time  # For cache-busting timestamp

app = Flask(__name__)
app.secret_key = "secret123"

# Initialize database on startup
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    username = session.get("user")
    if not username:
        return redirect("/login")  # Redirect if not logged in
    
    trips = get_user_trips(username)  # Get user's trips as list of tuples
    # Process trips to ensure budget is an integer for template formatting
    processed_trips = []
    for trip in trips:
        try:
            trip_id = int(trip[0]) if trip[0] and str(trip[0]).isdigit() else 0  # Fallback to 0 if invalid
            budget = int(trip[5]) if trip[5] and str(trip[5]).isdigit() else 0
        except (ValueError, TypeError):
            trip_id = 0
            budget = 0  # Fallback if conversion fails
        # Always add the trip
        processed_trips.append({
            'id': trip_id,
            'city': trip[1] or 'Unknown',
            'start_date': trip[2] or 'N/A',
            'end_date': trip[3] or 'N/A',
            'days': trip[4] or 0,
            'budget': budget,
            'style': trip[6] if len(trip) > 6 else 'Unknown'
        })
    return render_template("dashboard.html", username=username, trips=processed_trips)

@app.route("/get_min_budget/<city>")
def get_min_budget_route(city):
    """Returns the minimum budget for a city as JSON."""
    min_budget = get_min_budget(city)
    if min_budget is not None:
        return jsonify({'min_budget': min_budget})
    else:
        return jsonify({'error': 'City not found'}), 404

@app.route("/signup", methods=["GET", "POST"])
def signup():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        success = add_user(username, password)
        if success:
            return redirect("/login")
        else:
            error = "Username already taken. Please choose another."
    return render_template("signup.html", error=error)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = get_user(username)
        if user and user[2] == password:
            session["user"] = username
            return redirect("/dashboard")  # Redirect to dashboard after login
        else:
            error = "Invalid username or password."
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")  # Redirect to first page after logout

# WHEN USER CLICKS "START PLANNING" or submits dashboard form
@app.route('/plan', methods=['GET','POST'])
def plan():
    if request.method == 'POST':
        city       = request.form.get('city')
        start_date = request.form.get('start_date')
        end_date   = request.form.get('end_date')
        budget     = int(request.form.get('budget', 0))  # Allow 0 if not set
        style      = request.form.get('style', 'standard')

        from datetime import datetime
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end   = datetime.strptime(end_date,   "%Y-%m-%d")
        days  = (end - start).days + 1

        breakdown = generate_pie_chart(city, budget, style, save_folder="static")

        # Save the trip for the logged-in user
        username = session.get("user")
        if username:
            save_trip(username, city, start_date, end_date, days, budget, style)

        return render_template(
            'result.html',
            city=city,
            start_date=start_date,
            end_date=end_date,
            days=days,
            budget=budget,
            style=style,
            breakdown=breakdown
        )

    return redirect('/')

# GENERATE ITINERARY BUTTON
@app.route("/generate", methods=["POST"])
def generate():
    city = request.form.get("city")
    days_str = request.form.get("days")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")
    budget_str = request.form.get("budget")
    style = request.form.get("style")

    # Basic validation
    if not city or not days_str or not start_date or not end_date:
        return "Error: Missing required data. Please go back and try again."
    
    try:
        days = int(days_str)  # Use requested days directly
        budget = int(budget_str) if budget_str else 0
    except ValueError:
        return "Error: Invalid days or budget value."

    # Regenerate breakdown for the template
    breakdown = generate_pie_chart(city, budget, style, save_folder="static")

    data = city_data.get(city.lower())
    if not data:
        return "City not found"

    attractions = data.get("attractions", [])
    restaurants = data.get("restaurants", [])
    activities = data.get("activities", [])

    # Fallbacks if no data
    if not attractions:
        attractions = [{"name": "Explore the city freely"}]
    if not restaurants:
        restaurants = [{"name": "Dine at a local spot"}]
    if not activities:
        activities = [{"name": "Enjoy free time"}]

    # Shuffle each list once
    random.shuffle(attractions)
    random.shuffle(restaurants)
    random.shuffle(activities)

    # Generate itinerary, allowing repeats by cycling through lists
    itinerary = []
    for day in range(1, days + 1):  # Use full requested days
        attr_name = attractions[(day - 1) % len(attractions)]["name"]
        rest_name = restaurants[(day - 1) % len(restaurants)]["name"]
        act_name = activities[(day - 1) % len(activities)]["name"]
        
        day_plan = {
            "day": day,
            "visit": attr_name,
            "eat": rest_name,
            "do": act_name
        }
        itinerary.append(day_plan)

    return render_template(
        'itinerary.html',
        city=city,
        start_date=start_date,
        end_date=end_date,
        days=days,
        budget=budget,
        style=style,
        breakdown=breakdown,
        itinerary=itinerary
    )

# New route to delete a trip
@app.route("/delete-trip/<trip_id>", methods=["POST"])
def delete_trip_route(trip_id):
    try:
        trip_id = int(trip_id)  # Convert to int safely
    except ValueError:
        flash("Invalid trip ID. Please try again.", "error")
        return redirect(f"/dashboard?t={int(time.time())}")  # Invalid ID, redirect to dashboard
    
    username = session.get("user")
    if not username:
        return redirect("/login")
    
    # Delete the trip (ensure it belongs to the user)
    delete_trip(trip_id, username)
    flash("Trip deleted successfully!", "success")
    # Add cache-busting timestamp to force fresh load
    return redirect(f"/dashboard?t={int(time.time())}")

@app.route("/explore/<city>/attractions")
def view_attractions(city):
    data = city_data.get(city.lower())
    if not data:
        return "City not found"
    if session.get("user"):
        save_history(session["user"], city)
    return render_template("attractions.html",
                           city=city.title(),
                           attractions=data["attractions"])

@app.route("/explore/<city>/restaurants")
def view_restaurants(city):
    data = city_data.get(city.lower())
    if not data:
        return "City not found"
    if session.get("user"):
        save_history(session["user"], city)
    return render_template("restaurants.html",
                           city=city.title(),
                           restaurants=data["restaurants"])

@app.route("/explore/<city>/activities")
def view_activities(city):
    data = city_data.get(city.lower())
    if not data:
        return "City not found"
    if session.get("user"):
        save_history(session["user"], city)
    return render_template("activities.html",
                           city=city.title(),
                           activities=data["activities"])

if __name__ == "__main__":
    app.run(debug=True)