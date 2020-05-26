import requests
from bs4 import BeautifulSoup

choice = input("Hello! Would you like to know the current temperature? ")

if (choice == "Yes"):
    country = input("What Country? ")
    state = input("Province/State? ")
    city = input("City? ")

    url = "https://www.geodatos.net/en/coordinates/"+country+"/"+state+"/"+city
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    coordLinks = soup.find_all('div', attrs={"class": "col-md-12 fcenter"})
    coordinates = coordLinks[0].find('strong').text
    splitWords = coordinates.split()
    latitude = splitWords[0]
    longitude = splitWords[1]

    result = requests.get("https://weather.com/en-CA/weather/today/l/"+latitude+longitude)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    mainLinks = soup.find_all('div', attrs={"class": "today_nowcard-section today_nowcard-condition"})

    temp = mainLinks[0].find('span').text
    print(f"The temperature right now in "+city+" is "+ temp +" Celcius!")
    feel = mainLinks[0].find_all('span')[2].text
    print("It feels like", feel)
    high = mainLinks[0].find_all('span')[4].text
    print("Today's High is", high)
    low = mainLinks[0].find_all('span')[8].text
    print("Today's Low is", low)
    uvIndex = mainLinks[0].find_all('span')[11].text
    print("Today's UV index is", uvIndex)

    sideLinks = soup.find_all('div', attrs={"class": "today_nowcard-sidecar component panel"})

    wind = sideLinks[0].find_all('span')[0].text
    direction, strength, unit = wind.split()
    print(f"Right now, the wind is at a speed of "+ strength + unit+ " in the "+direction+" direction")
    humidity = sideLinks[0].find_all('span')[1].text
    print(f"Right now, it is "+humidity+" humidity")
    dewPoint = sideLinks[0].find_all('span')[4].text
    print("Right now, the dewPoint is", dewPoint)
    pressure = sideLinks[0].find_all('span')[5].text
    print("Right now, there is a pressure of", pressure)
    visibility = sideLinks[0].find_all('span')[7].text #sometimes it works at index 7 and sometimes 6
    print("Right now, the visibility is a distance of", visibility)

else:
    print("Ok...")