import asyncio
from typing import Optional
from colorama import Fore
from time import sleep

async def show_some_numbers(num: Optional[int]) -> str:
    counter = 0
    total = 0
    for i in range(num):
        total += 1
        asyncio.sleep(.3)
    return str(total)


def send_tweet_with_image():
    pass

print(Fore.RED + asyncio.run(show_some_numbers(10)))
print(Fore.GREEN + asyncio.run(show_some_numbers(10)))