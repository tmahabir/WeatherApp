import requests
from bs4 import BeautifulSoup

choice = input("Hello! Would you like to know the current temperature? ")

if (choice == "Yes"):
    location = input("Where? ")
    if (location == "San Francisco"):
        result = requests.get(
            "https://weather.com/en-IN/weather/today/l/69bedc6a5b6e977993fb3e5344e3c06d8bc36a1fb6754c3ddfb5310a3c6d6c87")
    else:
        result = requests.get("https://weather.com/en-IN/weather/today/l/CAON1288:1:CA")

    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    mainLinks = soup.find_all('div', attrs={"class": "today_nowcard-section today_nowcard-condition"})

    temp = mainLinks[0].find('span').text
    print(f"The temperature right now in "+location+" is "+ temp +" Celcius!")
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
    visibility = sideLinks[0].find_all('span')[7].text
    print("Right now, the visibility is a distance of", visibility)


else:
    print("Ok...")
#result = requests.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")
#result = requests.get("https://www.theweathernetwork.com/ca/weather/ontario/clarington")
#result = requests.get("https://weather.com/en-IN/weather/tenday/l/INKA0344:1:IN")
result = requests.get("https://weather.com/en-IN/weather/today/l/CAON1288:1:CA")
result = requests.get("https://weather.com/en-IN/weather/today/l/af60f113ba123ce93774fed531be2e1e51a1666be5d6012f129cfa27bae1ee6c")
#result = requests.get("https://www.google.com/search?q=weather&oq=weather&aqs=chrome.0.69i59j0l2j69i60l5.1618j0j7&sourceid=chrome&ie=UTF-8")

#src = result.content
#soup = BeautifulSoup(src, 'lxml')


#links = soup.find_all('div', attrs = {'id': 'main-content'})
#links = soup.find_all("a", href=True, attrs = {'class':'_31qSD5'})
#links = soup.find_all('div', attrs = {'class':'detailed-metrics'})
#links = soup.find_all('td', attrs = {"class":"temp"})
#links = soup.find_all('div', attrs = {"class":"today_nowcard-section today_nowcard-condition"})
#<a href="/weather/CAON0142" class="citylink" data-event-action="clicks" data-event-label="currentWeather"><div class="current-location-city">Clarington, ON</div><div class="current-location-wrapper clearfix"><div class="lbl_current_weather">Current Weather</div><div class="current-location-temperature"><div class="current-location-icon"><img src="//s1.twnmm.com/images/en_ca/icons/wxicons_medium/1.png" class="weather-icon"></div><div class="current-location-current-temp-c">24<div class="current-location-current-temp-unit">°C</div></div><div class="current-location-current-temp-f" style="display: none;">75<div class="current-location-current-temp-unit">°F</div></div></div><div class="view-current-forecast">View Forecast &gt;&gt;</div></div></a>
#<a class="_31qSD5" target="_blank" rel="noopener noreferrer" href="/lenovo-ideapad-core-i5-7th-gen-8-gb-1-tb-hdd-windows-10-home-2-gb-graphics-ip-320-15ikb-laptop/p/itmf3s3fzedndvna?pid=COMEW6QPC5HDQAFK&amp;lid=LSTCOMEW6QPC5HDQAFKMTENRZ&amp;marketplace=FLIPKART&amp;srno=b_1_2&amp;otracker=browse&amp;fm=organic&amp;iid=6a0e5c1f-4c79-4b62-b007-f30132119941.COMEW6QPC5HDQAFK.SEARCH&amp;ssid=2pora2aro00000001590268765414"><div class="_3SQWE6"><div class="_1OCn9C"><div style="-webkit-filter:grayscale(1);-moz-filter:grayscale(1);-o-filter:grayscale(1);-ms-filter:grayscale(1);filter:grayscale(1);opacity:0.6"><div class="_3BTv9X" style="height:200px;width:200px"><img class="_1Nyybr _30XEf0" alt="Lenovo Ideapad Core i5 7th Gen - (8 GB/1 TB HDD/Windows 10 Home/2 GB Graphics) IP 320-15IKB Laptop" src="https://rukminim1.flixcart.com/image/312/312/jhf5pjk0/computer/a/f/k/lenovo-ip-320-laptop-original-imaf49pfduqmxqsf.jpeg?q=70"></div></div><div class="_3aV9Tq"><span class="_1GJ2ZM">Not Deliverable</span></div></div><div class="_2lesQu"><div class="_1O_CiZ"><span class="_1iHA1p"><div class="_2kFyHg"><label><input type="checkbox" class="_3uUUD5" readonly="" value="on"><div class="_1p7h2j"></div></label></div></span><label class="_10TB-Q"><span>Add to Compare</span></label></div></div><div class="_3gDSOa _32A6AP"><div class="DsQ2eg"><svg xmlns="http://www.w3.org/2000/svg" class="_2oLiqr" width="16" height="16" viewBox="0 0 20 16"><path d="M8.695 16.682C4.06 12.382 1 9.536 1 6.065 1 3.219 3.178 1 5.95 1c1.566 0 3.069.746 4.05 1.915C10.981 1.745 12.484 1 14.05 1 16.822 1 19 3.22 19 6.065c0 3.471-3.06 6.316-7.695 10.617L10 17.897l-1.305-1.215z" fill="#2874F0" class="_35Y7Yo" stroke="#FFF" fill-rule="evenodd" opacity=".9"></path></svg></div></div></div><div class="_1-2Iqu row"><div class="col col-7-12"><div class="_3wU53n">Lenovo Ideapad Core i5 7th Gen - (8 GB/1 TB HDD/Windows 10 Home/2 GB Graphics) IP 320-15IKB Laptop</div><div class="niH0FQ"><span id="productRating_LSTCOMEW6QPC5HDQAFKMTENRZ_COMEW6QPC5HDQAFK_" class="_2_KrJI"><div class="hGSR34">4.3<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==" class="_2lQ_WZ"></div></span><span class="_38sUEc"><span><span>13,176 Ratings&nbsp;</span><span class="_1VpSqZ">&amp;</span><span>&nbsp;2,613 Reviews</span></span></span></div><div class="_3ULzGw"><ul class="vFw0gD"><li class="tVe95H">Pre-installed Genuine Windows 10 Operating System (Includes Built-in Security, Free Automated Updates, Latest Features)</li><li class="tVe95H">Intel Core i5 Processor (7th Gen)</li><li class="tVe95H">8 GB DDR4 RAM</li><li class="tVe95H">64 bit Windows 10 Operating System</li><li class="tVe95H">1 TB HDD</li><li class="tVe95H">39.62 cm (15.6 inch) Display</li><li class="tVe95H">1 Year Onsite Warranty</li></ul></div></div><div class="col col-5-12 _2o7WAb"><div class="_6BWGkk"><div class="_1uv9Cb"><div class="_1vC4OE _2rQ-NK">₹51,990</div><div class="_3auQ3N _2GcJzG">₹<!-- -->53,745</div><div class="VGWI6T"><span>3% off</span></div></div></div><div class="_3n6o0t"><img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"></div><div class="_2nE8_R"><div class="_3_G5Wj" style="color:#000000;font-size:14px;font-family:inherit;font-weight:normal">No Cost EMI</div></div></div></div></a>

#<div class="current-location-current-temp-c">24<div class="current-location-current-temp-unit">°C</div></div>
#<div class="_3wU53n">Lenovo Ideapad Core i5 7th Gen - (8 GB/1 TB HDD/Windows 10 Home/2 GB Graphics) IP 320-15IKB Laptop</div>


#print(links[0].find('span').text)


#for link in links:
#    city = link.find('p')
#   for i in range(len(link.find_all("span"))-1):
#       temp = link.find_all('span')[i]
#        print(temp.text)
        #print(temp.text)
    #print(temp)
    #print(link.find('span', attrs={'class': 'value', 'style':'float: left;'}))
    #print(link.find('div', attrs = {'class': 'current-location-current-temp-c'}))
    #temp = link.find('div', attrs={'class':'current-location-current-temp-c'})
    #temp = link.find('div', attrs={'id': 'wob_loc'}).text
#print(city)

#print(temp.text)

#choice = input("Hello! Would you like to know the current temperature? ")

#if (choice == "Yes"):
    #print("The temperature right now is 22 degrees Celcius!")
#else:
#    print("Ok...")

###########result = requests.get("https://weather.com/en-IN/weather/tenday/l/INKA0344:1:IN")##############

#links = soup.find_all('td', attrs = {"class":"temp"})

#for link in links:
#    for i in range(len(link.find_all("span"))-1):
#        temp = link.find_all('span', attrs={'class': ''})[i]
#        if (i==1):
#            print("Low:" + temp.text)
#       else:
#            print("High:" + temp.text)


################result = requests.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")
#for link in links:
#    name = link.find('div', attrs={'class': '_3wU53n'})
 #   price = link.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
  #  rating = link.find('div', attrs={'class': 'hGSR34'})
#print(name.text)
#print(price.text)
#print(rating.text)