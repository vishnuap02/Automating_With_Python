# this program takes names from one excel file and searches it in another , if found it will write
# that row into another new excel file.

# import module to operate .xlsx file
import xlrd

loc1 = input("Enter path of file to GET column values: ")
loc2 = input("Enter path of file to SEARCH values: ")

# To open Workbook
wb1 = xlrd.open_workbook(loc1)
wb2 = xlrd.open_workbook(loc2)

k = int(input("Enter sheet number to operate"))
sheet = wb1.sheet_by_index(k)

j = int(input("Enter column index to extract info : "))

rowValues = []
for i in range(sheet.nrows):
    rowValues.append(sheet.cell_value(i, j))

k = int(input("Enter sheet number to search"))
sheet = wb2.sheet_by_index(k)

j = int(input("Enter column index to Search info : "))

finalRows=[]
for i in rowValues:
    for x in range(sheet.nrows):
        if sheet.cell_value(x,j) in i:
            finalRows.append(sheet.row_values(x, j))

print(finalRows)



