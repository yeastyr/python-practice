# TERMINAL CLICKER

import functions
import time
import threading
from pynput import mouse

# VARIABLES 

click = 0
click_base = 1
cooldown = 1
auto_click = False
PROMPT = "\nAction? (Upgrade) : "

def STATS():
    print("---------------TERMINAL CLICKER---------------")
    print("\nClicks!", click)
    print("\nClick Base!", click_base)


def CLICKING(): # Clicking Function
    functions.clear()
    global click
    global click_base
    click = click + click_base
    STATS()
    print(PROMPT, end="", flush=True)


def MONEY_CHECK(price): # Money check function
    global click
    check = click - (price + click_base)
    if check < 0:
      return False
    elif check >= 0:
      return True 


def UPGRADE(price): # Upgrading Function
    global click
    global click_base
    global cost
    cost = price + click_base
    click = click - cost
    click_base = click_base + 1


def ON_CLICK(x, y, button, pressed): # Record mouse click and call for clicking function
    if pressed:
        CLICKING()


def ACTION(): 

    global action

    functions.clear()
    STATS()

    while True:

        action = input(PROMPT)

        functions.clear()

        STATS()

        if action.lower().strip() == "Upgrade".lower().strip():

            print("\nCost;", 25 + click_base)
            choice = str(input("\nUpgrade? (Y/N) : "))

            if choice.lower().strip() == "Y".lower():

                if MONEY_CHECK(25) == True: # Money check and upgrading
                    UPGRADE(25)
                    print("\nUpgraded")
                    time.sleep(0.5)
                    functions.clear()
                    STATS()

                else:     
                    print("\nNot enough money")

            elif choice.lower().strip() == "N".lower():
                print("\nUpgrade aborted")

a = threading.Thread(target=ACTION, daemon=True).start() # Threading action text

with mouse.Listener(on_click = ON_CLICK) as listener: # Listening for clicks
    listener.join()