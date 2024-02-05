import csv

csv_file = 'snow_data/stnIds_list.csv'

def col_value(csv_file, col_nm):
    stn_val = []

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames

        if col_nm not in headers:
            print(f"does not exist {col_nm}.")
            return stn_val

        for row in reader:
            value = row[col_nm].strip()
            stn_val.append(value)

    return stn_val

def merge_col(col1_values, col4_values):
    if col1_values and col4_values:
        col1_values[-1] += " " + col4_values[0]
    return col1_values

col1_values = col_value(csv_file, '지점1')
col4_values = col_value(csv_file, '지점2')

merged_values = merge_col(col1_values, col4_values)
print(merged_values)
