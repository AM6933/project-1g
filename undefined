while (true) {
    console.log("Temperature (F): " + input.temperature(TemperatureUnit.Fahrenheit))
    if (input.temperature(TemperatureUnit.Fahrenheit) > 170) {
        light.setAll(light.rgb(255, 0, 0))
    } else if (input.temperature(TemperatureUnit.Fahrenheit) < 150) {
        light.setAll(light.rgb(0, 0, 255))
    } else {
        light.setAll(light.rgb(255, 255, 0))
    }
    
}
