metro_lines = {
    "1": {
        "name": "blue line 1",
        "stations": [
            "versova",
            "dn nagar",
            "azad nagar",
            "andheri",
            "western express highway",
            "chakala",
            "airport road",
            "marol naka",
            "saki naka",
            "asalpha",
            "jagruti nagar",
            "ghatkopar"
        ]
    },
    "2": {
        "name": "yellow line 2a",
        "stations": [
            "dahanukarwadi",
            "kandivali west",
            "pahadi goregaon",
            "goregaon west",
            "oshiwara",
            "lower oshiwara",
            "dn nagar",
            "andheri west"
        ]
    },
    "3": {
        "name": "red line 7",
        "stations": [
            "dahisar east",
            "ovaripada",
            "national park",
            "devipada",
            "magathane",
            "poisar",
            "akurli",
            "kurar",
            "dindoshi",
            "gundavali"
        ]
    }
}

def show_available_lines():
    print("\n--- available metro lines ---")
    print("1. blue line 1 (versova - ghatkopar)")
    print("2. yellow line 2a (dahanukarwadi - andheri west)")
    print("3. red line 7 (dahisar east - gundavali)")
    print("-----------------------------")

def show_stations_in_line(line_choice):
    selected_line = metro_lines[line_choice]
    print("\n--- stations on " + selected_line["name"] + " ---")
    num = 1
    for s in selected_line["stations"]:
        print(num, ".", s)
        num = num + 1
    print("----------------------------------------")

def find_station(user_input, stations_list):
    clean_input = user_input.strip().lower()
    for s in stations_list:
        if s.lower() == clean_input:
            return s
    return None