from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from model_utils import Choices


BODY_AREA = Choices("all", "sacral", "heel", "fingers", "toes", "leg", "arms", "torso", "head", "groin")


class Dressing(models.Model):
    
    ABSORB_LEVEL = Choices("low", "medium", "high")
    MORPH_TYPE = Choices("morphous", "amorphous")
    ADDED_AGENT = Choices("silver", "iodine", "honey")

    # Dressing details
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    # Dressing categories
    absorbancy = models.CharField(max_length=10, choices=ABSORB_LEVEL)
    body_area = models.CharField(max_length=10, choices=BODY_AREA, default=BODY_AREA.all)
    morphology = models.CharField(max_length=10, choices=MORPH_TYPE)
    anti_microbial = models.BooleanField(default=False)
    added_agent = models.CharField(max_length=10, blank=True, choices=ADDED_AGENT)
    adherence = models.BooleanField(default=False)
    fibrous = models.BooleanField(default=False)
    foam = models.BooleanField(default=False)
    hydrating = models.BooleanField(default=False)
    debriding = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            viewname="dressing_detail",
            kwargs={
                "slug": self.name,
            }
        )

    @property 
    def whole_body(self):
        return self.body_area == BODY_AREA.all

# class Product(Dressing):
    

class Wound(models.Model):
    
    EXUDATE_LEVEL = Choices("low", "medium", "high")
    WOUND_TYPE = Choices(
        ("pink", "Epithelialising"),
        ("red", "Granulating"),
        ("yellow", "Sloughy"),
        ("black", "Necrotic/Eschar"),
        ("infected", "Infected"),
        ("malignant", "Malignant"),
    )
    WOUND_DEPTH = Choices("shallow", "medium", "deep")
    CHANGE_FREQUENCY = Choices(
        ("low", "Weekly"),
        ("mid", "3-6x Week"),
        ("high", "Daily"),
    )
    WOUND_AGE = Choices(
        ("fresh", "less than 24 hours"),
        ("recent", "less than a week"),
        ("established", "less than a month"),
        ("mature", "less than six months"),
        ("old", "more than six months"),
        ("chronic", "more than a year"),
    )
    CLASSIFICATION = Choices("acute", "chronic")
    HERITAGE = Choices("inherited", "new")

    # Entry details
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    patient_nhs_number = models.CharField(max_length=15, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # Wound description
    heritage = models.CharField(max_length=15, choices=HERITAGE, default=HERITAGE.new)
    exudate_level = models.CharField(max_length=30, choices=EXUDATE_LEVEL)   
    wound_type = models.CharField(max_length=30, choices=WOUND_TYPE)
    wound_depth = models.CharField(max_length=30, choices=WOUND_DEPTH)
    body_area = models.CharField(max_length=10, choices=BODY_AREA)
    change_frequency = models.CharField(max_length=50, choices=CHANGE_FREQUENCY)
    wound_age = models.CharField(max_length=50, choices=WOUND_AGE, default=WOUND_AGE.fresh)
    wound_classification = models.CharField(max_length=10, choices=CLASSIFICATION)
    diabetic_patient = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created"]
        get_latest_by = "created"

    def __unicode__(self):
        return unicode("Wound {pk} by {user}".format(pk=self.id, user=self.user))
        
    @property 
    def whole_body(self):
        return self.body_area == BODY_AREA.all
