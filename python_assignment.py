class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def search_by_team(self, team_name):
        team_matches = [match for match in self.matches if team_name in (match.team1, match.team2)]
        return team_matches

    def search_by_location(self, location):
        location_matches = [match for match in self.matches if match.location == location]
        return location_matches

    def search_by_timing(self, timing):
        timing_matches = [match for match in self.matches if match.timing == timing]
        return timing_matches

def main():
    flight_table = FlightTable()

    flight_table.add_match(Match("Mumbai", "India", "Sri Lanka", "DAY"))
    flight_table.add_match(Match("Delhi", "England", "Australia", "DAY-NIGHT"))
    flight_table.add_match(Match("Chennai", "India", "South Africa", "DAY"))
    flight_table.add_match(Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    flight_table.add_match(Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    flight_table.add_match(Match("Delhi", "India", "Australia", "DAY"))

    while True:
        print("Search options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            team_name = input("Enter the team name: ")
            team_matches = flight_table.search_by_team(team_name)
            if team_matches:
                print("Matches for", team_name)
                for match in team_matches:
                    print(match.location, match.team1, "vs", match.team2, match.timing)
            else:
                print("No matches found for", team_name)
        
        elif choice == '2':
            location = input("Enter the location: ")
            location_matches = flight_table.search_by_location(location)
            if location_matches:
                print("Matches at", location)
                for match in location_matches:
                    print(match.location, match.team1, "vs", match.team2, match.timing)
            else:
                print("No matches found at", location)
        
        elif choice == '3':
            timing = input("Enter the timing: ")
            timing_matches = flight_table.search_by_timing(timing)
            if timing_matches:
                print("Matches at", timing, "timing")
                for match in timing_matches:
                    print(match.location, match.team1, "vs", match.team2, match.timing)
            else:
                print("No matches found at", timing, "timing")
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
