from django.shortcuts import render
from .models import HealthData
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import CaloriesForm

appname = 'Smartwatch App'

def health_data_form(request):
    calories = None

    met_values = {
        'walking': 3.8,
        'running': 9.8,
        'cycling': 8.0,
        'swimming': 7.0,
        'yoga': 3.0,
    }
    if request.method == 'POST':
        form = CaloriesForm(request.POST)
        if form.is_valid():
            
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            duration = form.cleaned_data['duration']
            exercise = form.cleaned_data['exercise']

            met_value = met_values.get(exercise, 1)
            calories = (met_value * weight * duration) / 60
            HealthData.objects.create(
                age=age,
                weight=weight,
                duration=duration,
                exercise=exercise,
                calories_burned=calories
            )
            return redirect('health_data_form')

    else:
        form = CaloriesForm()

    return render(request, 'list.html', {'form': form, 'calories': calories,'appname':appname})



