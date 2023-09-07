import openpyxl

wb = openpyxl.load_workbook("planilla.xlsx")

print(wb.sheetnames)
