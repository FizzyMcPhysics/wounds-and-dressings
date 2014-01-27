from django import forms

from . import models 

class WoundForm(forms.ModelForm):
    class Meta:
        model = models.Wound 
        fields = (
            "patient_nhs_number",
            "heritage",
            "body_area",
            "wound_type",
            "wound_depth",
            "exudate_level",
            "wound_age",
            "wound_classification",            
        )

    def __init__(self, *args, **kwargs):
        super(WoundForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
