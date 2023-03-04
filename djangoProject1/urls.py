
from django.contrib import admin
from django.urls import path
from devises.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('days=<int:user_delta>&currencies=<str:user_devise>', dashboard, name='dashboard')
]
