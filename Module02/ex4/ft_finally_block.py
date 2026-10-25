
class PlantError(Exception):
    pass

def water_plant(plant_name: str) -> None:
    if plant_name and plant_name[0].isupper():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: tuple[str, ...]) -> None:
    print("Opening watering system")

    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")

    print("Testing valid plants...")
    test_watering_system(("Tomato", "Lettuce", "Carrots"))

    print("Testing invalid plants...")
    test_watering_system(("Tomato", "lettuce", "Carrots"))

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
