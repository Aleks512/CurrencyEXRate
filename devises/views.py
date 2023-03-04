from django.shortcuts import render, HttpResponse
import api

# Create your views here.
def dashboard(request, user_delta = 60, user_devise="CAD"):
    days, rates = api.get_rates(currencies=user_devise.split(","), days=user_delta)
    return render(request,'devises/index.html', context={'data': rates,
                                                         'days_labels': days})
