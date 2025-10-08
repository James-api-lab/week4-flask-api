# Week 4 – Flask API

## Overview
This week you built your first **Flask-based microservice** — a small, production-style REST API that logs, caches, and serves weather data.  
It marks the transition from CLI-based tools into **server-based API design**.

---

## Project Structure
```
Week 4 - Flask API/
│
├── app.py                # Main Flask app (routes, logging, caching)
├── config.py             # Configuration class
├── .env.example          # Example environment variables
├── data/
│   ├── access.log        # Text access log of all requests
│   ├── weather_log.csv   # Historical weather data
│
├── logs/
│   └── app.log           # Rotating log handler (1MB x 3 files)
│
└── README.md             # This file
```

---

## Endpoints Summary

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/` | GET | Basic API heartbeat |
| `/health` | GET | Returns uptime + version |
| `/meta` | GET | Shows app config metadata |
| `/hello/<name>` | GET | Dynamic greeting using path params |
| `/square/<int:n>` | GET | Example path param with type conversion |
| `/add?a=1&b=2` | GET | Example query params |
| `/echo` | POST | Echoes back JSON body |
| `/weather/<city>` | GET | Fetch current weather for one city |
| `/weather?cities=Seattle,Tokyo` | GET | Fetch multiple cities concurrently |
| `/history?city=Seattle&limit=7` | GET | Retrieve recent weather rows |
| `/history/daily` | GET | Summarized daily averages |
| `/chart/view` | GET | Redirects to QuickChart chart image |
| `/chart/html` | GET | Simple HTML page rendering a chart |

---

## Features Implemented
- ✅ Config via `.env` (OpenWeather key)
- ✅ Structured logging to `/logs` and `/data`
- ✅ Error handling (400/404/500)
- ✅ JSON request + response bodies
- ✅ In-memory caching with TTL
- ✅ CSV persistence (`data/weather_log.csv`)
- ✅ Concurrent bulk city fetch
- ✅ QuickChart integration for visual history

---

## Usage

**Run the server:**
```bash
flask --app app run
```

**Example requests (PowerShell):**
```powershell
iwr "http://127.0.0.1:5000/weather/Seattle"
iwr "http://127.0.0.1:5000/weather?cities=Seattle,Miami,Paris"
start http://127.0.0.1:5000/chart/view?city=Seattle&limit=7
```

---

## Next Steps
- Add authentication headers
- Introduce pagination and `per_page` params
- Deploy to Render or Railway
- Replace local CSV with SQLite for persistence

---

© 2025 James Gilmore | API Learning Journey Week 4


**Author:** James Gilmore  
**Organization:** [James API Lab](https://github.com/James-api-lab)  
**License:** MIT


