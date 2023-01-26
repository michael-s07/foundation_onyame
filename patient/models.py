from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Folder(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    date_registered = models.DateField(default="10/01/2022")
    first_name = models.CharField(max_length=20, null=False)
    median_name = models.CharField(max_length=15, null= True)
    last_name = models.CharField(max_length=20, null=False)
    gender = models.CharField(max_length=5, null=False)
    date_of_birth = models.DateField(default="10/01/2022")
    martial_status = models.CharField(max_length=10, null=False)
    occupation = models.CharField(max_length=19, default="")
    religion = models.CharField(max_length=15, default="")
    address = models.TextField(default="Ablekuma-Obelu behind the Mosque")
    mobile = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=220, default="samle@onyamefoundation.org")
    relative_name = models.CharField(max_length=50, null=False)
    relative_address = models.TextField(default="Ablekuma - Newtown, after the taxi rank")
    relative_contact = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    nhis_number = models.CharField(max_length = 8, default='22222222')
