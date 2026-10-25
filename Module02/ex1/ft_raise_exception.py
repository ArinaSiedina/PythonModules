
class TemperatureError(Exception):
    pass

def input_temperature(temp_str: str) -> int:
    temperature =  int(temp_str)
    if (temperature < 0 ):
        raise TemperatureError (f"{temperature:g}°C is too cold for plants (min 0°C)")
    elif(temperature > 40):
        raise TemperatureError (f"{temperature:g}°C is too hot for plants (max 40°C)")
    return temperature

def test_temperature():
    print("=== Garden Temperature ===")

    for value in ("25", "abc","-50", "100"):
        print(f"Input data is '{value}'")
        try:
            temperature = input_temperature(value)
            print(f"Temperature is now {temperature}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
        except TemperatureError as temp_error:
             print(f"Caught input_temperature error: {temp_error}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
