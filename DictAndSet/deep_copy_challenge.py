from contents import recipes

def deep_copy(data: dict) -> dict:
    """
    Copy a dictionary, creating copies of the `list`
    or `dict` values.

    Arguments:
        data -- The dictionary to copy.
    
    Return:
        A copy of `data`, with the values being copies of
        the original values.
    """
    new_data = {}
    for key, value in data.items():
        new_data[key] = value.copy()

    return new_data


recipes_copy = deep_copy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])