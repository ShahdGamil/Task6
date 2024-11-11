def celsius_to_kelvin(celsius):
    # Formula to convert Celsius to Kelvin
    return celsius +273.15
# Convert specific Celsius temperatures to Kelvin
print(celsius_to_kelvin(0))       # Output: 273.15 (freezing point of water)
print(celsius_to_kelvin(100))     # Output: 373.15 (boiling point of water)
print(celsius_to_kelvin(-273.15)) # Output: 0 (absolute zero)
print(celsius_to_kelvin(25.5))    # Output: 298.65 (room temperature)
print(celsius_to_kelvin(1000))    # Output: 1273.15 (high temperature example)