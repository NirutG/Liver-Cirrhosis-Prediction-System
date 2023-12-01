# Use the official Python base image
FROM python:3.10-slim

# Set the working directory in the container
# WORKDIR /root/lcps_v1
WORKDIR /lcps_v1

# Install project dependencies
RUN pip3 install ipykernel==6.25.1
RUN pip3 install seaborn==0.13.0
RUN pip3 install ppscore==1.1.0
RUN pip3 install Django==4.2.4
RUN pip3 install mlflow==2.8.0
RUN pip3 install numpy==1.26.0
RUN pip3 install pandas==2.1.1
RUN pip3 install scikit-learn==1.3.0
RUN pip3 install matplotlib==3.8.0
RUN pip3 install pandoc==2.3
# RUN pip3 install fastapi                          
# RUN pip3 install gensim
# RUN pip3 install huggingface_hub
# RUN pip3 install scipy
# RUN pip3 install spacy
# RUN pip3 install torch                       
# RUN pip3 install torchtext  
# RUN pip3 install torchvision                     
# RUN pip3 install tqdm                             
# RUN pip3 install transformers
# RUN pip3 install evaluate
# RUN pip3 install sentencepiece
# RUN pip3 install accelerate
# RUN pip3 install datasets
RUN pip3 install pillow
RUN pip3 install shap
RUN pip3 install xgboost
RUN pip3 install imblearn

# Copy the project code to the working directory
# COPY ./lcps_v1 /root/lcps_v1
COPY . .

CMD tail -f /dev/null

# Expose the Django development server port
# EXPOSE 8000

# Define the command to run the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]