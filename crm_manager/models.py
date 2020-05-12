from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Promocode(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True, unique=True)
    amount_percent = models.CharField(max_length=255, blank=True, null=True)
    PERCENT = "percent"
    AMOUNT = "amount"
    PROMO_TYPE = (
        (AMOUNT,'Amount'),
        (PERCENT,'Percentage'),
                 )
    type = models.CharField(max_length=100, choices=PROMO_TYPE)
    is_Available = models.BooleanField(default=True)
    is_free = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.code

class Calculator(models.Model):
        firstnumber = models.IntegerField()
        lastnumber = models.IntegerField()
        result = models.IntegerField()
        user = models.ForeignKey(User, blank=True, null=True)

        Add = "Add"
        subtract = "subtract"
        multiply = "multiply"
        division = "division"
        CAL_TYPE = (
            (Add, 'Add'),
            (subtract, 'subtract'),
            (multiply, 'multiply'),
            (division, 'division'),
        )
        type = models.CharField(max_length=100, choices=CAL_TYPE)

        def __int__(self):
            return self.firstnumber


class Code(models.Model):

    name = models.CharField(max_length=120, blank=False, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null= True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __int__(self):
        return self.name