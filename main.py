from GET_Data_API import GET_TABLE, CREATE_CSV, GET_ALL_ROUNDS, GET_FIXTURES
from GET_Calc import GET_ALL_GOALS, GET_ATT_DEF_VALUE, GET_ATT_DEF_ANALYSE, GET_ESTIMATE_GOALS_POISSON , GET_POINTS, GET_SEASON, GET_STATS_FROM_CLUB, CALC_SEASON_POISSON, GET_ALL_CLUBS

league_name = "1_Bundesliga"
season = 2024

#print(GET_TABLE(league_name, season))

#CREATE_CSV(league_name, season, round_number=13)

#GET_ALL_ROUNDS(league_name, season, max_rounds=34)




file = "./CSV/1_Bundesliga_2024.csv"


#print(GET_ALL_CLUBS(file))

#print(GET_ALL_GOALS(file))

#print(GET_STATS_FROM_CLUB("Eintracht Frankfurt", file, 1))

# [Games_Sum, [Games_Home, [Goals, Goals_AVG, Trend], [Hits, Hits_AVG, Trend]], 
#             [Games_Out,  [Goals, Goals_AVG, Trend], [Hits, Hits_AVG, Trend]]]


#print(GET_ATT_DEF_VALUE("Borussia Dortmund", file))

# [ATT_Home, DEF_Home, ATT_Out, DEF_Out]

#print(GET_ATT_DEF_ANALYSE("Borussia Dortmund", file))

#print(GET_ESTIMATE_GOALS_POISSON("Eintracht Frankfurt", "Bayern München", file))

#print(GET_POINTS("Bayern München", file))

#print(GET_SEASON("Eintracht Frankfurt", file))

print(CALC_SEASON_POISSON("Eintracht Frankfurt", file))

# [[Day, Location, Opponent, [Estimate_Goals, [Poisson], 
#                             Estimate_Hits,  [Poisson]], 
#                           [[Real_Result],   [Difference], [Trend(Club_Goals, Club_Hits)]]]  

