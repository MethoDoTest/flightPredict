from django.db import models


class FlightPredictionModel(models.Model):
    airline = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    total_stops = models.IntegerField()
    price = models.FloatField()
    date = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    dep_hours = models.IntegerField()
    dep_min = models.IntegerField()
    arrival_hours = models.IntegerField()
    arrival_min = models.IntegerField()
    duration_hours = models.IntegerField()
    duration_min = models.IntegerField()

    def __str__(self):
        return f"{self.date}/{self.month}/{self.year} | {self.airline} | {self.source} to {self.destination} | {self.price}"

    class Meta:
        verbose_name = "Flight Prediction"
        verbose_name_plural = "Flight Prediction"
