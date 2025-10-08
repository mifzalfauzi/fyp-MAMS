from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def redirect_home(request):
    return redirect('login')  # redirects to /login/

urlpatterns = [
    path('', redirect_home),  # redirect root to /login/
    path('admin/', admin.site.urls),

    # Include apps
    path('', include('authentication.urls')),
    path('', include('assistant.urls')),
    path('', include('administrator.urls')),
    path('', include('parent.urls')),
    path('', include('tickets.urls')),
    path('', include('teacher.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
