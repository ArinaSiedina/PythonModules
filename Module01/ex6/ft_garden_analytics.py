class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self._age = age
        self._stats = self.Statistics()

    def grow(self, amount: float) -> None:
        self.height += amount
        self._stats.record_grow()

    def age(self, days: int) -> None:
        self._age += days
        self._stats.record_age()

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def show_statistics(self) -> None:
        self._stats.display()

    @staticmethod
    def is_older_than_year(age: int) -> None:
        print(f"Is {age} days more than a year? -> {age > 365}")

    @classmethod
    def create_anonymous(cls) -> Plant:
        return cls("Unknown plant", 0, 0)

    class Statistics:
        def __init__(self):
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0

        def record_grow(self) -> None:
            self.__grow_calls += 1

        def record_age(self) -> None:
            self.__age_calls += 1

        def record_show(self) -> None:
            self.__show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self.__grow_calls} grow",
                f"{self.__age_calls} age",
                f"{self.__show_calls} show",
                sep=", ",
            )


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        self.has_bloomed = False
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        self.has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.has_bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_count = 0

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f} cm")

    def produce_shade(self):
        self._stats.record_shade()
        print(
            f"Tree Oak now produces a shade of {self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    class Statistics(Plant.Statistics):
        def __init__(self):
            super().__init__()
            self.__shade_calls = 0

        def record_shade(self) -> None:
            self.__shade_calls += 1

        def display(self):
            super().display()
            print(f" {self.__shade_calls} shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days_old: int, harvest_season: str):
        super().__init__(name, height, days_old)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0
        self.growth_rate = 2.1

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def age(self) -> None:
        self.set_age(self._age + 1)
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value:g}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self._seeds = 0

    def set_seeds(self, amount: int) -> None:
        if self.has_bloomed and amount >= 0:
            self._seeds += amount

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def show_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===", "=== Check year-old", sep="\n")
    Plant.is_older_than_year(30)
    Plant.is_older_than_year(400)
    print()

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    rose._stats.display()
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    rose._stats.display()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    print("[statistics for Oak]")
    oak._stats.display()
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.set_seeds(42)
    sunflower.show()
    show_plant_statistics(sunflower)
    print()

    print("=== Anonymous")
    anonymous_plant = Plant.create_anonymous()
    anonymous_plant.show()
    show_plant_statistics(anonymous_plant)
