from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from stage_prediction.models import Input, InputForm, Output

# Import neccessary things for predicting
import os
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Sepecify the relative path to the model file
model_relative_path = 'stage_prediction_updated.pkl'

# Create the absolute path to the model file
model_absolute_path = os.path.join(current_directory, model_relative_path)

# Load the model from disk
loaded_model = pickle.load(open(model_absolute_path, 'rb'))

def stage_prediction(request):

    if request.method == 'POST':
        user_input = InputForm(request.POST)
        if user_input.is_valid():

            # Save the user input values into input table
            user_input.save()

            # Read the input1 and input2 from the input table
            last_row_input = Input.objects.last()
            input_form = InputForm(initial=last_row_input.__dict__)

            # Calculate the total_number
            input1 = last_row_input.input1
            input1 = float(input1)
            input2 = last_row_input.input2
            input2 = float(input2)
            input3 = last_row_input.input3
            input4 = last_row_input.input4
            input4 = float(input4)
            input5 = last_row_input.input5
            input5 = float(input5)
            input6 = last_row_input.input6
            input7 = last_row_input.input7
            input8 = last_row_input.input8
            input9 = last_row_input.input9
            input9 = float(input9)
            input10 = last_row_input.input10
            input10 = float(input10)
            input11 = last_row_input.input11
            input12 = last_row_input.input12
            input13 = last_row_input.input13
            input14 = last_row_input.input14
            input15 = last_row_input.input15
            input15 = float(input15)
            input16 = last_row_input.input16
            input17 = last_row_input.input17
            input18 = last_row_input.input18
            # total_number = input1 + input2 + input3 + input4 + input5 + input6 + input7 + input8 + input9 + input10 + input11 + input12 + input13 + input14 + input15 + input16 + input17 + input18

            # 'input1': 'Hepatomegaly',
            # 'input2': 'Status',
            # 'input3': 'Albumin',
            # 'input4': 'Spiders',
            # 'input5': 'Edema',
            # 'input6': 'Copper',
            # 'input7': 'Platelets',
            # 'input8': 'SGOT',
            # 'input9': 'Ascites',
            # 'input10': 'Drug',
            # 'input11': 'Alk_Phos',
            # 'input12': 'Tryglicerides',
            # 'input13': 'Age',
            # 'input14': 'Cholesterol',
            # 'input15': 'Sex',
            # 'input16': 'Prothrombin',
            # 'input17': 'Bilirubin',
            # 'input18': 'N_Days'
            
            Hepatomegaly  = input1
            Status        = input2
            Albumin       = input3
            Spiders       = input4
            Edema         = input5
            Copper        = input6
            Platelets     = input7
            SGOT          = input8
            Ascites       = input9
            Drug          = input10
            Alk_Phos      = input11
            Tryglicerides = input12
            # Age           = input13
            # Cholesterol   = input14
            # Sex           = input15
            # Prothrombin   = input16
            # Bilirubin     = input17
            # N_Days        = input18


            last_row_input_data = np.array([[Hepatomegaly, Status, Albumin, Spiders, Edema,
                                             Copper, Platelets, SGOT, Ascites, Drug]])
            
            last_row_input_data = pd.DataFrame(last_row_input_data)
            # print("last_row_input_data = ", last_row_input_data)
            

            # feature scaling helps improve reach convergence faster
            scaler = StandardScaler()
            # X_train = scaler.fit_transform(X_train)
            # X_test  = scaler.transform(X_test)            
            last_row_input_data  = scaler.fit_transform(last_row_input_data)

            predicted_output = loaded_model.predict(last_row_input_data)
            predicted_output = predicted_output[0] # Get element inside array

            # Stages of the patient
            # 0 = 1,
            # 1 = 2,
            # 2 = 3,
            # 3 = 4,
            if predicted_output == 0.0:
                predicted_output = 'Histologic stage of disease : 1'
            elif predicted_output == 1.0:
                predicted_output = 'Histologic stage of disease : 2'
            elif predicted_output == 2.0:
                predicted_output = 'Histologic stage of disease : 3'
            elif predicted_output == 3.0:
                predicted_output = 'Histologic stage of disease : 4'
            else:
                predicted_output = 'Please check with Doctor again!'

            # Save the output1 value in the table
            Output(output1 = predicted_output).save()

            # Read the output1 from the output table
            output_last_recorded = Output.objects.last()
            output = output_last_recorded.output1


            return render(request, 'stage_prediction.html', {'input_form': input_form,
                                                  'output': output})
        else:
            input_form = InputForm()
            return render(request, 'survival_prediction.html', {'input_form': input_form})

    else:
        input_form = InputForm()
        return render(request, 'stage_prediction.html', {'input_form': input_form})