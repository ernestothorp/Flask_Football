from GET_Data_API import GET_TABLE, GET_FIXTURES, CREATE_CSV, GET_ALL_ROUNDS

print("=" * 60)
print("API-Football.com Integration Example")
print("=" * 60)
print()

league_name = "1_Bundesliga"
season = 2024

print(f"League: {league_name}")
print(f"Season: {season}")
print()

print("Available leagues:")
print("  - 1_Bundesliga (Bundesliga)")
print("  - 2_Bundesliga (2. Bundesliga)")
print("  - 3_Liga (3. Liga)")
print()

print("-" * 60)
print("Example 1: Fetch League Standings")
print("-" * 60)

standings = GET_TABLE(league_name, season)
if standings:
    print(f"\n{standings[0]} - Season {standings[1]}")
    print("\nTop 5 Teams:")
    for i in range(3, min(8, len(standings))):
        team_data = standings[i]
        print(f"{team_data[0]}. {team_data[1]} - {team_data[8]} points")
else:
    print("Could not fetch standings. Check your API key and connection.")

print()
print("-" * 60)
print("Example 2: Fetch Fixtures for Round 1")
print("-" * 60)

fixtures = GET_FIXTURES(league_name, season, round_number=1)
if fixtures:
    print(f"\nFixtures for Round {fixtures[2]}:")
    for i in range(3, min(12, len(fixtures)), 3):
        if i+2 < len(fixtures):
            print(f"{fixtures[i]} {fixtures[i+1]} {fixtures[i+2]}")
else:
    print("Could not fetch fixtures.")

print()
print("-" * 60)
print("Example 3: Save Round Data to CSV")
print("-" * 60)

print("\nSaving round 1 to CSV...")
CREATE_CSV(league_name, season, round_number=1)

print()
print("-" * 60)
print("Example 4: Fetch All Rounds (Commented Out)")
print("-" * 60)

print("""
To fetch all rounds for a season, uncomment and run:

    GET_ALL_ROUNDS(league_name, season, max_rounds=34)

Note: This will use 34 API requests. Free tier allows 100/day.
""")

print()
print("=" * 60)
print("Setup Instructions:")
print("=" * 60)
print("""
1. Get free API key from: https://rapidapi.com/api-sports/api/api-football
2. Set environment variable: export API_FOOTBALL_KEY="your_key"
3. Or edit GET_Data_API.py line 6 with your key

For more details, see API_MIGRATION.md
""")
print("=" * 60)
