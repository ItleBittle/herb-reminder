import python_weather as pw
from dotenv import load_dotenv
import os

load_dotenv()

LOCATION = os.getenv("LOCATION")

async def get_low_today():
    async with pw.Client(unit=pw.IMPERIAL) as client:
        weather = await client.get(LOCATION)

        today = weather.daily_forecasts[0]
        low_today = today.lowest_temperature

        return low_today