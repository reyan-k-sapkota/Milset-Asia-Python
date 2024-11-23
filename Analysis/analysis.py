from pandas import *
import numpy as np
import matplotlib.pyplot as plt


def convert_graphX_Displ(df_cnt, df_conc, model, choice_file):

    dict_parameter = {
    1: "Story Displacement",
    2: "Story Drift",
    3: "Story Stiffness",
    }

    dfcnt_dataX = df_cnt['X-Dir(cnt)']
    dfconc_dataX = df_conc['X-Dir(conc)']
    dfcnt_dataY = df_cnt['Y-Dir(cnt)']
    dfconc_dataY = df_conc['Y-Dir(conc)']

    cx = len (dfcnt_dataX)
    i=0

    cy = len(dfcnt_dataY)
    j=0
    
    story = [10,9,8,7,6,5,4,3,2,1,0]
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    font3 = {'family':'serif','color':'darkred','size':15}
    
    model_name = f'{model}'
    choice_file_name = f'{choice_file}'

    j = 0
    b = []
    for i in range (0,15):
        b.append(0.025*i)
    
    plt.figure() 
    plt.plot (story, dfcnt_dataX, marker = 'o', label="CNT")
    plt.plot(story, dfconc_dataX, marker = 'o', label = "Concrete")
    plt.title(f'{choice_file_name} in X-Direction for ({model_name})', fontdict=font1)
    plt.xlabel("Story", fontdict= font2)
    plt.ylabel(f' {choice_file_name} in X-direction', fontdict = font3)
    plt.grid()
    plt.xticks(range(0, 11))
    plt.yticks(b)
    plt.legend(loc="lower right")
    plt.savefig(f'Analysis/GraphComparison/graph{model_name}{choice_file_name}XDir.png', dpi = 300)
    






