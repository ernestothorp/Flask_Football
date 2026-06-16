import requests
import csv
import time
import os
from datetime import datetime

API_KEY = os.getenv("API_FOOTBALL_KEY", "YOUR_API_KEY_HERE")
API_HOST = "v3.football.api-sports.io"
API_BASE_URL = f"https://{API_HOST}"

LEAGUE_IDS = {
    "1_Bundesliga": 78,
    "2_Bundesliga": 79,
    "3_Liga": 80
}

def get_api_headers():
    return {
        'x-rapidapi-host': API_HOST,
        'x-rapidapi-key': API_KEY
    }

def GET_LEAGUE_STANDINGS(league_name, season):
    league_id = LEAGUE_IDS.get(league_name)
    if not league_id:
        print(f"Unknown league: {league_name}")
        return None
    
    url = f"{API_BASE_URL}/standings"
    params = {
        'league': league_id,
        'season': season
    }
    
    try:
        response = requests.get(url, headers=get_api_headers(), params=params)
        response.raise_for_status()
        data = response.json()
        
        if data['response'] and len(data['response']) > 0:
            standings = data['response'][0]['league']['standings'][0]
            
            table = []
            table.append(league_name)
            table.append(str(season))
            table.append("All")
            
            for team in standings:
                row = [
                    team['rank'],
                    team['team']['name'],
                    team['all']['played'],
                    team['all']['win'],
                    team['all']['draw'],
                    team['all']['lose'],
                    f"{team['all']['goals']['for']}:{team['all']['goals']['against']}",
                    team['goalsDiff'],
                    team['points']
                ]
                table.append(row)
            
            return table
        else:
            print("No standings data available")
            return None
            
    except Exception as e:
        print(f"Error fetching standings: {e}")
        return None

def GET_FIXTURES(league_name, season, round_number=None):
    league_id = LEAGUE_IDS.get(league_name)
    if not league_id:
        print(f"Unknown league: {league_name}")
        return None
    
    url = f"{API_BASE_URL}/fixtures"
    params = {
        'league': league_id,
        'season': season
    }
    
    if round_number:
        params['round'] = f"Regular Season - {round_number}"
    
    try:
        response = requests.get(url, headers=get_api_headers(), params=params)
        response.raise_for_status()
        data = response.json()
        
        fixtures = []
        fixtures.append(league_name)
        fixtures.append(str(season))
        
        if round_number:
            fixtures.append(str(round_number).zfill(2))
        else:
            fixtures.append("All")
        
        if data['response']:
            for match in data['response']:
                home_team = match['teams']['home']['name']
                away_team = match['teams']['away']['name']
                home_goals = match['goals']['home']
                away_goals = match['goals']['away']
                status = match['fixture']['status']['short']
                
                if status == 'FT':
                    status_text = "PASS"
                    goals_home = home_goals if home_goals is not None else ""
                    goals_away = away_goals if away_goals is not None else ""
                else:
                    status_text = "OPEN"
                    goals_home = ""
                    goals_away = ""
                
                fixtures.extend([home_team, f"{goals_home}:{goals_away}", away_team])
        
        return fixtures
        
    except Exception as e:
        print(f"Error fetching fixtures: {e}")
        return None

def CREATE_CSV(league_name, season, round_number=None):
    fixtures_data = GET_FIXTURES(league_name, season, round_number)
    
    if not fixtures_data:
        print("No data to save")
        return
    
    league = fixtures_data[0]
    season_str = fixtures_data[1].replace("/", "_")
    
    csv_dir = "./CSV"
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)
    
    file_path = f"{csv_dir}/{league}_{season_str}.csv"
    
    exist_entry = False
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            spamreader = csv.reader(f)
            for row in spamreader:
                if row is not None:
                    exist_entry = True
                    break
    except FileNotFoundError:
        pass
    
    with open(file_path, mode='a', encoding="utf-8", newline='') as result_file:
        result_writer = csv.writer(result_file, delimiter=',')
        
        if not exist_entry:
            result_writer.writerow(["Spieltag", "Status", "Team_1", "Team_2", "Tore_Team_1", "Tore_Team_2"])
        
        spieltag = fixtures_data[2]
        
        for i in range(3, len(fixtures_data), 3):
            if i+2 < len(fixtures_data):
                team_1 = fixtures_data[i]
                score = fixtures_data[i+1]
                team_2 = fixtures_data[i+2]
                
                if ":" in score and score != ":":
                    goals = score.split(":")
                    goals_team_1 = goals[0].strip()
                    goals_team_2 = goals[1].strip()
                    
                    if goals_team_1 and goals_team_2:
                        status = "PASS"
                        result_writer.writerow([spieltag, status, team_1, team_2, goals_team_1, goals_team_2])
                    else:
                        status = "OPEN"
                        result_writer.writerow([spieltag, status, team_1, team_2, "", ""])
                else:
                    status = "OPEN"
                    result_writer.writerow([spieltag, status, team_1, team_2, "", ""])
    
    print(f"CSV updated: {file_path}")

def GET_ALL_ROUNDS(league_name, season, max_rounds=34):
    csv_dir = "./CSV"
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)
    
    league = league_name
    season_str = str(season).replace("/", "_")
    file_path = f"{csv_dir}/{league}_{season_str}.csv"
    
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted existing file: {file_path}")
    
    for round_num in range(1, max_rounds + 1):
        print(f"Fetching round {round_num}...")
        CREATE_CSV(league_name, season, round_num)
        time.sleep(1)
    
    print(f"All rounds fetched for {league_name} season {season}")

def GET_TABLE(league_name, season):
    return GET_LEAGUE_STANDINGS(league_name, season)
