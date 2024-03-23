#Level 1 Task 2
def convert_temperature(scale, value):
    if scale == 'C':
        converted_value = (value * 1.8) + 32
        return converted_value
    elif scale == 'F':
        converted_value = (value - 32) / 1.8
        return converted_value
    else:
        return ValueError('Invalid temperature scale. Please enter either C for Celsius or F for Fahrenheit.')

value = float(input('Enter the temperature value: '))
scale = input('Enter the temperature scale (C for Celsius or F for Fahrenheit): ')
converted_value = convert_temperature(scale, value)
print(f'{value} {scale} is equivalent to {converted_value} {(scale.upper() == "C" and "F" or "C")}:')
