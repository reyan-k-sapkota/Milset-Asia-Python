from pandas import *
import numpy as np
import matplotlib.pyplot as plt


df_cnt = read_excel('Analysis/AllExcel/G+10CNTDrift.xlsx')
df_conc = read_excel ('Analysis/AllExcel/G+10CONCDrift.xlsx')
model = "G+3"

def graph_storydisplX(df_cnt, df_conc, model):

    choice_file = "StoryDisplacement"
    
    dfcnt_dataX = df_cnt['X-Dir(cnt)']
    dfconc_dataX = df_conc['X-Dir(conc)']
    
    story = df_cnt['Story(cnt)']
    
    storey_value = story.values.tolist()
    storey_len = len(storey_value)
    
    
    
    font1 = {'family':'serif','color':'blue','size':18}
    font2 = {'family':'serif','color':'darkred','size':15}
    font3 = {'family':'serif','color':'darkred','size':15}
    
    model_name = f'{model}'
    choice_file_name = f'{choice_file}'
    
    j = 0
    b = []
    
    plt.figure() 
    plt.plot (storey_value, dfcnt_dataX, marker = 'o', label="CNT")
    plt.plot(storey_value, dfconc_dataX, marker = 'o', label = "Concrete")
    plt.title(f'{choice_file_name} in X-Direction for ({model_name})', fontdict=font1)
    plt.xlabel("Story", fontdict= font2)
    plt.ylabel(f' {choice_file_name} in X-direction (mm)', fontdict = font3)
    plt.grid()
    plt.xticks(range(0, storey_len))
    #plt.yticks(b)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(f'Analysis/GraphComparison/graph{model_name}{choice_file_name}XDir.png', dpi = 300)


def graph_storydisplY(df_cnt, df_conc, model):

    choice_file = "StoryDisplacement"
    
    dfcnt_dataY = df_cnt['Y-Dir(cnt)']
    dfconc_dataY = df_conc['Y-Dir(conc)']
    
    
    story = df_cnt['Story(cnt)']
    
    storey_value = story.values.tolist()
    storey_len = len(storey_value)
    
    
    font1 = {'family':'serif','color':'blue','size':18}
    font2 = {'family':'serif','color':'darkred','size':15}
    font3 = {'family':'serif','color':'darkred','size':15}
    
    model_name = f'{model}'
    choice_file_name = f'{choice_file}'
    
    
    plt.figure() 
    plt.plot (storey_value, dfcnt_dataY, marker = 'o', label="CNT")
    plt.plot(storey_value, dfconc_dataY, marker = 'o', label = "Concrete")
    plt.title(f'{choice_file_name} in Y-Direction for ({model_name})', fontdict=font1)
    plt.xlabel("Story", fontdict= font2)
    plt.ylabel(f' {choice_file_name} in Y-direction (mm)', fontdict = font3)
    plt.grid()
    plt.xticks(range(0, storey_len))
    #plt.yticks(b)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(f'Analysis/GraphComparison/graph{model_name}{choice_file_name}YDir.png', dpi = 300)


def graph_storydriftX(df_cnt, df_conc, model):

    choice_file = "StoryDrift"
    
    dfcnt_dataX = df_cnt['X-Dir(cnt)']
    dfconc_dataX = df_conc['X-Dir(conc)']
    
    
    story = df_cnt['Story(cnt)']
    
    storey_value = story.values.tolist()
    storey_len = len(storey_value)
    
    
    font1 = {'family':'serif','color':'blue','size':18}
    font2 = {'family':'serif','color':'darkred','size':15}
    font3 = {'family':'serif','color':'darkred','size':15}
    
    model_name = f'{model}'
    choice_file_name = f'{choice_file}'
    
    
    plt.figure() 
    plt.plot (storey_value, dfcnt_dataX, marker = 'o', label="CNT")
    plt.plot(storey_value, dfconc_dataX, marker = 'o', label = "Concrete")
    plt.title(f'{choice_file_name} in X-Direction for ({model_name})', fontdict=font1)
    plt.xlabel("Story", fontdict= font2)
    plt.ylabel(f' {choice_file_name} in X-direction (unitless)', fontdict = font3)
    plt.grid()
    plt.xticks(range(0, storey_len))
    #plt.yticks(b)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(f'Analysis/GraphComparison/graph{model_name}{choice_file_name}XDir.png', dpi = 300)



def graph_storydriftY(df_cnt, df_conc, model):

    choice_file = "StoryDrift"
    
    dfcnt_dataY = df_cnt['Y-Dir(cnt)']
    dfconc_dataY = df_conc['Y-Dir(conc)']
    
    
    story = df_cnt['Story(cnt)']
    
    storey_value = story.values.tolist()
    storey_len = len(storey_value)
    
    
    font1 = {'family':'serif','color':'blue','size':18}
    font2 = {'family':'serif','color':'darkred','size':15}
    font3 = {'family':'serif','color':'darkred','size':15}
    
    model_name = f'{model}'
    choice_file_name = f'{choice_file}'
    
    
    plt.figure() 
    plt.plot (storey_value, dfcnt_dataY, marker = 'o', label="CNT")
    plt.plot(storey_value, dfconc_dataY, marker = 'o', label = "Concrete")
    plt.title(f'{choice_file_name} in Y-Direction for ({model_name})', fontdict=font1)
    plt.xlabel("Story", fontdict= font2)
    plt.ylabel(f' {choice_file_name} in Y-direction (unitless)', fontdict = font3)
    plt.grid()
    plt.xticks(range(0, storey_len))
    #plt.yticks(b)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(f'Analysis/GraphComparison/graph{model_name}{choice_file_name}YDir.png', dpi = 300)



def graph_storystiffnessX(df_cnt, df_conc, model):

    choice_file = "StoryStiffness"
    
    dfcnt_dataX = df_cnt['X-Dir(cnt)']
    dfconc_dataX = df_conc['X-Dir(conc)']
    
    
    story = df_cnt['Story(cnt)']
    
    storey_value = story.values.tolist()
    storey_len = len(storey_value)
    
    
    font1 = {'family':'serif','color':'blue','size':18}
    font2 = {'family':'serif','color':'darkred','size':15}
    font3 = {'family':'serif','color':'darkred','size':15}
    
    model_name = f'{model}'
    choice_file_name = f'{choice_file}'
    
    
    plt.figure() 
    plt.plot (storey_value, dfcnt_dataX, marker = 'o', label="CNT")
    plt.plot(storey_value, dfconc_dataX, marker = 'o', label = "Concrete")
    plt.title(f'{choice_file_name} in X-Direction for ({model_name})', fontdict=font1)
    plt.xlabel("Story", fontdict= font2)
    plt.ylabel(f' {choice_file_name} in X-direction (kN/m)', fontdict = font3)
    plt.grid()
    plt.xticks(range(0, storey_len))
    #plt.yticks(b)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(f'Analysis/GraphComparison/graph{model_name}{choice_file_name}XDir.png', dpi = 300)



def graph_storystifnessY(df_cnt, df_conc, model):

    choice_file = "StoryStiffness"
    
    dfcnt_dataY = df_cnt['Y-Dir(cnt)']
    dfconc_dataY = df_conc['Y-Dir(conc)']
    
    
    story = df_cnt['Story(cnt)']
    
    storey_value = story.values.tolist()
    storey_len = len(storey_value)
    
    
    font1 = {'family':'serif','color':'blue','size':18}
    font2 = {'family':'serif','color':'darkred','size':15}
    font3 = {'family':'serif','color':'darkred','size':15}
    
    model_name = f'{model}'
    choice_file_name = f'{choice_file}'
    
    
    plt.figure() 
    plt.plot (storey_value, dfcnt_dataY, marker = 'o', label="CNT")
    plt.plot(storey_value, dfconc_dataY, marker = 'o', label = "Concrete")
    plt.title(f'{choice_file_name} in Y-Direction for ({model_name})', fontdict=font1)
    plt.xlabel("Story", fontdict= font2)
    plt.ylabel(f' {choice_file_name} in Y-direction (kN/m)', fontdict = font3)
    plt.grid()
    plt.xticks(range(0, storey_len))
    #plt.yticks(b)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(f'Analysis/GraphComparison/graph{model_name}{choice_file_name}YDir.png', dpi = 300)
