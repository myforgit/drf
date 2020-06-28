from django.db import models


# Create your models here.


class Userdrf(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=64)
    class Meta:
        db_table = "bz_userdef"
