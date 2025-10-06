import os

class Config:
    VERSION = "0.1"
    DEBUG = True
    OPENWEATHER_KEY = os.getenv("OPENWEATHER_API_KEY")
    JSON_SORT_KEYS = False
    APP_NAME = "Week 4 Flask API"
