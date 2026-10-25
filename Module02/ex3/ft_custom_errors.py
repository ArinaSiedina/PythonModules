class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant="Unknown plant"):
        super().__init__(f"The {plant} plant is wilting!")


class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    for error in (PlantError("tomato"), WaterError()):
        print(f"Testing {error.__class__.__name__}...")
        try:
            raise error
        except GardenError as e:
            match e:
                case PlantError():
                    print(f"Caught PlantError: {e}")
                case WaterError():
                    print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")

    for error in (PlantError("tomato"), WaterError()):
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")

if __name__ == "__main__":
    test_custom_errors()
