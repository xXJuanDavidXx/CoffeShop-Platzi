from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, logout


class CreateUser(CreateView):

    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy("lista")


    def get_context_data(self, **kwargs):
        """
        super(): Llama al método de la clase base (super) para obtener el contexto predeterminado que Django genera.
        context: Es un diccionario que almacena toda la información que pasará a la plantilla. Aquí es donde añadimos nuestros propios datos.
        kwargs: Son los argumentos adicionales que se le pasan a la función. En este caso, no los estamos modificando, pero podrían contener datos extra que provienen de la vista.
        """
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'signup'
        return context



    def form_valid(self, form):
        """
        super().form_valid(form): Llama al método base que procesa el formulario una vez que ha sido validado con éxito. Este paso normalmente guarda el nuevo usuario en la base de datos.
        form.cleaned_data: Es un diccionario que contiene los datos del formulario que han sido limpiados y validados. Aquí estamos accediendo a los datos del username y la password1 (que es la contraseña ingresada por el usuario).
        authenticate(username, password): Es una función de Django que verifica si los datos del usuario y la contraseña son correctos.
        login(self.request, user): Es otra función de Django que inicia sesión al usuario una vez que ha sido autenticado.

        """
        response = super().form_valid(form)  # Guarda al usuario en la base de datos utilizando la funcionalidad predeterminada.
        username = form.cleaned_data.get('username')  # Extrae el nombre de usuario del formulario validado.
        raw_password = form.cleaned_data.get('password1')  # Extrae la contraseña del formulario validado.
        user = authenticate(username=username, password=raw_password)  # Verifica las credenciales.
        login(self.request, user)  # Inicia sesión automáticamente al usuario si las credenciales son correctas.
        return response  # Retorna la respuesta original (redirecciona al 'success_url').


def singout(request):
    logout(request)
    return redirect('Login')


