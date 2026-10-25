import sys


def create_inventory(arguments: list[str]) -> dict[str, int]:
    inventory = {}

    for argument in arguments:
        parts = argument.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{argument}'")
            continue

        key, value = parts

        try:
            number = int(value)
        except ValueError as error:
            print(f"Quantity error for '{key}': {error}")
            continue

        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue

        inventory[key] = number

    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = create_inventory(sys.argv[1:])
    if inventory:
        print(f"Got inventory: {inventory}")
        print(f"Item list: {inventory.keys}")
        print(f"Item list: {inventory.keys}")
        items_count = sum(inventory.values)
        print(f"Total quantity of the {len(inventory.keys)} items: {items_count}")
        percent = lambda number: number / items_count * 100
        for key, value in inventory:
            print(f"Item {key} represents {percent(value)}")

        biggest = max(inventory.items(), key=lambda pair: pair[1])
        print(f"Item most abundant: {biggest.key} with quantity {biggest.value}")

        smallest = min(inventory.items(), key=lambda pair: pair[1])
        print(f"Item most abundant: {smallest.key} with quantity {smallest.value}")

        inventory.update("'magic_item", 1)
        print(f"Updated inventory: {inventory}")
    else:
        print("Inventory is empty, my Lord")
