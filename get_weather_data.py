import requests
from bs4 import BeautifulSoup

url = 'https://penteli.meteo.gr/stations/heraclion/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_weather(url):
    try:

        html_text = requests.get(url ,headers=headers).text
        soup = BeautifulSoup(html_text, "html.parser")

        table = soup.find("div", class_="col_sub dist boxshadow realtime")
        lines = table.find_all("div", class_="line")

        data = {}

        for line in lines:
                key = line.find("div", class_="lleft").find("span").get_text(strip=True)
                value = line.find("div", class_="lright").find("span").get_text(strip=True)
                data[key] = value

    except Exception as e:
        print("error:",e)
        pass

    return data

data = get_weather(url)

temperature = float(data['Temperature'].split(' ')[0])
todays_rain = float(data["Today's Rain"].split(' ')[0])

print("################################################")
print(data)
print("################################################")

print(f"Temperature:{temperature}")
print(f"Today's Rain:{todays_rain}")