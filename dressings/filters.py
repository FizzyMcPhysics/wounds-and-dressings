import django_filters

from .models import Dressing, BODY_AREA

class DressingFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_type='icontains')
    body_area = django_filters.MultipleChoiceFilter()

    class Meta:
        model = Dressing 
        fields = [
            'name', 
            'suitable_for',
            'absorbancy',
            'body_area',
            'morphology',
            'anti_microbial',
            'topical_agent',
            'adherence',
            'fibrous',
            'foam',
            'hydrating',
            'debriding',
            'diabetic_safe',
        ]

    def __init__(self, *args, **kwargs):
        super(DressingFilter, self).__init__(*args, **kwargs)
        self.filters['body_area'].extra.update(
            {
                'choices': [('', 'Any')] + list(BODY_AREA)   
            }
        )