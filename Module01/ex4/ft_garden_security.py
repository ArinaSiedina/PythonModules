#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        self.growth_rate = 0.8

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age
    
    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self.height = round(self._height + self.growth_rate, 1)


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    print(
        f"Plant created: {plant.name}: "
        f"{plant.get_height():.1f}cm, {plant.get_age()} days old"
    )

    plant.set_height(25)
    print(f"Height updated: {plant.get_height():g}cm")

    plant.set_age(30)
    print(f"Age updated: {plant.get_age()} days")

    plant.set_height(-5)
    plant.set_age(-10)

    print(
        f"Current state: {plant.name}: "
        f"{plant.get_height():.1f}cm, {plant.get_age()} days old"
    )

    def show(self) -> None:
        print(
            f"{self.name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    plant.show()

    plant.set_height(25.0)
    plant.set_age(30)

    plant.set_height(-10.0)
    plant.set_age(-5)

    print("Current state: ", end="")
    plant.show()