input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline() # Skip the first line
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t)
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        # code_lookup[code.casefold()] = country
        countries[code.casefold()] = country_dict

# print(countries)

while True:
    chosen_country = input("Please enter a country name: ")
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        if not country_data['capital']:
            print("This country has no capital")
        else:
            print(f"The capital of {chosen_country} is {country_data['capital']}.")
    elif country_key == 'quit':
        break
    else:
        print("That's not a valid country.")

for country, data in countries.items():
    for field_name, value in data.items():
        if not value:
            print(country, field_name)