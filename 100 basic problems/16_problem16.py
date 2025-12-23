# Write a program that will determine weather when the value of temperature and humidity is provided by the user.
"""
TEMPERATURE(C)            HUMIDITY(%)      WEATHER

      >= 30                >=90            Hot and Humid
      >= 30                < 90             Hot
      <30                   >= 90           Cool and Humid
      <30                    <90             Cool

"""

temperature = float(input("Enter temperature : "))
humidity = float(input("Enter humidity : "))


if temperature >= 30 :
    if  humidity >= 90 :
        weather = "Hot and Humid"
    else:
        weather = "Hot"
else:
    if humidity >= 90 :
        weather = "Cool and Humid"
    else:
        weather = "Cool"

print(f"Temperature : {temperature}")
print(f"Humidity : {humidity}")
print(f"Weather : {weather}")