from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = dark_spell_allowed_ingredients()
    normalized_ingredients = ingredients.lower()

    for ingredient in allowed_ingredients:
        if ingredient in normalized_ingredients:
            return f"{ingredients}: VALID"

    return f"{ingredients}: INVALID"
