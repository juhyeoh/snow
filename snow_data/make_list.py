from docx import Document

docx_file = 'snow_data/stnIds_list.docx'

def col_value(docx_file, col_nm):
    doc = Document(docx_file)
    stn_val = []

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if cell.text.strip() == col_nm:
                    index = row.cells.index(cell)
                    for row in table.rows:
                        value = row.cells[index].text.strip()
                        stn_val.append(value)
                    print(stn_val)
                    return stn_val
                
def merge_col(col1_values, col4_values):
    if col1_values and col4_values:
        col1_values[-1] += " " + col4_values[0]
    return col1_values

col1_values = col_value(docx_file, 'col1')
col4_values = col_value(docx_file, 'col4')

merged_values = merge_col(col1_values, col4_values)
print(merged_values)