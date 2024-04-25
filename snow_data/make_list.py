import csv

csv_file = "C:/Users/yjwon-test/Desktop/2024/Python_2024/asos/snow_data"


def col_value(csv_file, col_nm):
    stn_val = []

    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        headers = next(reader)

        if col_nm not in headers:
            print(f"does not exist {col_nm}.")
            return stn_val

        col_index = headers.index(col_nm)

        for row in reader:
            value = row[col_index].strip()
            stn_val.append(value)

    return stn_val


def merge_id_col(col1_values, col4_values):
    merged_id_values = col1_values + col4_values[:-5]
    return merged_id_values


def merge_nm_col(col2_values, col5_values):
    merged_nm_values = col2_values + col5_values[:-5]
    return merged_nm_values


col1_values = col_value(csv_file, "지점1")
col2_values = col_value(csv_file, "지점명1")
col4_values = col_value(csv_file, "지점2")
col5_values = col_value(csv_file, "지점명2")

merged_id_values = merge_id_col(col1_values, col4_values)
merged_nm_values = merge_nm_col(col2_values, col5_values)

merged_data = zip(merged_id_values, merged_nm_values)
