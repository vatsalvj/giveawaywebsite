from django.db import models

class Items(models.Model):


    item=models.OneToOneField(null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    product=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.item
