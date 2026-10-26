import requests
from bs4 import BeautifulSoup
from functions import clear
import time

while True: 
    try:
        page = int(input("\nEnter page : "))
        if 1 <= page <= 10:
            break
        print("Error: Choose a page number between 1 and 10")
    except ValueError:
        print("ValueError: Enter a number")

response = requests.get(f"https://quotes.toscrape.com/page/{page}/")
soup = BeautifulSoup(response.text, "html.parser")

for tag in soup.find_all("small", class_="author"):
    print("\n",tag.text)

author_name = input("\nEnter author (First & Last Name) : ").strip()

clear()

found = False

for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    if author_name.lower() == author.lower():
    
        print("\n" + text)
        print("\n—", author)
        print()
        found = True

if not found:
    print("\nAuthor not found, try again")
    time.sleep(2)
    exit()

input("\nPress enter to exit...")