from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=50)
    last_login = models.DateTimeField(null=True, blank=True)

class Waste(models.Model):
    material = models.CharField(max_length=255)
    waste_type = models.CharField(max_length=255)
    is_recycle = models.BooleanField()
    main_color = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=255)
    sample_image = models.CharField(max_length=255)
    description = models.TextField()

class DisposalHistory(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    waste = models.ForeignKey(Waste, on_delete=models.CASCADE)
    waste_type = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    capture = models.TextField()

class Bin(models.Model):
    bin_type = models.CharField(max_length=255)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    usage = models.CharField(max_length=255)
    content_weight = models.DecimalField(max_digits=10, decimal_places=2)