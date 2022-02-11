import requests
from bs4 import BeautifulSoup
def horoscope(zodiac_sign: int, day: str) -> str:
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find("div", class_="main-horoscope").p.text
if __name__ == "__main__":
    print("Daily Horoscope. \n")
    print(
        "Input your Zodiac sign number:\n",
    
    )
    zodiac_sign = int(input("Input a number from said list: ").strip())
    print("Choose some day:\n", "yesterday\n", "today\n", "tomorrow\n")
    day = input("Input the day from said list: ")
    horoscope_text = horoscope(zodiac_sign, day)
    print(horoscope_text)