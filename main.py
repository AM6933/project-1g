while True:
    print("Temperature (F): " + input.temperature(TemperatureUnit.FAHRENHEIT))
    if input.temperature(TemperatureUnit.FAHRENHEIT) > 170:
        light.set_all (light.rgb(255, 0, 0))
    elif input.temperature(TemperatureUnit.FAHRENHEIT) < 150:
        light.set_all (light.rgb(0, 0, 255))
    else:
        light.set_all (light.rgb (255,255,0))