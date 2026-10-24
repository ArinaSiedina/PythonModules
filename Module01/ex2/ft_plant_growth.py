class Plant:
    name: str
    height: float
    days_old: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.days_old = age
        self.growth_rate = 0.8

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.days_old += 1


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)
    initial_height = plant.height

    print("=== Garden Plant Growth ===")
    plant.show()

    for day in range(1, 8):
        plant.grow()
        plant.age()

        print(f"=== Day {day} ===")
        plant.show()

    increase = round(plant.height - initial_height, 1)
    print(f"Growth this week: {increase:.1f}cm")
