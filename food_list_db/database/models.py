from django.db import models

# Sensible field sizes for CharField columns
LG_CHAR = 1500
MD_CHAR = 500
SM_CHAR = 50


class Category(models.Model):
    """
    Support table
    """
    category = models.CharField(unique=True, max_length=SM_CHAR)
    description = models.CharField(null=True, blank=True, max_length=MD_CHAR)

    def __str__(self):
        return f"{self.category}"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class FoodCoding(models.Model):
    """
    Support table
    """
    fid_cde = models.IntegerField(unique=True)  # Food code
    fdc_den = models.CharField(max_length=MD_CHAR)  # Food description english

    def __str__(self):
        return f"{self.fid_cde}: {self.fdc_den}"

    class Meta:
        verbose_name = 'Food Coding'
        verbose_name_plural = 'Food Coding'


class BNSFoodCoding(models.Model):
    """
    Support table
    """
    fid_fgr = models.CharField(unique=True, max_length=SM_CHAR)  # BNS food code
    fdc_fge = models.CharField(max_length=MD_CHAR)  # BNS food group description

    def __str__(self):
        return f"{self.fid_fgr}: {self.fdc_fge}"

    class Meta:
        verbose_name = 'BNS Food Coding'
        verbose_name_plural = 'BNS Food Coding'


class FoodItem(models.Model):
    """
    Table that allows for new entries to be added with values from support tables
    """
    food = models.ForeignKey(FoodCoding, on_delete=models.CASCADE)
    bns_category = models.ForeignKey(BNSFoodCoding, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.food}"

    class Meta:
        verbose_name = 'Food Item'
        verbose_name_plural = 'Food Items'
