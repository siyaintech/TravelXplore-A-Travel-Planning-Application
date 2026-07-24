import random

city_data = {

    "goa": {
        "attractions": [
            {"name": "Baga Beach", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Baga_beach_Goa_india.jpg/640px-Baga_beach_Goa_india.jpg"},
            {"name": "Fort Aguada", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Fort_Aguada_Goa.jpg/640px-Fort_Aguada_Goa.jpg"},
            {"name": "Anjuna Beach", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Anjuna_beach_Goa.jpg/640px-Anjuna_beach_Goa.jpg"},
            {"name": "Basilica of Bom Jesus", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/fifty/Basilica_of_Bom_Jesus.jpg/640px-Basilica_of_Bom_Jesus.jpg"},
            {"name": "Dudhsagar Falls", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Dudhsagar_Falls_Goa.jpg/640px-Dudhsagar_Falls_Goa.jpg"},
            {"name": "Calangute Beach", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Calangute_beach.jpg/640px-Calangute_beach.jpg"},
        ],
        "restaurants": [
            {"name": "Thalassa", "img": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600"},
            {"name": "Pousada by the Beach", "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600"},
            {"name": "Gunpowder", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600"},
            {"name": "Fisherman's Wharf", "img": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=600"},
            {"name": "Britto's", "img": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=600"},
        ],
        "activities": [
            {"name": "Scuba Diving", "img": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600"},
            {"name": "Parasailing", "img": "https://images.unsplash.com/photo-1530870110042-98b2cb110834?w=600"},
            {"name": "Dolphin Watching", "img": "https://images.unsplash.com/photo-1607153333879-c174d265f1d2?w=600"},
            {"name": "Spice Plantation Tour", "img": "https://images.unsplash.com/photo-1599598425947-5202edd56bdb?w=600"},
            {"name": "Casino Night Cruise", "img": "https://images.unsplash.com/photo-1548438294-1ad5d5f4f063?w=600"},
        ]
    },

    "delhi": {
        "attractions": [
            {"name": "India Gate", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/India_gate.jpg/640px-India_gate.jpg"},
            {"name": "Red Fort", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Red_Fort_in_Delhi_03-2016.jpg/640px-Red_Fort_in_Delhi_03-2016.jpg"},
            {"name": "Qutub Minar", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Qutb_Minar_mausoleum.jpg/640px-Qutb_Minar_mausoleum.jpg"},
            {"name": "Humayun's Tomb", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Humayun%27s_Tomb_by_Martand.jpg/640px-Humayun%27s_Tomb_by_Martand.jpg"},
            {"name": "Lotus Temple", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Lotus_temple_Evening.jpg/640px-Lotus_temple_Evening.jpg"},
            {"name": "Akshardham Temple", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/forty/Akshardham_Delhi.jpg/640px-Akshardham_Delhi.jpg"},
        ],
        "restaurants": [
            {"name": "Karim's", "img": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600"},
            {"name": "Indian Accent", "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600"},
            {"name": "Bukhara", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600"},
            {"name": "Paranthe Wali Gali", "img": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=600"},
            {"name": "Saravana Bhavan", "img": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=600"},
        ],
        "activities": [
            {"name": "Chandni Chowk Walk", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Chandni_Chowk_Delhi.jpg/640px-Chandni_Chowk_Delhi.jpg"},
            {"name": "Heritage Tour", "img": "https://images.unsplash.com/photo-1548013146-72479768bada?w=600"},
            {"name": "Rickshaw Ride", "img": "https://images.unsplash.com/photo-1567157577867-05ccb1388e66?w=600"},
            {"name": "Street Food Tour", "img": "https://images.unsplash.com/photo-1599598425947-5202edd56bdb?w=600"},
            {"name": "Museum Visit", "img": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600"},
        ]
    },

    "mumbai": {
        "attractions": [
            {"name": "Gateway of India", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Mumbai_03-2016_30_Gateway_of_India.jpg/640px-Mumbai_03-2016_30_Gateway_of_India.jpg"},
            {"name": "Marine Drive", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Marine_Drive%2C_Mumbai.jpg/640px-Marine_Drive%2C_Mumbai.jpg"},
            {"name": "Juhu Beach", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Juhu_beach_mumbai.jpg/640px-Juhu_beach_mumbai.jpg"},
            {"name": "Elephanta Caves", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Elephanta_Caves.jpg/640px-Elephanta_Caves.jpg"},
            {"name": "Haji Ali Dargah", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Haji_Ali_Dargah.jpg/640px-Haji_Ali_Dargah.jpg"},
            {"name": "Chhatrapati Shivaji Terminus", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Mumbai_CST.jpg/640px-Mumbai_CST.jpg"},
        ],
        "restaurants": [
            {"name": "Leopold Cafe", "img": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600"},
            {"name": "Bastian", "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600"},
            {"name": "Trishna", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600"},
            {"name": "Cafe Mondegar", "img": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=600"},
            {"name": "Khyber", "img": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=600"},
        ],
        "activities": [
            {"name": "Bollywood Studio Tour", "img": "https://images.unsplash.com/photo-1530870110042-98b2cb110834?w=600"},
            {"name": "Yacht Ride", "img": "https://images.unsplash.com/photo-1548438294-1ad5d5f4f063?w=600"},
            {"name": "Dharavi Tour", "img": "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=600"},
            {"name": "Cricket Match", "img": "https://images.unsplash.com/photo-1599598425947-5202edd56bdb?w=600"},
            {"name": "Koli Fishing Village Tour", "img": "https://images.unsplash.com/photo-1607153333879-c174d265f1d2?w=600"},
        ]
    },

    "jaipur": {
        "attractions": [
            {"name": "Hawa Mahal", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Hawa_Mahal_Jaipur_Rajasthan.jpg/640px-Hawa_Mahal_Jaipur_Rajasthan.jpg"},
            {"name": "Amber Fort", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Amer_Fort%2C_Jaipur%2C_Rajasthan.jpg/640px-Amer_Fort%2C_Jaipur%2C_Rajasthan.jpg"},
            {"name": "City Palace", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/City_Palace%2C_Jaipur_01.jpg/640px-City_Palace%2C_Jaipur_01.jpg"},
            {"name": "Jantar Mantar", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jantar_Mantar%2C_Jaipur.jpg/640px-Jantar_Mantar%2C_Jaipur.jpg"},
            {"name": "Nahargarh Fort", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Nahargarh_Fort_Jaipur.jpg/640px-Nahargarh_Fort_Jaipur.jpg"},
            {"name": "Jal Mahal", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Jal_Mahal_at_night.jpg/640px-Jal_Mahal_at_night.jpg"},
        ],
        "restaurants": [
            {"name": "Chokhi Dhani", "img": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600"},
            {"name": "Spice Court", "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600"},
            {"name": "LMB Restaurant", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600"},
            {"name": "1135 AD", "img": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=600"},
            {"name": "Rawat Kachori", "img": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=600"},
        ],
        "activities": [
            {"name": "Elephant Ride", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Elephant_Ride_Amber_Fort_Jaipur.jpg/640px-Elephant_Ride_Amber_Fort_Jaipur.jpg"},
            {"name": "Block Printing Workshop", "img": "https://images.unsplash.com/photo-1599598425947-5202edd56bdb?w=600"},
            {"name": "Hot Air Balloon", "img": "https://images.unsplash.com/photo-1530870110042-98b2cb110834?w=600"},
            {"name": "Gem Polishing Tour", "img": "https://images.unsplash.com/photo-1607153333879-c174d265f1d2?w=600"},
            {"name": "Bazaar Shopping", "img": "https://images.unsplash.com/photo-1548438294-1ad5d5f4f063?w=600"},
        ]
    },

    "ahmedabad": {
        "attractions": [
            {"name": "Sabarmati Ashram", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Sabarmati_Ashram_Ahmedabad.jpg/640px-Sabarmati_Ashram_Ahmedabad.jpg"},
            {"name": "Kankaria Lake", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Kankaria_Lake_Ahmedabad.jpg/640px-Kankaria_Lake_Ahmedabad.jpg"},
            {"name": "Adalaj Stepwell", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Adalaj_stepwell.jpg/640px-Adalaj_stepwell.jpg"},
            {"name": "Sidi Saiyyed Mosque", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Sidi_Saiyyed_Mosque.jpg/640px-Sidi_Saiyyed_Mosque.jpg"},
            {"name": "Akshardham Temple", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Akshardham_Gandhinagar.jpg/640px-Akshardham_Gandhinagar.jpg"},
        ],
        "restaurants": [
            {"name": "Agashiye", "img": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600"},
            {"name": "Gordhan Thal", "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600"},
            {"name": "Patang", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600"},
            {"name": "Green House", "img": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=600"},
        ],
        "activities": [
            {"name": "Riverfront Cycling", "img": "https://images.unsplash.com/photo-1530870110042-98b2cb110834?w=600"},
            {"name": "Heritage Walk", "img": "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=600"},
            {"name": "Kite Museum Visit", "img": "https://images.unsplash.com/photo-1599598425947-5202edd56bdb?w=600"},
            {"name": "Auto World Vintage Car Museum", "img": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600"},
        ]
    },

    "paris": {
        "attractions": [
            {"name": "Eiffel Tower", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Tour_Eiffel_Wikimedia_Commons.jpg/640px-Tour_Eiffel_Wikimedia_Commons.jpg"},
            {"name": "Louvre Museum", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Louvre_Museum_Wikimedia_Commons.jpg/640px-Louvre_Museum_Wikimedia_Commons.jpg"},
            {"name": "Montmartre", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Sacre_Coeur_1.jpg/640px-Sacre_Coeur_1.jpg"},
            {"name": "Notre Dame Cathedral", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Cath%C3%A9drale_Notre-Dame_de_Paris%2C_20_March_2014.jpg/640px-Cath%C3%A9drale_Notre-Dame_de_Paris%2C_20_March_2014.jpg"},
            {"name": "Palace of Versailles", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Versailles_-_Chateau_-_Parterre_du_Midi_%28view%29.jpg/640px-Versailles_-_Chateau_-_Parterre_du_Midi_%28view%29.jpg"},
            {"name": "Champs-Élysées", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Champs-Elysees.jpg/640px-Champs-Elysees.jpg"},
        ],
        "restaurants": [
            {"name": "Le Jules Verne", "img": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600"},
            {"name": "Cafe de Flore", "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600"},
            {"name": "Le Grand Colbert", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600"},
            {"name": "Ladurée", "img": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=600"},
            {"name": "Septime", "img": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=600"},
        ],
        "activities": [
            {"name": "Seine Cruise", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/forty/Seine_river_cruise_Paris.jpg/640px-Seine_river_cruise_Paris.jpg"},
            {"name": "Wine Tasting Tour", "img": "https://images.unsplash.com/photo-1530870110042-98b2cb110834?w=600"},
            {"name": "Cooking Class", "img": "https://images.unsplash.com/photo-1599598425947-5202edd56bdb?w=600"},
            {"name": "Moulin Rouge Show", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Moulin_Rouge_-_2011_%28crop%29.jpg/640px-Moulin_Rouge_-_2011_%28crop%29.jpg"},
            {"name": "Bike Tour", "img": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600"},
        ]
    },

    "dubai": {
        "attractions": [
            {"name": "Burj Khalifa", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/9/93/Burj_Khalifa.jpg/640px-Burj_Khalifa.jpg"},
            {"name": "Palm Jumeirah", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Palm_Jumeirah_from_the_air.jpg/640px-Palm_Jumeirah_from_the_air.jpg"},
            {"name": "Dubai Marina", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Dubai_Marina_Skyline.jpg/640px-Dubai_Marina_Skyline.jpg"},
            {"name": "Dubai Mall", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Dubai_mall.jpg/640px-Dubai_mall.jpg"},
            {"name": "Gold Souk", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Gold_Souk_Dubai.jpg/640px-Gold_Souk_Dubai.jpg"},
            {"name": "Museum of the Future", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Museum_of_the_Future%2C_Dubai.jpg/640px-Museum_of_the_Future%2C_Dubai.jpg"},
        ],
        "restaurants": [
            {"name": "Pierchic", "img": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600"},
            {"name": "Atmosphere", "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600"},
            {"name": "Nobu Dubai", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600"},
            {"name": "Al Hadheerah", "img": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=600"},
            {"name": "Zuma", "img": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=600"},
        ],
        "activities": [
            {"name": "Desert Safari", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Desert_Safari_Dubai.jpg/640px-Desert_Safari_Dubai.jpg"},
            {"name": "Skydiving", "img": "https://images.unsplash.com/photo-1530870110042-98b2cb110834?w=600"},
            {"name": "Ski Dubai", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/forty/Ski_Dubai.jpg/640px-Ski_Dubai.jpg"},
            {"name": "Dhow Cruise", "img": "https://images.unsplash.com/photo-1607153333879-c174d265f1d2?w=600"},
            {"name": "Helicopter Tour", "img": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600"},
        ]
    },

    "london": {
        "attractions": [
            {"name": "Big Ben", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Elizabeth_Tower%2C_2022.jpg/640px-Elizabeth_Tower%2C_2022.jpg"},
            {"name": "Tower Bridge", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Tower_Bridge_from_Shad_Thames.jpg/640px-Tower_Bridge_from_Shad_Thames.jpg"},
            {"name": "London Eye", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/London_Eye_2.jpg/640px-London_Eye_2.jpg"},
            {"name": "Buckingham Palace", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Buckingham_Palace%2C_London_-_April_2009.jpg/640px-Buckingham_Palace%2C_London_-_April_2009.jpg"},
            {"name": "British Museum", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/British_Museum_from_NE_2.JPG/640px-British_Museum_from_NE_2.JPG"},
            {"name": "Hyde Park", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/sixty/Hyde_Park_London.jpg/640px-Hyde_Park_London.jpg"},
        ],
        "restaurants": [
            {"name": "Dishoom", "img": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600"},
            {"name": "Sketch", "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600"},
            {"name": "Ottolenghi", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600"},
            {"name": "Gordon Ramsay", "img": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=600"},
            {"name": "The Ledbury", "img": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=600"},
        ],
        "activities": [
            {"name": "Thames Cruise", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Thames_Cruise_London.jpg/640px-Thames_Cruise_London.jpg"},
            {"name": "Harry Potter Studio Tour", "img": "https://images.unsplash.com/photo-1530870110042-98b2cb110834?w=600"},
            {"name": "West End Show", "img": "https://images.unsplash.com/photo-1607153333879-c174d265f1d2?w=600"},
            {"name": "Changing of the Guard", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Changing_of_the_Guard_at_Buckingham_Palace.jpg/640px-Changing_of_the_Guard_at_Buckingham_Palace.jpg"},
            {"name": "Jack the Ripper Tour", "img": "https://images.unsplash.com/photo-1599598425947-5202edd56bdb?w=600"},
        ]
    },

    "newyork": {
        "attractions": [
            {"name": "Statue of Liberty", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Statue_of_Liberty_7.jpg/640px-Statue_of_Liberty_7.jpg"},
            {"name": "Central Park", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Central_Park_-_Photo_by_Ggia.jpg/640px-Central_Park_-_Photo_by_Ggia.jpg"},
            {"name": "Times Square", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/New_york_times_square-terabass.jpg/640px-New_york_times_square-terabass.jpg"},
            {"name": "Empire State Building", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Empire_State_Building_%28aerial_view%29.jpg/640px-Empire_State_Building_%28aerial_view%29.jpg"},
            {"name": "Brooklyn Bridge", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Brooklyn_Bridge_Postdlf.jpg/640px-Brooklyn_Bridge_Postdlf.jpg"},
            {"name": "The High Line", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/High_Line_-_Section_2_Opening.jpg/640px-High_Line_-_Section_2_Opening.jpg"},
        ],
        "restaurants": [
            {"name": "Katz's Deli", "img": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600"},
            {"name": "The River Cafe", "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600"},
            {"name": "Le Bernardin", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600"},
            {"name": "Peter Luger Steak House", "img": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=600"},
            {"name": "Grimaldi's Pizza", "img": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=600"},
        ],
        "activities": [
            {"name": "Broadway Show", "img": "https://images.unsplash.com/photo-1607153333879-c174d265f1d2?w=600"},
            {"name": "Helicopter Ride", "img": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600"},
            {"name": "Brooklyn Food Tour", "img": "https://images.unsplash.com/photo-1599598425947-5202edd56bdb?w=600"},
            {"name": "MoMA Museum", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/MoMA_NYC.jpg/640px-MoMA_NYC.jpg"},
            {"name": "Cycling in Central Park", "img": "https://images.unsplash.com/photo-1548438294-1ad5d5f4f063?w=600"},
        ]
    },

    "singapore": {
        "attractions": [
            {"name": "Marina Bay Sands", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Marina_Bay_Sands_in_the_evening_-_20101120.jpg/640px-Marina_Bay_Sands_in_the_evening_-_20101120.jpg"},
            {"name": "Gardens by the Bay", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/nine/Supertree_grove_Singapore.jpg/640px-Supertree_grove_Singapore.jpg"},
            {"name": "Sentosa Island", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Sentosa_Island_Singapore.jpg/640px-Sentosa_Island_Singapore.jpg"},
            {"name": "Chinatown", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Singapore_Chinatown_2.jpg/640px-Singapore_Chinatown_2.jpg"},
            {"name": "Little India", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Little_India%2C_Singapore_-_20110723.jpg/640px-Little_India%2C_Singapore_-_20110723.jpg"},
            {"name": "Singapore Zoo", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/forty/Singapore_Zoo.jpg/640px-Singapore_Zoo.jpg"},
        ],
        "restaurants": [
            {"name": "Lau Pa Sat", "img": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600"},
            {"name": "Ce La Vi", "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600"},
            {"name": "Burnt Ends", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600"},
            {"name": "Hawker Chan", "img": "https://images.unsplash.com/photo-1544148103-0773bf10d330?w=600"},
            {"name": "Odette", "img": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=600"},
        ],
        "activities": [
            {"name": "Night Safari", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/nine/Night_Safari_Singapore.jpg/640px-Night_Safari_Singapore.jpg"},
            {"name": "Universal Studios", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Universal_Studios_Singapore_2.jpg/640px-Universal_Studios_Singapore_2.jpg"},
            {"name": "Cable Car Ride", "img": "https://images.unsplash.com/photo-1548438294-1ad5d5f4f063?w=600"},
            {"name": "Bumboat River Cruise", "img": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600"},
            {"name": "ArtScience Museum", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/ArtScience_Museum_Jan_2013.jpg/640px-ArtScience_Museum_Jan_2013.jpg"},
        ]
    }
}


def generate_itinerary(city, days):
    city = city.lower()
    if city not in city_data:
        return []

    data = city_data[city]

    attractions = data["attractions"].copy()
    restaurants = data["restaurants"].copy()
    activities  = data["activities"].copy()

    random.shuffle(attractions)
    random.shuffle(restaurants)
    random.shuffle(activities)

    itinerary = []
    for i in range(days):
        day_plan = {
            "visit": attractions[i % len(attractions)]["name"],
            "eat":   restaurants[i % len(restaurants)]["name"],
            "do":    activities[i % len(activities)]["name"]
        }
        itinerary.append(day_plan)

    return itinerary