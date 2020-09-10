from django.db import models


class Category(models.Model):
    """
    Support table
    """
    category = models.CharField(unique=True)
    description = models.CharField(null=True, blank=True)


class FoodCoding(models.Model):
    """
    Support table
    """
    fid_cde = models.IntegerField(unique=True)  # Food code
    fdc_den = models.CharField()  # Food description english


class BNSFoodCoding(models.Model):
    """
    Support table
    """
    fid_fgr = models.CharField(unique=True)  # BNS food code
    fdc_fge = models.CharField()  # BNS food group description


class FoodItem(models.Model):
    """
    Table that allows for new entries to be added with values from support tables
    """
    food = models.ForeignKey(FoodCoding, on_delete=models.CASCADE)
    bns_category = models.ForeignKey(BNSFoodCoding, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
