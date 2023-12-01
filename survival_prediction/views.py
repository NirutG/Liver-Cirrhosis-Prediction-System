from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from survival_prediction.models import Input, InputForm, Output

# Import neccessary things for predicting
import os
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Sepecify the relative path to the model file
model_relative_path = 'survival_predictoin.pkl'

# Create the absolute path to the model file
model_absolute_path = os.path.join(current_directory, model_relative_path)

# Load the model from disk
loaded_model = pickle.load(open(model_absolute_path, 'rb'))

# # Temp test
# inference_sample1 = np.array([[4.5, 348, 11.4]])
# inference_sample2 = np.array([[12.6, 51, 11.5]])
# inference_sample3 = np.array([[0.7, 4459, 10.6]])
# # Try to use inference sample 1 to predict
# predicted_selling_price1 = loaded_model.predict(inference_sample1)
# predicted_selling_price2 = loaded_model.predict(inference_sample2)
# predicted_selling_price3 = loaded_model.predict(inference_sample3)
# print('predicted_selling_price1 :', predicted_selling_price1[0])
# print('predicted_selling_price2 :', predicted_selling_price2[0])
# print('predicted_selling_price3 :', predicted_selling_price3[0])

def survival_prediction(request):

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
            input2 = last_row_input.input2
            input3 = last_row_input.input3
            input4 = last_row_input.input4
            input5 = last_row_input.input5
            input5 = float(input5)
            input6 = last_row_input.input6
            input7 = last_row_input.input7
            input7 = float(input7)
            input8 = last_row_input.input8
            input9 = last_row_input.input9
            input10 = last_row_input.input10
            input11 = last_row_input.input11
            input12 = last_row_input.input12
            input12 = float(input12)
            input13 = last_row_input.input13
            input14 = last_row_input.input14
            input15 = last_row_input.input15
            input15 = float(input15)
            input16 = last_row_input.input16
            input16 = float(input16)
            input17 = last_row_input.input17
            input17 = float(input17)
            input18 = last_row_input.input18
            input18 = float(input18)
            # total_number = input1 + input2 + input3 + input4 + input5 + input6 + input7 + input8 + input9 + input10 + input11 + input12 + input13 + input14 + input15 + input16 + input17 + input18
            
            # 'input1': 'Bilirubin',
            # 'input2': 'N_Days',
            # 'input3': 'Prothrombin',
            # 'input4': 'Copper',
            # 'input5': 'Edema',
            # 'input6': 'Platelets',
            # 'input7': 'Ascites',
            # 'input8': 'Age',
            # 'input9': 'Albumin',
            # 'input10': 'SGOT',
            # 'input11': 'Alk_Phos',
            # 'input12': 'Spiders',
            # 'input13': 'Tryglicerides',
            # 'input14': 'Cholesterol',
            # 'input15': 'Sex',
            # 'input16': 'Hepatomegaly',
            # 'input17': 'Drug',
            # 'input18': 'Stage'

            Bilirubin       = input1
            N_Days          = input2
            Prothrombin     = input3
            Copper          = input4
            Edema           = input5
            Platelets       = input6
            Ascites         = input7
            Age             = input8
            Albumin         = input9
            SGOT            = input10
            Alk_Phos        = input11
            Spiders         = input12
            Tryglicerides   = input13
            Cholesterol     = input14
            Sex             = input15
            Hepatomegaly    = input16
            Drug            = input17
            Stage           = input18

            # print(f"Bilirubin   = {Bilirubin},   Type is {type(Bilirubin)}")
            # print(f"N_Days      = {N_Days},      Type is {type(N_Days)}")
            # print(f"Prothrombin = {Prothrombin}, Type is {type(Prothrombin)}")

            last_row_input_data = np.array([[Bilirubin, N_Days, Prothrombin]])
            # print('last_row_input_data : ', last_row_input_data)
            predicted_output = loaded_model.predict(last_row_input_data)
            predicted_output = predicted_output[0] # Get element inside array

            # lass Labels
            # Status: status of the patient 
            # 0 = D (death), 
            # 1 = C (censored), 
            # 2 = CL (censored due to liver transplantation)
            if predicted_output == 0.0:
                predicted_output = 'Status of the patient : Less chances of survival!' # Death
            elif predicted_output == 1.0:
                predicted_output = 'Status of the patient : Censored' # Data not available
            elif predicted_output == 2.0:
                predicted_output = 'Status of the patient : Take liver transplantation'
            else:
                predicted_output = 'Please check with Doctor again!'



            # Save the output1 value in the table
            Output(output1 = predicted_output).save()

            # Read the output1 from the output table
            output_last_recorded = Output.objects.last()
            output = output_last_recorded.output1


            return render(request, 'survival_prediction.html', {'input_form': input_form,
                                                  'output': output})
        else:
            input_form = InputForm()
            return render(request, 'survival_prediction.html', {'input_form': input_form})

    else:
        input_form = InputForm()
        return render(request, 'survival_prediction.html', {'input_form': input_form})