from django.conf.urls import url#librería para configurar las urls que necesitemos en la aplicación
from . import views #importar de las vistas

app_name = 'pizza'#los patrones de url que encontremos, pertenece a pizza
urlpatterns = [
    #/pizza/
    url(r'^$', views.index , name='index'),
    url(r'^([0-9]+)/$', views.pizza_detail , name='detail'),
    url(r'^pizzas/$' , views.PizzasListView.as_view(), name='pizzas'),
    url(r'^pizza/(?P<pk>[0-9]+)/$' , views.PizzaDetailView.as_view(), name='pizza_detail'),

    url(r'^ingredients/$' , views.IngredientListView.as_view(), name='ingres lo que ponemos en la urledientes'),
    url(r'^ingredients/(?P<pk>[0-9]+)/$' , views.IngredientDetailView.as_view(), name='ingredient_detail'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),#primer register, es el nombre de la ruta url que nosotros ponemos
    url(r'^add/$', views.PizzaCreate.as_view(), name='add-pizza'),
    url(r'^update/(?P<pk>[0-9]+)/', views.PizzaUpdate.as_view(), name='update-pizza'),
    url(r'^delete/(?P<pk>[0-9]+)/', views.PizzaDelete.as_view(), name='delete-pizza'),
]