from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
year_choice = []
for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))


features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
        )

door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

class Car(models.Model):

    car_title = models.CharField(max_length=250)
    state = models.CharField(choices = state_choice,max_length=250)
    city = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    color = models.CharField(max_length=250)
    year = models.IntegerField(('year'), choices =year_choice)
    condtion = models.IntegerField()
    price = models.CharField(max_length=250)
    description = RichTextField()
    car_photo =  models.ImageField(upload_to = 'photo/%Y/%m/%d/')
    carphoto1 = models.ImageField(upload_to = 'photo/%Y/%m/%d/',blank=True)
    carphoto2 =  models.ImageField(upload_to = 'photo/%Y/%m/%d/',blank=True)
    carphoto3 =  models.ImageField(upload_to = 'photo/%Y/%m/%d/',blank=True)
    carphoto4 =  models.ImageField(upload_to = 'photo/%Y/%m/%d/',blank=True)
    features = MultiSelectField(choices = features_choices)
    body_style = models.CharField(max_length=250)
    engine = models.CharField(max_length=250)
    transmission = models.CharField(max_length=250)
    interiors = models.CharField(max_length=250)
    miles = models.IntegerField()
    doors = models.CharField(choices = door_choices,max_length=250)
    passangers = models.IntegerField
    vech_no =  models.CharField(max_length=250)
    milage  =  models.IntegerField()
    fuel_type = models.CharField(max_length=250)
    no_of_owners = models.CharField(max_length=250)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.car_title
     
