from django.db import models

# Create your models here.

#Not sure if I need this so just commenting it ou
#class MenuItemType(models.Model):
#  #Is it a pizza, pasta, salad, sub, etc.
#  name = models.CharField(max_length=20)
#
#
#class MenuItem(models.Model):
#  name = models.CharField(max_length=25)
#  item_type = models.ForeignKey(MenuItemType, on_delete=models.CASCADE)
#  display_order = models.IntegerField()

class PizzaCrust(models.Model):
  #Sicilian or Regular
  name = models.CharField(max_length=20)

  def __str__(self):
    return f"{self.name}"

class PizzaStyle(models.Model):
  name = models.CharField(max_length=20)
  free_toppings = models.IntegerField()

  def __str__(self):
    return f"{self.name}"

class PizzaSize(models.Model):
  name = models.CharField(max_length=10)

  def __str__(self):
    return f"{self.name}"

class PizzaTopping(models.Model):
  name = models.CharField(max_length=20)

  def __str__(self):
    return f"{self.name}"
  
class Pizza(models.Model):
  crust = models.ForeignKey(PizzaCrust, on_delete=models.CASCADE)
  style = models.ForeignKey(PizzaStyle, on_delete=models.CASCADE)
  size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=4, decimal_places=2)

  def __str__(self):
    return f"{self.crust.name} pizza - {self.size.name} - {self.style.name} "

