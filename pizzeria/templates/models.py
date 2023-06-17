from django.db import models



class Topping(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
   

    def __str__(self):
        return self.name

class Crust(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default = 1)

    def __str__(self):
        return self.name

class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default = 1)

    def __str__(self):
        return self.name

class Sauce(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default = 1)

    def __str__(self):
        return self.name

class Cheese(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default = 1)

    def __str__(self):
        return self.name
class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE, default=1)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, default=1)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE, default=1)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE, default=1)
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return f"{self.size} {self.crust}"

    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address =models.CharField(max_length=150)
    cardNum = models.CharField(max_length=19, blank=True)
    cvv = models.CharField(max_length=10, blank=True)
    expiration = models.CharField(max_length=5, blank=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)



