"""from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Pizza(models.Model): #pizza hereda características de Model. 
    name = models.CharField(verbose_name=("Name"), max_length=100) #verbose_name, es el nombre que se da a Name, es interno
    ingredients = models.ManyToManyField("pizza.Ingredient" , verbose_name=("Ingredients"), related_name="pizza")#Ingredient es una tabla
    image = models.CharField(verbose_name=("image"), max_length=500)
    
    def __str__(self): #método igual que el toString de Java, saca el nombre de la pizza
        return self.name#Con este método, en el crud que crea pone el nombre del ingrediente, si no lo ponemos
        #pondría en la aplicación ingrediente object
    def get_absolute_url(self):#coger de la url de entrada el objeto de pizza
         #Devuelve la url de acceso a una instancia de mi nombre de modelo
        return reverse('pizza:pizza_detail', kwargs={'pk' : self.pk })

class Ingredient(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=100)
    price = models.DecimalField(verbose_name=("Price"), max_digits=6, decimal_places=2)

    def __str__(self): #método igual que el toString de Java, obtiene el nombre del ingrediente
        return self.name + "price " + str(self.price)#Con este método, en el crud que crea pone el nombre del ingrediente, si no lo ponemos
        #pondría en la aplicación ingrediente object

    def get_absolute_url(self):#coger de la url de entrada el objeto de pizza
         #Devuelve la url de acceso a una instancia de mi nombre de modelo
        return reverse('pizza:ingredient_detail', kwargs={'pk' : self.pk })"""

from django.db import models
from decimal import Decimal
from django.core.urlresolvers import reverse

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=100)
    ingredients = models.ManyToManyField("pizza.Ingredient", verbose_name=("Ingredients"), related_name="pizza")
    image = models.FileField(blank=True, null=True)

    @property
    def price(self):
        price = Decimal(0.0)
        for ingredient in self.ingredients.all():
            price += ingredient.price
        return price * Decimal(1.5)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of Pizza.
         """
         return reverse('pizza:pizza_detail', kwargs={ 'pk': self.pk })


class Ingredient(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=100)
    price = models.DecimalField(verbose_name=("Price"), max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of Ingredient.
         """
         return reverse('pizza:ingredient_detail', kwargs={ 'pk': self.pk })
    