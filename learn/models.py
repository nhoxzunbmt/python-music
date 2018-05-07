from django.db import models



class Musician(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    id = models.AutoField(primary_key=True)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    first_name = models.CharField("Tran ",max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Topping(models.Model):
    # ...
    name = models.CharField(max_length=100)
    

class Pizza(models.Model):
    # ...
    name = models.CharField(max_length=100)
    toppings = models.ManyToManyField(Topping)
    
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)