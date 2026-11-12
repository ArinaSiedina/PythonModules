import alchemy.transmutation as tm

from .. import potions


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{tm.create_air()}' "
        f"and '{potions.strength_potion()}' mixed with '{tm.create_fire()}'"
    )
