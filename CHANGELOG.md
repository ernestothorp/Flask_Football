# Changelog

## [2.0.0] - API Migration - 2026-06-16

### Major Changes

#### Migrated from Web Scraping to API-Football.com
- **Reason**: The DFB website structure changed completely, making the old web scraping approach obsolete
- **New Data Source**: API-Football via RapidAPI (https://rapidapi.com/api-sports/api/api-football)
- **Benefits**:
  - More reliable data access
  - No breaking changes when website updates
  - Structured JSON responses
  - Better error handling
  - Access to more detailed statistics

### Added

#### New Files
- `GET_Data_API.py` - New API-based data fetching module
- `API_MIGRATION.md` - Comprehensive migration guide
- `example_api_usage.py` - Example script demonstrating API usage
- `.env.example` - Template for environment variables
- `CHANGELOG.md` - This file

#### New Functions in GET_Data_API.py
- `get_api_headers()` - Returns headers for API requests
- `GET_LEAGUE_STANDINGS(league_name, season)` - Fetch league table/standings
- `GET_FIXTURES(league_name, season, round_number)` - Fetch match fixtures
- `CREATE_CSV(league_name, season, round_number)` - Save data to CSV
- `GET_ALL_ROUNDS(league_name, season, max_rounds)` - Fetch all rounds for a season
- `GET_TABLE(league_name, season)` - Alias for standings

#### League Support
- Bundesliga (1_Bundesliga) - League ID: 78
- 2. Bundesliga (2_Bundesliga) - League ID: 79
- 3. Liga (3_Liga) - League ID: 80

### Changed

#### Modified Files
- `main.py` - Updated imports and examples to use API-based functions
- `README.md` - Updated instructions for API usage
- File paths changed from `./Python_Projects/Football/CSV/` to `./CSV/`

#### API Changes
**Old (Web Scraping):**
```python
from GET_Data import GET_ALL, CREATE_CSV
url = "https://www.dfb.de/..."
GET_ALL(url)
```

**New (API):**
```python
from GET_Data_API import GET_ALL_ROUNDS, CREATE_CSV
league_name = "1_Bundesliga"
season = 2024
GET_ALL_ROUNDS(league_name, season)
```

### Deprecated

- `GET_Data.py` - Old web scraping module (kept for reference, no longer functional)
- DFB URL-based functions
- `GET_RESULTS(url)` - Replaced by `GET_FIXTURES(league_name, season, round_number)`
- `GET_CROSS_TABLE(url)` - Not yet implemented in API version
- `GET_ALL(url)` - Replaced by `GET_ALL_ROUNDS(league_name, season)`

### Requirements

#### API Key Required
- Users must obtain a free API key from RapidAPI
- Free tier: 100 requests/day
- See API_MIGRATION.md for setup instructions

#### Environment Variables
- `API_FOOTBALL_KEY` - Your RapidAPI key for API-Football

### CSV Format

CSV output format remains unchanged for backward compatibility:
```csv
Spieltag,Status,Team_1,Team_2,Tore_Team_1,Tore_Team_2
```

### Migration Guide

See [API_MIGRATION.md](API_MIGRATION.md) for:
- How to get an API key
- Configuration instructions
- Usage examples
- Troubleshooting tips
- API rate limits and pricing

### Notes

- The `GET_Calc.py` module remains unchanged and works with CSV files from both old and new systems
- Flask GUI (`START_Gui.py`) should work without changes as it reads from CSV files
- Historical data depends on API availability
- Season parameter format: use year (e.g., 2024) not year range (e.g., 2024/2025)

### Breaking Changes

1. **Import Changes**: Old imports from `GET_Data` will not work
2. **Parameter Changes**: Functions now use `league_name` and `season` instead of `url`
3. **API Key Required**: Application won't work without valid API key
4. **Rate Limits**: Free tier has 100 requests/day limit

### Backward Compatibility

The following remain compatible:
- CSV file format
- `GET_Calc.py` functions
- Flask GUI interface
- Directory structure (updated to ./CSV/)

### Future Enhancements

Potential additions for future versions:
- Implement cross table functionality via API
- Add caching to reduce API calls
- Support for more leagues (Premier League, La Liga, etc.)
- Real-time match updates
- Player statistics integration
- Team form analysis

---

## [1.0.0] - Initial Release

### Features
- Web scraping from DFB website
- CSV data export
- Flask-based GUI
- Poisson distribution predictions
- Attack/Defense value calculations
- Season analysis and statistics
