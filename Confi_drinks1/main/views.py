from django.shortcuts import render
from django.http import HttpResponse
from .forms import create_Coctail
from .models import ingredients



def main(request):
    return render(request,'main/main2.html')

def cm(request):
    ings = ingredients.objects.order_by("name")
    ing = {
        'ings': ings
    }

    if request.method == "POST":
        create = create_Coctail(request.POST)
        if create.is_valid():
            create.save()
            
    create = create_Coctail
    data = {
        "create": create
    }
    return render(request,'main/coctails_make.html', data, ing)

def search_of_ingrid(request):
    return render(request, "main/search_of_ingrid.html")

def prof(request):
    return render(request, "main/my_profile.html")

def coctail_info(request):
    return render(request, "main/coctail_info.html")