from django.core.urlresolvers import reverse
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.conf import settings
from model_utils import Choices


BODY_AREA = Choices("sacral", "heel", "fingers", "toes", "leg", "arms", "torso", "head", "groin")
WOUND_TYPE = Choices(
    ("pink", "Epithelialising"),
    ("red", "Granulating"),
    ("yellow", "Sloughy"),
    ("black", "Necrotic/Eschar"),
    ("infected", "Infected"),
    ("malignant", "Malignant"),
    ("exuding", "High Exuding"),
)
WOUND_DEPTH = Choices("shallow", "medium", "deep")


class WoundType(models.Model):

    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return self.name


class Dressing(models.Model):
    
    ABSORB_LEVEL = Choices("none", "low", "medium", "high")
    MORPH_TYPE = Choices("morphous", "amorphous")
    TOPICAL_AGENT = Choices(
        ("none", "no agent"),
        "silver",
        "iodine",
        "honey"
    )

    # Dressing details
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.CharField(
        max_length=30,
        unique=True,
        help_text="This is the URL safe name to be used in the URL.",
        blank=True,
        null=True,
    )
    
    # Dressing categories
    absorbancy = models.CharField(max_length=10, choices=ABSORB_LEVEL, default=ABSORB_LEVEL.low)
    body_area = models.CharField(max_length=10, choices=BODY_AREA, blank=True)
    morphology = models.CharField(max_length=10, choices=MORPH_TYPE)
    anti_microbial = models.BooleanField(default=False)
    topical_agent = models.CharField(max_length=10, choices=TOPICAL_AGENT, default=TOPICAL_AGENT.none)
    adherence = models.BooleanField(default=False)
    fibrous = models.BooleanField(default=False)
    foam = models.BooleanField(default=False)
    hydrating = models.BooleanField(default=False)
    debriding = models.BooleanField(default=False)
    diabetic_safe = models.BooleanField(default=True)
    suitable_for = models.ManyToManyField(WoundType)
    deep_wounds = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            viewname="dressing_detail",
            kwargs={
                "slug": self.slug,
            }
        )

    @property 
    def whole_body(self):
        return self.body_area == BODY_AREA.all

    def clean(self):
        from django.template.defaultfilters import slugify
        if "hydrocolloid" in self.name and self.diabetic_safe:
            raise ValidationError("Hydrocolloids are not diabetic safe!") 
        self.name = self.name.lower()
        self.slug = slugify(self.name)


# class Product(Dressing):
    

class Wound(models.Model):
    
    EXUDATE_LEVEL = Choices("none", "low", "medium", "high")
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
    patient_nhs_number = models.CharField(max_length=15, blank=True, verbose_name="Patient NHS Number")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # Wound description
    heritage = models.CharField(max_length=15, choices=HERITAGE, default=HERITAGE.new)
    exudate_level = models.CharField(max_length=30, choices=EXUDATE_LEVEL)   
    wound_type = models.ForeignKey(WoundType)
    wound_depth = models.CharField(max_length=30, choices=WOUND_DEPTH)
    body_area = models.CharField(max_length=10, choices=BODY_AREA, blank=True)
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
