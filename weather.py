import tkinter as tk
import requests
import time

def getweather(event=None):  # Accept event from bind
    city = textfield.get()
    api = f"http://api.weatherapi.com/v1/current.json?key=ad3a040492cf4eef860121635250408&q={city}&aqi=no"

    try:
        json_data = requests.get(api).json()

        condition = json_data['current']['condition']['text']
        region = json_data['location']['region']
        country = json_data['location']['country']
        latitude = json_data['location']['lat']
        longitude = json_data['location']['lon']
        timezone = json_data['location']['tz_id']
        localtime= json_data['location']['localtime']
        temp_c = json_data['current']['temp_c']
        temp_f =json_data['current']['temp_f']
        pressure = json_data['current']['pressure_mb']
        humidity = json_data['current']['humidity']
        wind = json_data['current']['wind_kph']

        final_info = f"{condition}\n{temp_c}°C"
        final_data = (
            f"\nRegion: {region}"
            f"\nCountry: {country}"
            f"\nLatitude: {latitude}"
            f"\nLongitude: {longitude}"
            f"\nTimeZone: {timezone}"
            f"\nLocal Time: {localtime}"
            f"\nTemp_c: {temp_c} C"
            f"\nTemp_f:{temp_f} F"
            f"\nPressure: {pressure} mb"
            f"\nHumidity: {humidity}%"
            f"\nWind Speed: {wind} kph"
        )

        label1.config(text=final_info)
        label2.config(text=final_data)

    except Exception as e:
        label1.config(text="Error fetching data")
        label2.config(text=str(e))


# API Key (your key)
api_key = 'ad3a040492cf4eef860121635250408'

# GUI
canvas = tk.Tk()
canvas.geometry("600x600")
canvas.title("Weather Application")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getweather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
