from pandas import *
from GraphsAll import graph_storydisplX
from GraphsAll import graph_storydisplY


df_cnt = read_excel('Analysis/AllExcel/G+10CNTDispl.xlsx')
df_conc = read_excel ('Analysis/AllExcel/G+10CONCDispl.xlsx')
model = "G+10"


graph_storydisplY(df_cnt, df_conc, model)
graph_storydisplX(df_cnt, df_conc, model)

