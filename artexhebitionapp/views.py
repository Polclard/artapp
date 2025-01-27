from django.shortcuts import render, redirect

from artexhebitionapp.forms import ArtForm
from artexhebitionapp.models import Art


# Create your views here.

def index(request):
    arts = Art.objects.filter()
    return render(request, 'index.html', {'arts': arts})


def edit_art(request, id):
    art_instance = Art.objects.filter(id=id).first()
    if request.method == "POST":
        art = ArtForm(request.POST, instance=art_instance)
        if art.is_valid():
            art.save()
        return redirect("index")
    else:
        repair = ArtForm(instance=art_instance)
    return render(request, "edit_art.html", {"form": repair})
