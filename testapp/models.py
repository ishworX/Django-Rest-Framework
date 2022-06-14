from django.db import models
from django.utils import timezone

# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length= 255, unique=True, null=False, blank = False, error_messages={
        "null": "This field cannot be null",
        "blank" : "You cannot leave it blank" 
    })
    desc = models.TextField()
    phone = models.PositiveIntegerField()
    is_live = models.BooleanField()
    amount = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
     

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = 