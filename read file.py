import csv
from functools import reduce
path_csv = 'data (1).csv'

with open(path_csv, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)


header_index = None
for i, row in enumerate(rows):
    if row and row[1] and row[1].startswith('1994'):
        header_index = i
        break

data = rows[header_index:]
def bring_the_ribit_now(start_date, end_date):
    filtered_data = []
    for row in data:
        date = row[1]
        if start_date <= date <= end_date:
            filtered_row = list(filter(lambda cell: cell.strip(), row))
            if filtered_row:

                filtered_data.append(filtered_row)
    my_dict =convert_data_to_dict(filtered_data,start_date,end_date)
    return my_dict
def convert_data_to_dict(arr,start,end):
    my_dict = {}
    my_dict["start"] = start
    my_dict["end"] = end

    min_value = reduce(lambda x, y: x if x[1] < y[1] else y, arr)
    my_dict["min"] = min_value[1]

    max_value = reduce(lambda x, y: x if x[1] > y[1] else y, arr)
    my_dict["max"] = max_value[1]
    count = 0
    for row in arr:
        count += float(row[1])

    my_dict["avg"] =(count / len(arr))
    return my_dict

start_date = '2022-06'
end_date = '2024-05'

print(bring_the_ribit_now(start_date, end_date))
