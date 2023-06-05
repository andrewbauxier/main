def start():
    print("hello anchan_full_state")


us_states = {
    "alabama": {
        "state_code": "al",
        "capital": "Montgomery",
        "state_population": 196010,
        "flower": "Camellia",
    },
    "alaska": {
        "state_code": "ak",
        "capital": "Juneau",
        "state_population": 31534,
        "flower": "Forget-me-not",
    },
    "arizona": {
        "state_code": "az",
        "capital": "Phoenix",
        "state_population": 1651344,
        "flower": "Saguaro Cactus Blossom",
    },
    "arkansas": {
        "state_code": "ar",
        "capital": "Little Rock",
        "state_population": 201029,
        "flower": "Apple Blossom",
    },
    "california": {
        "state_code": "ca",
        "capital": "Sacramento",
        "state_population": 528306,
        "flower": "California Poppy",
    },
    "colorado": {
        "state_code": "co",
        "capital": "Denver",
        "state_population": 699288,
        "flower": "Rocky Mountain Columbine",
    },
    "connecticut": {
        "state_code": "ct",
        "capital": "Hartford",
        "state_population": 119817,
        "flower": "Mountain Laurel",
    },
    "delaware": {
        "state_code": "de",
        "capital": "Dover",
        "state_population": 37892,
        "flower": "Peach Blossom",
    },
    "florida": {
        "state_code": "fl",
        "capital": "Tallahassee",
        "state_population": 198631,
        "flower": "Orange Blossom",
    },
    "georgia": {
        "state_code": "ga",
        "capital": "Atlanta",
        "state_population": 490270,
        "flower": "Cherokee Rose",
    },
    "hawaii": {
        "state_code": "hi",
        "capital": "Honolulu",
        "state_population": 337088,
        "flower": "Hibiscus",
    },
    "idaho": {
        "state_code": "id",
        "capital": "Boise",
        "state_population": 240713,
        "flower": "Syringa",
    },
    "illinois": {
        "state_code": "il",
        "capital": "Springfield",
        "state_population": 111711,
        "flower": "Violet",
    },
    "indiana": {
        "state_code": "in",
        "capital": "Indianapolis",
        "state_population": 871449,
        "flower": "Peony",
    },
    "iowa": {
        "state_code": "ia",
        "capital": "Des Moines",
        "state_population": 208734,
        "flower": "Wild Prairie Rose",
    },
    "kansas": {
        "state_code": "ks",
        "capital": "Topeka",
        "state_population": 125353,
        "flower": "Sunflower",
    },
    "kentucky": {
        "state_code": "ky",
        "capital": "Frankfort",
        "state_population": 28523,
        "flower": "Goldenrod",
    },
    "louisiana": {
        "state_code": "la",
        "capital": "Baton Rouge",
        "state_population": 217665,
        "flower": "Magnolia",
    },
    "maine": {
        "state_code": "me",
        "capital": "Augusta",
        "state_population": 19058,
        "flower": "White Pine Cone and Tassel",
    },
    "maryland": {
        "state_code": "md",
        "capital": "Annapolis",
        "state_population": 40397,
        "flower": "Black-Eyed Susan",
    },
    "massachusetts": {
        "state_code": "ma",
        "capital": "Boston",
        "state_population": 617459,
        "flower": "Mayflower",
    },
    "michigan": {
        "state_code": "mi",
        "capital": "Lansing",
        "state_population": 112460,
        "flower": "Apple Blossom",
    },
    "minnesota": {
        "state_code": "mn",
        "capital": "St. Paul",
        "state_population": 299830,
        "flower": "Pink and White Lady's Slipper",
    },
    "mississippi": {
        "state_code": "ms",
        "capital": "Jackson",
        "state_population": 143776,
        "flower": "Magnolia",
    },
    "missouri": {
        "state_code": "mo",
        "capital": "Jefferson City",
        "state_population": 42535,
        "flower": "Hawthorn",
    },
    "montana": {
        "state_code": "mt",
        "capital": "Helena",
        "state_population": 34690,
        "flower": "Bitterroot",
    },
    "nebraska": {
        "state_code": "ne",
        "capital": "Lincoln",
        "state_population": 295222,
        "flower": "Goldenrod",
    },
    "nevada": {
        "state_code": "nv",
        "capital": "Carson City",
        "state_population": 59630,
        "flower": "Sagebrush",
    },
    "new hampshire": {
        "state_code": "nh",
        "capital": "Concord",
        "state_population": 44606,
        "flower": "Purple Lilac",
    },
    "new jersey": {
        "state_code": "nj",
        "capital": "Trenton",
        "state_population": 90048,
        "flower": "Violet",
    },
    "new mexico": {
        "state_code": "nm",
        "capital": "Santa Fe",
        "state_population": 89220,
        "flower": "Yucca Flower",
    },
    "new york": {
        "state_code": "ny",
        "capital": "Albany",
        "state_population": 97593,
        "flower": "Rose",
    },
    "north carolina": {
        "state_code": "nc",
        "capital": "Raleigh",
        "state_population": 472540,
        "flower": "Flowering Dogwood",
    },
    "north dakota": {
        "state_code": "nd",
        "capital": "Bismarck",
        "state_population": 75073,
        "flower": "Wild Prairie Rose",
    },
    "ohio": {
        "state_code": "oh",
        "capital": "Columbus",
        "state_population": 907865,
        "flower": "Scarlet Carnation",
    },
    "oklahoma": {
        "state_code": "ok",
        "capital": "Oklahoma City",
        "state_population": 697763,
        "flower": "Oklahoma Rose",
    },
    "oregon": {
        "state_code": "or",
        "capital": "Salem",
        "state_population": 181620,
        "flower": "Oregon Grape",
    },
    "pennsylvania": {
        "state_code": "pa",
        "capital": "Harrisburg",
        "state_population": 50267,
        "flower": "Mountain Laurel",
    },
    "rhode island": {
        "state_code": "ri",
        "capital": "Providence",
        "state_population": 179883,
        "flower": "Violet",
    },
    "south carolina": {
        "state_code": "sc",
        "capital": "Columbia",
        "state_population": 133273,
        "flower": "Yellow Jessamine",
    },
    "south dakota": {
        "state_code": "sd",
        "capital": "Pierre",
        "state_population": 14033,
        "flower": "Pasque Flower",
    },
    "tennessee": {
        "state_code": "tn",
        "capital": "Nashville",
        "state_population": 689006,
        "flower": "Iris",
    },
    "texas": {
        "state_code": "tx",
        "capital": "Austin",
        "state_population": 978908,
        "flower": "Bluebonnet",
    },
    "utah": {
        "state_code": "ut",
        "capital": "Salt Lake City",
        "state_population": 199936,
        "flower": "Sego Lily",
    },
    "vermont": {
        "state_code": "vt",
        "capital": "Montpelier",
        "state_population": 7902,
        "flower": "Red Clover",
    },
    "virginia": {
        "state_code": "va",
        "capital": "Richmond",
        "state_population": 232226,
        "flower": "Dogwood",
    },
    "washington": {
        "state_code": "wa",
        "capital": "Olympia",
        "state_population": 53764,
        "flower": "Coast Rhododendron",
    },
    "west virginia": {
        "state_code": "wv",
        "capital": "Charleston",
        "state_population": 46204,
        "flower": "Rhododendron",
    },
    "wisconsin": {
        "state_code": "wi",
        "capital": "Madison",
        "state_population": 259680,
        "flower": "Wood Violet",
    },
    "wyoming": {
        "state_code": "wy",
        "capital": "Cheyenne",
        "state_population": 64235,
        "flower": "Indian Paintbrush",
    },
}

for state, data in us_states.items():
    print(state.capitalize())
    print("Capital:", data["capital"])
    print("Population:", data["state_population"])
    print("Flower:", data["flower"])
    print()
find_state_by_name = input(
    "Enter the state name or two digit representation: "
)  # Prompt the user to enter a state name
for state, state_code in us_states:
    if state_code == find_state_by_name:
        state_data_entry = us_states.get(find_state_by_name)  # Retrieve the state info

if state_data_entry:
    print(find_state_by_name.capitalize())
    print("Capital:", state_data_entry["capital"])
    print("Population:", state_data_entry["state_population"])
    print("Flower:", state_data_entry["flower"])
    print()
else:
    print(
        "Sorry, the state was not found. Please check your spelling and ensure it is correct."
    )
