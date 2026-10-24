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
    garden: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Sunflower", 80.0, 45),
        Plant("Cactus", 15.0, 120),
        Plant("Tulip", 12.0, 20),
        Plant("Fern", 35.0, 60),
    ]

    print("=== Plant Factory Output===")
    for plant in garden:
        print("Created :", end="")
        plant.show()
    