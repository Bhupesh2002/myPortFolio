from django.db import models

# Create your models here.
class HealthData(models.Model):
    EXERCISE_CHOICES = [
        ('walking', 'Walking'),
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('yoga', 'Yoga'),
    ]

    age = models.IntegerField(default=25)
    weight = models.FloatField(default=70)  # in kilograms
    duration = models.IntegerField()  # in minutes
    exercise = models.CharField(max_length=20, choices=EXERCISE_CHOICES,default='walking')
    calories_burned = models.FloatField()  # Calculated value

    def __str__(self):
        return (f"Age: {self.age},weight: {self.weight},duration: {self.duration}"
                f",exercise: {self.exercise},calories(in kcal): {self.calories_burned}")