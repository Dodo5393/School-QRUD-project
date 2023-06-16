from django.shortcuts import render ,  redirect
from django.http import HttpResponse
from django.template import loader
from .models import Animal , Food , Positions , JobApplication
from .forms import JobApplicationForm
from django.urls import reverse


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def about(request):
    return render(request, 'about.html')

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animal_list.html', {'animals': animals})

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods})

def positions_list(request):
    positions = Positions.objects.all()
    return render(request, 'positions_list.html', {'positions': positions})

def search_results(request):
    query = request.GET.get('query')  
    results = Animal.objects.filter(name__icontains=query)

    return render(request, 'search_results.html', {'results': results})

def job_application(request, position_id):
    position = Positions.objects.get(id=position_id)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.position = position
            job_application.save()
            return render(request, 'application_success.html')
    else:
        form = JobApplicationForm()

    context = {
        'form': form,
        'position': position
    }
    return render(request, 'job_application.html', context)