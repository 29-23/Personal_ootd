from django.db import models
from hashid_field import HashidAutoField

"""
fashion matching result
"""
SPRING = 'SP'
SUMMER = 'SU'
AUTUMN = 'AU'
WINTER = 'WI'
SEASON_CHOICES = [
    (SPRING, 'spring'),
    (SUMMER, 'summer'),
    (AUTUMN, 'autumn'),
    (WINTER, 'winter')
]

GOOD = 'G'
SOSO = 'S'
BAD = 'B'
RESULT_CHOICES = [
    (GOOD, 'good'),
    (SOSO, 'soso'),
    (BAD, 'bad')
]

# Create your models here.
class Fashion(models.Model):
    id = HashidAutoField(primary_key=True)
    '''user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)'''
    color = models.CharField(max_length=2, choices=SEASON_CHOICES, default=SPRING)
    image = models.ImageField(upload_to='fashion/')
    date = models.DateField()
    spring_rate = models.IntegerField()
    summer_rate = models.IntegerField()
    autumn_rate = models.IntegerField()
    winter_rate = models.IntegerField()
    result = models.CharField(max_length=1, choices=RESULT_CHOICES, default=GOOD)
