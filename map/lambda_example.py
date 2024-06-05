from medals_data import medals_table

# def sort_key(d: dict, field: str) -> str:
#     return d[field]

def sort_key(d:dict) -> str:
    return d['country']

# sort_key will return the country names of the dictionary
medals_table.sort(key=sort_key)
print(medals_table)