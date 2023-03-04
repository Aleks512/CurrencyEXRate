
from django.contrib import admin
from django.urls import path
from devises.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('days=<int:days_range>&currencies=<str:currencies>', dashboard, name='dashboard')
]
