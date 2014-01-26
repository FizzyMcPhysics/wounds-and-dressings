from django import forms

from . import models 

class WoundForm(forms.ModelForm):
    class Meta:
        model = models.Wound 
        fields = (
            "patient_nhs_number",
            "diabetic_patient",            
            "heritage",
            "body_area",
            "wound_type",
            "wound_depth",
            "exudate_level",
            "wound_age",
            "wound_classification",
        )
        