from django.shortcuts import render, redirect
import api

# Create your views here.
def redirect_home(request):
    return redirect("dashboard", user_delta=30, user_devise="USD,PLN")


def dashboard(request, user_delta = 60, user_devise="CAD"):
    days, rates = api.get_rates(currencies=user_devise.split(","), days=user_delta)
    days_label = {7: "Semaine",30: "Mois", 365: "Année"}.get(user_delta, "Personalisé")
    return render(request,'devises/index.html', context={'data': rates, # axe y de chart
                                                         'days_labels': days, # axe x de chart
                                                         'user_devise_btn':user_devise, #for value buttons
                                                         'days_label': days_label})# titre dynamique
