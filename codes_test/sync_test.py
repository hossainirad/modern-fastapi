from typing import Optional
from colorama import Fore
from time import sleep

def show_some_numbers(num: Optional[int]) -> str:
    counter = 0
    total = 0
    for i in range(num):
        total += 1
        sleep(.3)
    return str(total)



print(Fore.RED + show_some_numbers(10))
print(Fore.GREEN + show_some_numbers(10))