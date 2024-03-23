import csv

csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',')
    print(f'Column header: {headers}')
    reader = csv.reader(csv_file)
    for row in reader:
        # for index, value in enumerate(row):
        #     if value.isnumeric():
        #         row[index] = int(value)
        print(row)