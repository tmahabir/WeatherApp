import requests
from bs4 import BeautifulSoup

choice = input("Hello! Would you like to know the current temperature? ").capitalize()

if (choice == "Yes"):

    decision = input("Would you like to enter the city's name (1) or coordinates (2)? ")

    if (decision == "1"):

        country = input("What Country? ").strip()
        undashedCountry = ""
        splits = country.split(" ")

        country =""
        for i in range(0, len(splits)):
            country += splits[i]
            undashedCountry += splits[i].capitalize()
            if (i != len(splits)-1):
                country += "-"
                undashedCountry += " "


        state = input("Province/State? ").strip()
        undashedState = ""
        splits = state.split(" ")


        state = ""
        for i in range(0, len(splits)):
            state += splits[i]
            undashedState += splits[i].capitalize()
            if (i != len(splits) - 1):
                state += "-"
                undashedState += " "
            else:
                undashedState += ","

        city = input("City? ").strip()
        undashedCity = ""
        splits = city.split(" ")

        city = ""
        for i in range(0, len(splits)):
            city += splits[i]
            undashedCity += splits[i].capitalize()
            if (i != len(splits) - 1):
                city += "-"
                undashedCity +=" "
            else:
                undashedCity += ","


        url = "https://www.geodatos.net/en/coordinates/"+country+"/"+state+"/"+city

        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        coordLinks = soup.find_all('div', attrs={"class": "col-md-12 fcenter"})
        coordinates = coordLinks[0].find('strong').text
        splitWords = coordinates.split()
        latitude = splitWords[0]
        longitude = splitWords[1]

        location = undashedCity + " " + undashedState + " " + undashedCountry

    else:
        latitude = input("What is the latitude of your wanted location? ").strip() + ","
        longitude = input("What is the longitude of your wanted location? ").strip()

        result = requests.get("https://weather.com/en-CA/weather/today/l/" + latitude + longitude)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        location = soup.find('span', attrs={"class": "today_nowcard-loc-title-wrqpper"}).find('h1').text

    result = requests.get("https://weather.com/en-CA/weather/today/l/" + latitude + longitude)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    mainLinks = soup.find_all('div', attrs={"class": "today_nowcard-section today_nowcard-condition"})

    print(f"\nThe Current Weather Statistics in " + location + " (" + latitude + " " + longitude + ") are...\n")
    temp = mainLinks[0].find('span').text
    print(f"The temperature right now is "+ temp +" Celcius!")
    feel = mainLinks[0].find_all('span')[2].text
    print("It feels like", feel)
    high = mainLinks[0].find_all('span')[4].text
    print("Today's High is", high)
    low = mainLinks[0].find_all('span')[8].text
    print("Today's Low is", low)
    uvIndex = mainLinks[0].find_all('span')[11].text
    print("Right now, the UV index is", uvIndex)

    sideLinks = soup.find_all('div', attrs={"class": "today_nowcard-sidecar component panel"})

    wind = sideLinks[0].find_all('span')[0].text
    if (len(wind.split()) == 3):
        direction, strength, unit = wind.split()
        print(f"Right now, the wind is at a speed of " + strength + unit + " in the " + direction + " direction")
    else:
        print(f"Right now, the wind is " + wind)

    humidity = sideLinks[0].find_all('span')[1].text
    print(f"Right now, it is "+humidity+" humidity")
    dewPoint = sideLinks[0].find_all('span')[4].text
    print("Right now, the dewPoint is", dewPoint)
    pressure = sideLinks[0].find_all('span')[5].text
    print("Right now, there is a pressure of", pressure)
    if (len(sideLinks[0].find_all('span')) == 7):
        visibility = sideLinks[0].find_all('span')[6].text #sometimes it works at index 7 and sometimes 6
    else:
        visibility = sideLinks[0].find_all('span')[7].text #if there is an arrow next to the pressure value on the website, then index 7 works
    print("Right now, the visibility is a distance of", visibility)

else:
    print("Ok...")