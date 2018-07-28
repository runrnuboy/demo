irom django.db import models

class Person(models.Model):
  p_name=models.CharField(max_length=64)
