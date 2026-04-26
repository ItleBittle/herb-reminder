from plants import get_plants
from weather import get_low_today
from notify import notify
import asyncio

async def main():
    low_today = await get_low_today()

    print(low_today)

    plants = get_plants()

    danger = []

    for plant in plants:
        if int(low_today) < int(plant["min_temp"]):
            danger.append(plant["name"])

    message = f"""
        The low temperature today is {low_today}.
        Please bring {danger} inside.
    """

    print(message)

    notify(message)

asyncio.run(main())