from django.db import models
from django import forms

# Create your models here.
class Input(models.Model):
    input1 = models.CharField(
        max_length=30,
        choices= [('0.0','N'),
                  ('1.0','Y')],
        default='0.0'
    )
    input2 = models.CharField(
        max_length=50,
        choices= [('0.0','D'),
                  ('1.0','C'),
                  ('2.0','CL')],
        default='2.0'
    )
    input3 = models.FloatField(
        null=True,
        default=None
    )
    input4 = models.CharField(
        max_length=30,
        choices= [('0.0','N'),
                  ('1.0','Y')],
        default='0.0'
    )
    input5 = models.CharField(
        max_length=30,
        choices= [('0.0','N'),
                  ('1.0','Y')],
        default='0.0'
    )
    input6 = models.FloatField(
        null=True,
        default=None
    )
    input7 = models.FloatField(
        null=True,
        default=None
    )
    input8 = models.FloatField(
        null=True,
        default=None
    )
    input9 = models.CharField(
        max_length=30,
        choices= [('0.0','N'),
                  ('1.0','Y')],
        default='0.0'
    )
    input10 = models.CharField(
        max_length=30,
        choices= [('0.0','D-pennicillamine'),
                  ('1.0','Placebo')],
        default='0.0'
    )
    input11 = models.FloatField(
        null=True,
        default=None
    )
    input12 = models.FloatField(
        null=True,
        default=None
    )
    input13 = models.FloatField(
        null=True,
        default=None
    )
    input14 = models.FloatField(
        null=True,
        default=None
    )
    input15 = models.CharField(
        max_length=30,
        choices= [('0.0','F'),
                  ('1.0','M')],
        default='0.0'
    )
    input16 = models.FloatField(
        null=True,
        default=None
    )
    input17 = models.FloatField(
        null=True,
        default=None
    )
    input18 = models.FloatField(
        null=True,
        default=None
    )

class InputForm(forms.ModelForm):
    class Meta:
        # models = Input # Typing wrong, model with s!
        model = Input    # Typing correct, model without s
        fields = '__all__'
        # Temp using, when Frontend done will have 18 features
        labels = {
            'input1': 'Hepatomegaly',   # Add drop-down list already
            'input2': 'Status',         # Add drop-down list already
            'input3': 'Albumin',
            'input4': 'Spiders',        # Add drop-down list already
            'input5': 'Edema',          # Add drop-down list already
            'input6': 'Copper',
            'input7': 'Platelets',
            'input8': 'SGOT',
            'input9': 'Ascites',        # Add drop-down list already
            'input10': 'Drug',          # Add drop-down list already
            'input11': 'Alk_Phos',
            'input12': 'Tryglicerides',
            'input13': 'Age',
            'input14': 'Cholesterol',
            'input15': 'Sex',         # Add drop-down list already
            'input16': 'Prothrombin',
            'input17': 'Bilirubin',
            'input18': 'N_Days'
        }        

class Output(models.Model):
    output1 = models.CharField(
        max_length=100,
        default='Please SUBMIT Data'
    )