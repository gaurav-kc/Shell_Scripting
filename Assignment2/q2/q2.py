import requests
import datetime
import os

Payload = {"APPID":"13c533755c6d8fcaad6aeb927075068a", "q":"Hyderabad, in" }
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params = Payload)
weather = response.json()
weathertype = weather["weather"][0]["main"]
print "Weather is: ", weathertype
now = datetime.datetime.now()
hour = now.hour
print "Hour ", hour
if weathertype == "Thunderstorm":
    wallpaper = "/wallpaper/thunderstorm.jpg"

elif weathertype == "Drizzle":
    if 6 <= hour and hour <= 18:
        wallpaper = "/wallpaper/drizzleDay.jpg"
    else:
        wallpaper = "/wallpaper/drizzleNight.jpg"

elif weathertype == "Rain":
    if 6 <= hour and hour <= 18:
        wallpaper = "/wallpaper/rainDay.jpg"
    else:
        wallpaper = "/wallpaper/rainNight.jpg"

elif weathertype == "Snow":
    if 6 <= hour and hour <= 18:
        wallpaper = "/wallpaper/snowDay.jpg"
    else:
        wallpaper = "/wallpaper/snowNight.jpg"

elif weathertype == "Clear":
    if 6 <= hour and hour <= 18:
        wallpaper = "/wallpaper/clearDay.jpg"
    else:
        wallpaper = "/wallpaper/clearNight.jpg"

elif weathertype == "Clouds":
    if 6 <= hour and hour <= 18:
        wallpaper = "/wallpaper/cloudsDay.jpg"
    else:
        wallpaper = "/wallpaper/cloudsNight.jpg"

elif weathertype == "Mist":
    if 6 <= hour and hour <= 18:
        wallpaper = "/wallpaper/mistDay.jpg"
    else:
        wallpaper = "/wallpaper/mistNight.jpg"

elif weathertype == "Haze":
    if 6 <= hour and hour <= 18:
        wallpaper = "/wallpaper/hazeDay.jpg"
    else:
        wallpaper = "/wallpaper/hazeNight.jpg"
currentDir = os.getcwd()
changeWallpaperCommand = "gsettings set org.gnome.desktop.background picture-uri " + currentDir + wallpaper
os.system(changeWallpaperCommand)
