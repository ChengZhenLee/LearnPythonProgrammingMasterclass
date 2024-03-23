import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    # sample = countries_data.read()
    sample = ""
    # Reads a small 'sample' of the file
    for line in range(3):
        sample += countries_data.readline()
    # Gets the dialect of the file (determine delimiters of the csv etc)
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    countries_data.seek(0)  # Moves the reader pointer back to the start
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print('*' * 80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]

# repr: shows special string characters
# getattr: gets the attributes of the object
for attribute in attributes:
    print(f'{attribute}: {repr(getattr(country_dialect, attribute))}')
