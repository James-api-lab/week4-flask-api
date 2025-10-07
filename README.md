# Week 4 — Flask API  
> Part of the API Learning Series (Python → Flask)

---

## 🧩 Project Overview
This week’s project transitions from CLI-based API exploration to **Flask-based web services**.  
We’re learning how to build real REST endpoints that return JSON, handle errors, and integrate live data.

By the end of Week 4, you’ll have:
- A functioning Flask API with live weather data
- Proper routing, logging, caching, and persistence
- Modular config and error handling
- A foundation for future visualization (Day 5)

---

## 🧱 Current Features (Days 1–3)

| Category | Endpoint | Description |
|-----------|-----------|-------------|
| **Core** | `/` | Root “API live” message |
|  | `/health` | Uptime and version |
|  | `/meta` | App metadata and cache count |
| **Demo Routes** | `/hello/<name>` | Path parameter example |
|  | `/square/<int:n>` | Type-converted path parameter |
|  | `/add?a=5&b=9` | Query parameters |
|  | `/echo` *(POST JSON)* | Echoes the request body |
|  | `/headers` | Debug view of request headers |
| **Weather** | `/weather/<city>` | Single city weather (OpenWeather API) |
|  | `/weather?cities=Seattle,Paris,...` | Bulk fetch multiple cities concurrently |
| **Logging** | `logs/app.log` | Rotating runtime log |
|  | `data/access.log` | Simple HTTP request audit trail |
|  | `data/weather_log.csv` | CSV persistence of weather history |

---

## ⚙️ Configuration

### `.env`
Your environment file must live next to `app.py`:
```
OPENWEATHER_API_KEY=your_api_key_here
```

### `config.py`
```python
import os

class Config:
    VERSION = "0.1"
    DEBUG = True
    APP_NAME = "Week 4 Flask API"
    JSON_SORT_KEYS = False
    OPENWEATHER_KEY = os.getenv("OPENWEATHER_API_KEY")
```

---

## 🧠 How It Works

### 1. Request Flow
```
Browser / Curl  →  Flask Routes  →  Cache Check  →  OpenWeather API  →  Log + Return
```

### 2. Error Handling
All errors are returned as **clean JSON**:
```json
{
  "error": "Bad request",
  "detail": "Missing query param 'a'"
}
```

### 3. Example Calls
```bash
# Single city
curl.exe "http://127.0.0.1:5000/weather/Seattle"

# Bulk fetch (concurrent)
curl.exe "http://127.0.0.1:5000/weather?cities=Seattle,Tokyo,Paris"

# Add numbers
curl.exe "http://127.0.0.1:5000/add?a=5&b=9"

# JSON echo
curl.exe -X POST "http://127.0.0.1:5000/echo" -H "Content-Type: application/json" -d "{\"msg\":\"hi\"}"
```

---

## 📂 Logs & Data
All runtime artifacts are stored locally:

| File | Purpose |
|------|----------|
| `logs/app.log` | Rotating Flask event log |
| `data/access.log` | Request summary per hit |
| `data/weather_log.csv` | Persisted weather history |

---

## 🪶 Learning Goals
- Understand how a Python web framework translates HTTP requests into data responses.
- Learn to safely integrate live APIs.
- Build reusable helpers for caching, logging, and configuration.
- See how JSON-first design simplifies testing and client integration.

---

## 🚀 Next Steps (Day 4–5)
- `/history` endpoint → Read and summarize CSV logs  
- `/chart` endpoint → Generate trend graphs with QuickChart.io  
- Optional: SQLite persistence layer + unit tests  

---

**Author:** James Gilmore  
**Organization:** [James API Lab](https://github.com/James-api-lab)  
**License:** MIT
