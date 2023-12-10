from django.db import models

# Create your models herel
class sensor_data(models.Model):
    temperature = models.FloatField(max_length=5)
    npk = models.FloatField(max_length=5)
    moisture = models.FloatField(max_length=5)
    timestamp_field = models.DateTimeField(db_index=True)  # Set db_index to True for indexing
    # Other fields here
