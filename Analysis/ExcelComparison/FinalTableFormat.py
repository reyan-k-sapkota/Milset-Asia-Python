from pandas import *
from TableFormat import TableFormatter



dict_model = {
    1:'G+3',
    2:'G+6',
    3:'G+10'
}

dict_typefile = {
    1:'Displ',
    2:'Drift',
    3:'Stiffness'
}

for i in range(1,4):
    for j in range (1, 4):
        model = dict_model[i]
        type_of_file = dict_typefile[j]
        excel_file = read_excel(f'Analysis/ExcelComparison/outputXY{model}{type_of_file}.xlsx')
        TableFormatter(excel_file, model, type_of_file)
        




