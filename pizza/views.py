from django.http import HttpResponse
from .models import Pizza,Ingredient
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.views.generic.edit import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views heredef index(request):
    #conseguimos los numeros de pizza en bbdd
    #num_pizza =Pizza.objects.count()
    #print(num_pizza)
    #construimos la cadena para mostrar
    #micadena="<style>body{background:#000000;color:white}</style><h1>En la pizzeria tenemos: ", num_pizza ,"pizzas</h1>"
    #return HttpResponse(micadena)
    #otra forma de hacerlo :
#def index(request):
    #all_pizzas= Pizza.objects.all()
    #cadena de Html para mostrar en la página
    #html="""
#<html>
    #<head>
    #<style>
#*{  font-family:"ms comic sans";
    #color:white;
    #background-color:black;
    #margin-left:17%;
#}
#h1{
    #margin-left:11%;
#}

    #</style>
    #<title>MI PAGINA DE PIZZAS SUPER CHACHI</title>
    #<h1>Mi lista de pizzas</h1>
    #</head>
    

#"""
    #en este bucle construimos el html
    #for pizza in all_pizzas:
        #construimos url para cada pizza
        #url= '/pizza/' + str(pizza.id) + '/'
        #añadimos url dentro de la cadena de html
        #html += '<a href ="' + url + '">' + pizza.name + '</a><br>'
    #fuera de bucle acordad de la identacion
    #return HttpResponse(html)

#OTRA FORMA DE HACERLO BAJANDO PLANTILLAS


#def index(request):
    #all_pizzas = Pizza.objects.all()
    #template = loader.get_template('pizza/index.html')
    #context ={'all_pizzas': all_pizzas}
    #return HttpResponse(template.render(context,request))

#OTRA FORMA DE HACER EL MÉTODO INDEX MAS OPTIMO

@login_required
def index(request):
    all_pizzas = Pizza.objects.all()
    #numero de visitas a esta vista,contadas como sesion variable
    num_visitas=request.session.get('num_visitas', 0)
    request.session['num_visitas'] = num_visitas+1
    context = {'all_pizzas': all_pizzas,'nombre_curso': 'Curso de Python','num_visitas':num_visitas}
    return render(request, 'pizza/index.html',context)



# esto si pongo otro id no da error, esta mal tiene que salir que no existe esa pizza
# def detail(request,pizza_id):
#     return HttpResponse("<h2>Detalles para la pizza id: " + str(pizza_id) + "</h2>")
# para solucionar el error hacemos otro metodo diferente

#def detail(request,pizza_id):
    #try:
        #pizza=Pizza.objects.get(pk=pizza_id)
    #except Pizza.DoesNotExist:
        #raise Http404("La pizza no existe")
    #return render(request,'pizza/detail.html' ,{'pizza' : pizza})
# hacerlo de otra forma el detail
def pizza_detail(request,pizza_id):
    pizza=get_object_or_404(Pizza, pk=pizza_id)
    return render(request, 'pizza/pizza_detail.html', {'pizza': pizza})
#deberes 
#1- crear album y song
#2. dentro de la carpeta musica creamos un virtual env, y activamos. instalamos django comando startproyect, creamos project de django, y creamos
#la app song. y hacemos todo lo que hemos hecho hoy.

class PizzasListView(LoginRequiredMixin, generic.ListView): #LoginRequiredMixin, es para loguearse al intentar ver la lista de pizzas
    model= Pizza

class PizzaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Pizza

def ingredientes_detail(request,ingredient_id):
    ingredient=get_object_or_404(Ingredient, pk=ingredient_id)
    return render(request, 'pizza/ingredient_detail.html',{'ingredient' : ingredient})

class IngredientListView(generic.ListView):
    model = Ingredient

class IngredientDetailView(generic.DetailView):
    model = Ingredient

#ahora empieza la clase del user form view apra hacer la vista del registro que se hace en forms.py

class UserFormView(View):
   form_class = UserForm
   template_name = 'pizza/register.html'

   #Display blank template
   def get(self, request):
       form = self.form_class(None)
       return render(request, self.template_name, {'form': form})
   
   def post(self, request):
       form = self.form_class(request.POST)
       
       if form.is_valid():
           user = form.save(commit=False)

           #Normalize the data
           email = form.cleaned_data['email']
           username = form.cleaned_data['username']            
           password = form.cleaned_data['password']
           user.set_password(password)
           user.save()

           #returns user object if credentials are correct
           user = authenticate(username= username, password= password)

           if user is not None:
               if user.is_active:
                   login(request, user)
                   return redirect('pizza:index')
           return render(request, self.template_name, {'form': form })

class PizzaCreate(LoginRequiredMixin, CreateView): #estamos creando una clase, pero es un método. Usa el modelo de pizza, pero en formulario, voy a usar todos los campos que hay en el modelo de pizza
    model = Pizza
    fields = '__all__'

class PizzaUpdate(LoginRequiredMixin, UpdateView): 
    model = Pizza
    fields = '__all__'

class PizzaDelete(LoginRequiredMixin, DeleteView): 
    model = Pizza
    def get_success_url(self):
        return reverse('pizza:index')


