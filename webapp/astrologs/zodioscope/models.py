from django.db import models
from django.contrib.postgres.fields import DateRangeField
# from django.contrib.postgres.fields import RangeOperators
# from django.contrib.postgres.constraints import ExclusionConstraint
# Create your models here.

class ZodioscopeDaily(models.Model):
    date_range = DateRangeField(unique=False)
    sign = models.CharField(max_length=15, blank=True, null=True)
    current_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    compatibility = models.CharField(max_length=15, blank=True, null=True)
    mood = models.CharField(max_length=15, blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    lucky_number = models.IntegerField(blank=True, null=True)
    lucky_time = models.CharField(max_length=15, blank=True, null=True)
    
        # class Meta:
        # constraints = [
        #     ExclusionConstraint(
        #         name='include_overlap',
        #         expressions=[
        #             ('date_range', RangeOperators.OVERLAPS),
        #         ],
        #     )
        # ]
    
    
    def __str__(self):
        return f"{self.current_date.strftime('%m/%d/%Y')} predictions for {self.sign}"