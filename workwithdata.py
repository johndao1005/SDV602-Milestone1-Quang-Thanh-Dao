from openpyxl.workbook import Workbook
from openpyxl import load_workbook

#create a workbook from objects
#wb = Workbook()


#load exiting worksheet
wb = load_workbook('data.xlsx')

# create a active worksheet
ws = wb.active

#set a variable
name = ws['A2'].value
color = ws['B3'].value
column_a = ws['A']

for cell in column_a:
    print(f'{cell.value}\n')
#print something from spreadsheet
print(f'{name} {color}')