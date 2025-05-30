import openpyxl

def extract_excel_text(file):
    wb = openpyxl.load_workbook(file, data_only=True)
    text = ""
    for sheet in wb.worksheets:
        for row in sheet.iter_rows(values_only=True):
            for cell in row:
                if cell is not None:
                    text += f"{cell} "
    return text
