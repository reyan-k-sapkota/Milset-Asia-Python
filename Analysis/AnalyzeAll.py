from pandas import *
import numpy as np
from AnalysisXY import finaloutput_XY
from GraphsAll import graph_storydisplX
from GraphsAll import graph_storydisplY
from GraphsAll import graph_storydriftX
from GraphsAll import graph_storydriftY
from GraphsAll import graph_storystiffnessX
from GraphsAll import graph_storystifnessY


dict_parameter = {
    1: "Story Displacement",
    2: "Story Drift",
    3: "Story Stiffness",
}

dict_model = {
    1: "G+3",
    2: "G+6",
    3: "G+10",
}

dict_type = {
    1: "Comparative Analysis on Excel Sheet",
    2: "Graph",
}

dictionary_fl = {
    1: "Displ",
    2: "Drift",
    3: "Stiffness",
}



while True:
    
    while True:
        try:
            print("What do you want to calculate?")
            print("")
            print("1. Story Displacement 2. Story Drift 3. Story Stiffness. Choose 1, 2, or 3.")
            print("")
            choice_file = int(input("Enter a number: "))
            print("")

            if choice_file in [1, 2, 3]:
                print(f"You selected option {choice_file}.")
                print("")
                break  
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
                print("")
        except ValueError:
            print("Invalid input. Please enter a number.")
            print("")

    print("Step 1 cleared")
    choice_value_parameter = dict_parameter[choice_file]
    print(f'You chose {choice_value_parameter}')
    choice_value_file = dictionary_fl[choice_file]
    print("")

    
    while True:
        try:
            print("Which model do you want to calculate?")
            print("")
            print("1. G+3 2. G+6 3. G+10 Choose 1, 2, or 3.")
            print("")
            choice_model = int(input("Enter a number: "))
            print("")

            if choice_model in [1, 2, 3]:
                print(f"You selected option {choice_model}.")
                
                print("")
                break 
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
                print("")
        except ValueError:
            print("Invalid input. Please enter a number.")
            print("")

    print("Step 2 cleared")
    choice_value_model = dict_model[choice_model]
    print(f'You chose {choice_value_model} model')
    print("")

    
    while True:
        try:
            print("What do you want as output?")
            print("")
            print("1. Comparative Analysis on Excel 2. Graph Choose")
            print("")
            choice_result_type = int(input("Enter a number: "))
            print("")

            if choice_result_type in [1, 2]:
                print(f"You selected option {choice_result_type}.")
                print("")
                break  
            else:
                print("Invalid input. Please enter 1 or 2.")
                print("")
        except ValueError:
            print("Invalid input. Please enter a number.")
            print("")

    print("Step 3 cleared")
    choice_value_type = dict_type[choice_result_type]
    model = dict_model[choice_model]
    print (f'You chose {model}')
    print(f'You chose {choice_value_type} of {choice_value_file}')
    print("")

    if (choice_result_type == 1):
        df_cnt = read_excel(f'Analysis/AllExcel/{model}CNT{choice_value_file}.xlsx')
        df_conc = read_excel (f'Analysis/AllExcel/{model}CONC{choice_value_file}.xlsx')
        
        finaloutput_XY(df_cnt, df_conc, choice_value_file, model)
        print("Excel Sheet has been produced")
        print("")
    
    if (choice_result_type==2):



        df_cnt = read_excel(f'Analysis/AllExcel/{model}CNT{choice_value_file}.xlsx')
        df_conc = read_excel (f'Analysis/AllExcel/{model}CONC{choice_value_file}.xlsx')

        if (choice_file == 1):
            graph_storydisplX(df_cnt, df_conc, model)
            graph_storydisplY(df_cnt, df_conc, model)
        elif (choice_file ==2):
            graph_storydriftX(df_cnt, df_conc, model)
            graph_storydriftY(df_cnt, df_conc, model)
        elif (choice_file ==3):
            graph_storystiffnessX(df_cnt, df_conc, model)
            graph_storystifnessY(df_cnt, df_conc, model)

       

        print(f"Graph of {model} {choice_value_file} has been be produced")

    
    while True:
        try:
            print("Do you want to restart the program? (Yes/No)")
            restart = input("Enter Yes or No: ").strip().lower()
            if restart in ['yes', 'no']:
                if restart == 'no':
                    print("Task Complete")
                    exit()  
                else:
                    print("Restarting the program...\n")
                    break  
            else:
                print("Invalid input. Please enter Yes or No.")
        except ValueError:
            print("Invalid input.")
