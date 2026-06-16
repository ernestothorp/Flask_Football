# Quick Start Guide

## 1. Get Your API Key (5 minutes)

1. Visit https://rapidapi.com/api-sports/api/api-football
2. Click "Sign Up" (free account)
3. Click "Subscribe to Test" (select the FREE plan - 100 requests/day)
4. Copy your API key from the dashboard

## 2. Configure the Project

### Option A: Environment Variable (Recommended)

**Linux/Mac:**
```bash
export API_FOOTBALL_KEY="your_api_key_here"
```

**Windows (PowerShell):**
```powershell
$env:API_FOOTBALL_KEY="your_api_key_here"
```

**Windows (CMD):**
```cmd
set API_FOOTBALL_KEY=your_api_key_here
```

### Option B: Edit the File Directly

Open `GET_Data_API.py` and change line 6:
```python
API_KEY = os.getenv("API_FOOTBALL_KEY", "paste_your_key_here")
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Test the API Connection

Run the example script:
```bash
python example_api_usage.py
```

If successful, you should see:
- League standings for Bundesliga 2024
- Fixtures for Round 1
- A new CSV file created in the `CSV/` folder

## 5. Fetch Data

### Fetch a Single Round
```bash
python -c "from GET_Data_API import CREATE_CSV; CREATE_CSV('1_Bundesliga', 2024, 1)"
```

### Fetch All Rounds for a Season
```bash
python -c "from GET_Data_API import GET_ALL_ROUNDS; GET_ALL_ROUNDS('1_Bundesliga', 2024, 34)"
```

**Note:** This uses 34 API requests. Free tier = 100 requests/day.

## 6. Available Leagues

| League Name | Description | Rounds |
|------------|-------------|--------|
| `1_Bundesliga` | German Bundesliga | 34 |
| `2_Bundesliga` | German 2nd Division | 34 |
| `3_Liga` | German 3rd Division | 38 |

## 7. Use the Data

After fetching data, CSV files will be in the `CSV/` folder:
```
CSV/
  ├── 1_Bundesliga_2024.csv
  ├── 2_Bundesliga_2024.csv
  └── 3_Liga_2024.csv
```

Now you can run the analysis functions in `main.py`:

```python
from GET_Data_API import GET_ALL_ROUNDS
from GET_Calc import GET_ALL_CLUBS, CALC_SEASON_POISSON

# Fetch data
GET_ALL_ROUNDS("1_Bundesliga", 2024, 34)

# Analyze
file = "./CSV/1_Bundesliga_2024.csv"
clubs = GET_ALL_CLUBS(file)
print(clubs)

predictions = CALC_SEASON_POISSON("Bayern München", file)
print(predictions)
```

## 8. Run the Flask GUI

```bash
python START_Gui.py
```

Then open your browser to: http://127.0.0.1:5000

## Common Issues

### "403 Forbidden"
- Check your API key is correct
- Verify you subscribed to the API on RapidAPI
- Check you haven't exceeded 100 requests/day

### "No data available"
- Make sure you're using the correct season year (2024, not 2024/2025)
- Some historical seasons may not be available
- Try the current or recent seasons first

### "Module not found"
```bash
pip install flask flask_bootstrap requests beautifulsoup4 pandas numpy scipy matplotlib
```

## Next Steps

1. Read [API_MIGRATION.md](API_MIGRATION.md) for detailed documentation
2. Explore the analysis functions in `GET_Calc.py`
3. Customize the Flask GUI in `START_Gui.py`
4. Check [CHANGELOG.md](CHANGELOG.md) for what's new

## Rate Limits

**FREE Tier:**
- 100 requests/day
- Enough for 2-3 full seasons per day

**Tips to Save Requests:**
- Fetch data once and reuse CSV files
- Don't fetch historical data repeatedly
- Consider upgrading if you need more

## Support

- API Documentation: https://www.api-football.com/documentation-v3
- RapidAPI Hub: https://rapidapi.com/api-sports/api/api-football
- Issues: Check the GitHub repository (if applicable)

---

**Happy analyzing!** ⚽📊
