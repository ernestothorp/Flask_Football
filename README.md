##  Football

This small project can import football results via API and analyse the data in flask.

It was created to learn flask, API integration, data processing and data visualization.

**Note:** The project has been migrated from web scraping to using API-Football.com. See [API_MIGRATION.md](API_MIGRATION.md) for details.  


### Features

- flask generates an interactive GUI environment
- extract soccer results from API-Football.com (German Bundesliga, 2. Bundesliga, 3. Liga)
- format and save the data in CSV-files automatically
- get season overviews 
- create dynamic data diagrams
- calculate the attack/defence value of each club and try to predict the results (based on poisson)
- compare the predicted and real results by using the coefficient of determination (R²)

------------
------------
------------

### First Steps: 

#### Setup API Key

1. Get a free API key from [RapidAPI API-Football](https://rapidapi.com/api-sports/api/api-football)
2. Set environment variable: `export API_FOOTBALL_KEY="your_key"`
3. Or edit `GET_Data_API.py` and add your key directly

See [API_MIGRATION.md](API_MIGRATION.md) for detailed setup instructions.

#### Import results

- open ```main.py``` and configure league and season:

```python
league_name = "1_Bundesliga"  # or "2_Bundesliga", "3_Liga"
season = 2024
```

- run:
```python
GET_ALL_ROUNDS(league_name, season, max_rounds=34)
```

- results will be saved in a CSV-file automatically (folder: CSV) 

</br>

#### Select a data source 

- open ```main.py``` and select the CSV-file you want to work with:

```python
file = "./CSV/1_Bundesliga_2024.csv"
```

------------
------------
------------

### GUI

start ```START_Gui.py``` (default IP: 127.0.0.1:5000)

###### choose a club in the dropdown menu:

<img src="pics/dropdown.png" alt="drawing" width="300"/>

###### now you can switch between the options and analyse the data:

<img src="pics/menu.png" alt="drawing" width="400"/>

</br>

------------

#### Example calculation:

</br>

<img src="pics/prediction.png" alt="drawing" width="600"/>



