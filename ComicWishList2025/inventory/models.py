from django.db import models

class Comic(models.Model):
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    grade = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.BinaryField()

    def __str__(self):
        return f"{self.title} #{self.number} - Grade: {self.grade}"
