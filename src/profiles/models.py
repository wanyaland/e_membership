from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    SINGLE = 'Single'
    MARRIED = 'Married'
    WIDOWED = 'Widowed'
    SEPARATED = 'Separated'
    OTHER = 'Other'
    MONTHLY = 'M'
    ANNUAL ='A'
    MARITAL_STATUS=(
        (SINGLE,'Single'),
        (MARRIED,'Married'),
        (WIDOWED,'Widowed'),
        (SEPARATED,'Separated'),
        (OTHER,'Other')
    )
    SUBSCRIPTION_OPTION = (
        (MONTHLY,'Monthly'),
        (ANNUAL,'Annual'),
    )
    date_of_birth = models.DateField(null=True)
    nationality = models.CharField(null=True,max_length=200)
    country_of_residence = models.CharField(null=True,max_length=200)
    marital_status = models.CharField(null=True,choices=MARITAL_STATUS,max_length=200)
    telephone = models.CharField(null=True,max_length=200)
    email = models.EmailField(null=True)
    postal_address = models.TextField(null=True)
    town = models.CharField(null=True,max_length=200)
    village = models.CharField(null=True,max_length=200)
    national_id_doc = models.FileField(null=True,upload_to='national_id')
    national_id = models.CharField(null=True,max_length=200)
    subscription = models.CharField(null=True,choices=SUBSCRIPTION_OPTION,max_length=200)

    def __str__(self):
        return "{}'s profile". format(self.user)
