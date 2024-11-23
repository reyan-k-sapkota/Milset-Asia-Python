from pandas import *
import numpy as np



def percentage_change_case_1(conc,cnt):
    diff = conc-cnt
    ratio = np.divide(diff, conc)
    return ratio * 100

def finaloutput_XY(df_cnt, df_conc, choice_value_file, model):

    dfcnt_dataX = df_cnt['X-Dir(cnt)']
    dfconc_dataX = df_conc['X-Dir(conc)']

    dfcnt_dataY = df_cnt['Y-Dir(cnt)']
    dfconc_dataY = df_conc['Y-Dir(conc)']

    new_merge = concat([df_conc, df_cnt], axis=1)

    new_dataX = {'Percentage_Change in X': []}
    df_changeX = DataFrame(new_dataX)
    
    new_dataY = {'Percentage_Change in Y': []}
    df_changeY = DataFrame(new_dataY)

    c = len (dfcnt_dataX) - 1
    cx = len (dfcnt_dataX)
    i=1

    cy = len(dfcnt_dataY)
    j=1

    while (i<=(cx-1)):
        a = percentage_change_case_1(dfconc_dataX[i], dfcnt_dataX[i])
        df_changeX.loc[i] = [a]
        i+=1

    while (j<=(cy-1)):
        b = percentage_change_case_1(dfconc_dataY[j], dfcnt_dataY[j])
        df_changeY.loc[j] = [b]
        j+=1


    final_merge_X = concat([new_merge, df_changeX], axis=1)
    final_merge_Y = concat([final_merge_X, df_changeY], axis=1)

    donwload_path = f'D:/Milset Asia Python/Analysis/ExcelComparison/outputXY{model}{choice_value_file}.xlsx'
    
    with ExcelWriter(donwload_path) as writer:
        final_merge_Y.to_excel(writer)



