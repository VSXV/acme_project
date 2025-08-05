from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import CustomUserCreationForm

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('birthday/', include('birthday.urls')),
    path(
        'auth/registration/', 
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,  # <-- используем кастомную форму
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
]
