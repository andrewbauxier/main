def start():
    print("hello anchan_full_state")


us_states_dictionary = {
    "alabama": {
        "state_code": "al",
        "capital": "Montgomery",
        "population": 196010,
        "flower": "Camellia",
    },
    "alaska": {
        "state_code": "ak",
        "capital": "Juneau",
        "population": 31534,
        "flower": "Forget-me-not",
    },
    "arizona": {
        "state_code": "az",
        "capital": "Phoenix",
        "population": 1651344,
        "flower": "Saguaro Cactus Blossom",
    },
    "arkansas": {
        "state_code": "ar",
        "capital": "Little Rock",
        "population": 201029,
        "flower": "Apple Blossom",
    },
    "california": {
        "state_code": "ca",
        "capital": "Sacramento",
        "population": 528306,
        "flower": "California Poppy",
    },
    "colorado": {
        "state_code": "co",
        "capital": "Denver",
        "population": 699288,
        "flower": "Rocky Mountain Columbine",
    },
    "connecticut": {
        "state_code": "ct",
        "capital": "Hartford",
        "population": 119817,
        "flower": "Mountain Laurel",
    },
    "delaware": {
        "state_code": "de",
        "capital": "Dover",
        "population": 37892,
        "flower": "Peach Blossom",
    },
    "florida": {
        "state_code": "fl",
        "capital": "Tallahassee",
        "population": 198631,
        "flower": "Orange Blossom",
    },
    "georgia": {
        "state_code": "ga",
        "capital": "Atlanta",
        "population": 490270,
        "flower": "Cherokee Rose",
    },
    "hawaii": {
        "state_code": "hi",
        "capital": "Honolulu",
        "population": 337088,
        "flower": "Hibiscus",
    },
    "idaho": {
        "state_code": "id",
        "capital": "Boise",
        "population": 240713,
        "flower": "Syringa",
    },
    "illinois": {
        "state_code": "il",
        "capital": "Springfield",
        "population": 111711,
        "flower": "Violet",
    },
    "indiana": {
        "state_code": "in",
        "capital": "Indianapolis",
        "population": 871449,
        "flower": "Peony",
    },
    "iowa": {
        "state_code": "ia",
        "capital": "Des Moines",
        "population": 208734,
        "flower": "Wild Prairie Rose",
    },
    "kansas": {
        "state_code": "ks",
        "capital": "Topeka",
        "population": 125353,
        "flower": "Sunflower",
    },
    "kentucky": {
        "state_code": "ky",
        "capital": "Frankfort",
        "population": 28523,
        "flower": "Goldenrod",
    },
    "louisiana": {
        "state_code": "la",
        "capital": "Baton Rouge",
        "population": 217665,
        "flower": "Magnolia",
    },
    "maine": {
        "state_code": "me",
        "capital": "Augusta",
        "population": 19058,
        "flower": "White Pine Cone and Tassel",
    },
    "maryland": {
        "state_code": "md",
        "capital": "Annapolis",
        "population": 40397,
        "flower": "Black-Eyed Susan",
    },
    "massachusetts": {
        "state_code": "ma",
        "capital": "Boston",
        "population": 617459,
        "flower": "Mayflower",
    },
    "michigan": {
        "state_code": "mi",
        "capital": "Lansing",
        "population": 112460,
        "flower": "Apple Blossom",
    },
    "minnesota": {
        "state_code": "mn",
        "capital": "St. Paul",
        "population": 299830,
        "flower": "Pink and White Lady's Slipper",
    },
    "mississippi": {
        "state_code": "ms",
        "capital": "Jackson",
        "population": 143776,
        "flower": "Magnolia",
    },
    "missouri": {
        "state_code": "mo",
        "capital": "Jefferson City",
        "population": 42535,
        "flower": "Hawthorn",
    },
    "montana": {
        "state_code": "mt",
        "capital": "Helena",
        "population": 34690,
        "flower": "Bitterroot",
    },
    "nebraska": {
        "state_code": "ne",
        "capital": "Lincoln",
        "population": 295222,
        "flower": "Goldenrod",
    },
    "nevada": {
        "state_code": "nv",
        "capital": "Carson City",
        "population": 59630,
        "flower": "Sagebrush",
    },
    "new hampshire": {
        "state_code": "nh",
        "capital": "Concord",
        "population": 44606,
        "flower": "Purple Lilac",
    },
    "new jersey": {
        "state_code": "nj",
        "capital": "Trenton",
        "population": 90048,
        "flower": "Violet",
    },
    "new mexico": {
        "state_code": "nm",
        "capital": "Santa Fe",
        "population": 89220,
        "flower": "Yucca Flower",
    },
    "new york": {
        "state_code": "ny",
        "capital": "Albany",
        "population": 97593,
        "flower": "Rose",
    },
    "north carolina": {
        "state_code": "nc",
        "capital": "Raleigh",
        "population": 472540,
        "flower": "Flowering Dogwood",
    },
    "north dakota": {
        "state_code": "nd",
        "capital": "Bismarck",
        "population": 75073,
        "flower": "Wild Prairie Rose",
    },
    "ohio": {
        "state_code": "oh",
        "capital": "Columbus",
        "population": 907865,
        "flower": "Scarlet Carnation",
    },
    "oklahoma": {
        "state_code": "ok",
        "capital": "Oklahoma City",
        "population": 697763,
        "flower": "Oklahoma Rose",
    },
    "oregon": {
        "state_code": "or",
        "capital": "Salem",
        "population": 181620,
        "flower": "Oregon Grape",
    },
    "pennsylvania": {
        "state_code": "pa",
        "capital": "Harrisburg",
        "population": 50267,
        "flower": "Mountain Laurel",
    },
    "rhode island": {
        "state_code": "ri",
        "capital": "Providence",
        "population": 179883,
        "flower": "Violet",
    },
    "south carolina": {
        "state_code": "sc",
        "capital": "Columbia",
        "population": 133273,
        "flower": "Yellow Jessamine",
    },
    "south dakota": {
        "state_code": "sd",
        "capital": "Pierre",
        "population": 14033,
        "flower": "Pasque Flower",
    },
    "tennessee": {
        "state_code": "tn",
        "capital": "Nashville",
        "population": 689006,
        "flower": "Iris",
    },
    "texas": {
        "state_code": "tx",
        "capital": "Austin",
        "population": 978908,
        "flower": "Bluebonnet",
    },
    "utah": {
        "state_code": "ut",
        "capital": "Salt Lake City",
        "population": 199936,
        "flower": "Sego Lily",
    },
    "vermont": {
        "state_code": "vt",
        "capital": "Montpelier",
        "population": 7902,
        "flower": "Red Clover",
    },
    "virginia": {
        "state_code": "va",
        "capital": "Richmond",
        "population": 232226,
        "flower": "Dogwood",
    },
    "washington": {
        "state_code": "wa",
        "capital": "Olympia",
        "population": 53764,
        "flower": "Coast Rhododendron",
    },
    "west virginia": {
        "state_code": "wv",
        "capital": "Charleston",
        "population": 46204,
        "flower": "Rhododendron",
    },
    "wisconsin": {
        "state_code": "wi",
        "capital": "Madison",
        "population": 259680,
        "flower": "Wood Violet",
    },
    "wyoming": {
        "state_code": "wy",
        "capital": "Cheyenne",
        "population": 64235,
        "flower": "Indian Paintbrush",
    },
}


def display_all_states_alphabetical():
    for state_name_and_entry, state_data_item in us_states_dictionary.items():
        print(state_name_and_entry)
        print("Capital:", state_data_item["capital"])
        print("Population:", state_data_item["population"])
        print("Flower:", state_data_item["flower"])
        print()


def get_state():
    find_state_by_name = input(
        "Enter the state name or two digit representation:\t"
    )  # Prompt state name
    state_data_lookup_results = us_states_dictionary.get(
        find_state_by_name.lower()
    )  # Retrieve state info

    for state_name_and_entry_id, state_data_item in us_states_dictionary.items():
        if (
            state_name_and_entry_id.lower() == find_state_by_name
            or state_data_item["state_code"] == find_state_by_name
        ):
            state_data_lookup_results = state_data_item
            break

    if state_data_lookup_results:
        print()
        print(state_name_and_entry_id.capitalize())
        print("Capital:", state_data_lookup_results["capital"])
        print("Population:", state_data_lookup_results["population"])
        print("Flower:", state_data_lookup_results["flower"])
        print()
    else:
        print("State not found.")
