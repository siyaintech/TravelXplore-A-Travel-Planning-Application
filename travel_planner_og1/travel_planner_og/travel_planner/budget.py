import matplotlib
matplotlib.use('Agg')  # Non-interactive backend (required for Flask)
import matplotlib.pyplot as plt
import os

# How to split the total budget across categories (must add to 1.0)
# Different splits based on travel style
SPLIT_RATIOS = {
    "budget":   {"attractions": 0.20, "restaurants": 0.35, "activities": 0.25, "transport": 0.20},
    "standard": {"attractions": 0.25, "restaurants": 0.30, "activities": 0.30, "transport": 0.15},
    "luxury":   {"attractions": 0.25, "restaurants": 0.35, "activities": 0.30, "transport": 0.10},
}

COLORS = ["#f4a261", "#e76f51", "#2a9d8f", "#457b9d"]


def calculate_budget(total_budget, style="standard"):
    """
    Splits the user's entered total budget into categories
    based on travel style ratios.
    Returns a dict with per-category amounts + total.
    """
    ratios = SPLIT_RATIOS.get(style, SPLIT_RATIOS["standard"])

    breakdown = {
        category: round(total_budget * ratio)
        for category, ratio in ratios.items()
    }
    breakdown["total"] = total_budget  # always show what user entered
    return breakdown


def generate_pie_chart(city, total_budget, style="standard", save_folder="static"):
    """
    Generates a matplotlib donut chart using the user's actual budget,
    saves it to static/budget_chart.png, and returns the breakdown dict.
    """
    breakdown = calculate_budget(total_budget, style)

    labels = ["Attractions", "Restaurants", "Activities", "Transport"]
    sizes  = [
        breakdown["attractions"],
        breakdown["restaurants"],
        breakdown["activities"],
        breakdown["transport"],
    ]

    fig, ax = plt.subplots(figsize=(5, 5), facecolor="white")

    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        colors=COLORS,
        autopct="%1.1f%%",
        startangle=140,
        pctdistance=0.75,
        wedgeprops=dict(width=0.55, edgecolor="white", linewidth=2)
    )

    for text in texts:
        text.set_fontsize(11)
        text.set_fontweight("bold")
        text.set_color("#333333")

    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_color("white")
        autotext.set_fontweight("bold")

    # Center label: show total budget
    ax.text(0, 0.10, "Budget", ha="center", va="center",
            fontsize=11, color="#777", fontweight="normal")
    ax.text(0, -0.15, f"₹{total_budget:,}", ha="center", va="center",
            fontsize=14, color="#111", fontweight="bold")

    ax.set_title(
        f"{city.title()} · {style.title()} Travel",
        fontsize=13, fontweight="bold", pad=16, color="#222"
    )

    plt.tight_layout()

    os.makedirs(save_folder, exist_ok=True)
    chart_path = os.path.join(save_folder, "budget_chart.png")
    plt.savefig(chart_path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close()

    return breakdown