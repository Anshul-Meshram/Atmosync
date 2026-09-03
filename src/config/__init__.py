import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env")

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
LLM_API_KEY = os.getenv("LLM_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
