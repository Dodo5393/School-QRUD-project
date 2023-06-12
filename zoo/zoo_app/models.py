
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator,MinLengthValidator
from django.core.validators import ValidationError
from django.utils import timezone



class Animal(models.Model):
    SPECIES_CHOICES = [
        ('mammal', 'Mammal'),
        ('bird', 'Bird'),
        ('reptile', 'Reptile'),
        ('amphibian', 'Amphibian'),
        ('fish', 'Fish'),
    ]
    
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100, choices=SPECIES_CHOICES)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    date_added = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])


    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    description = models.TextField()

class Positions(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

class AnimalHabitat(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    entry_date = models.DateField()
    exit_date = models.DateField()

    def __str__(self):
        return self.name

    def clean(self):
        if self.entry_date >= self.exit_date:
            raise ValidationError((' entry time must be later than the exit time.'))




class Visitor(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    ticket_type = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Exhibit(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(AnimalHabitat, on_delete=models.CASCADE)
    capacity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def clean(self):
        if self.start >= self.end:
            raise ValidationError(('Closing time must be later than the opening time.'))

class FeedingSchedule(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    time = models.TimeField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
   

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    def __str__(self):
        return self.name

    



