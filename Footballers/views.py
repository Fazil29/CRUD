from django.shortcuts import render, HttpResponse, redirect
from Footballers.models import Footballers as fb
from Footballers.forms import FootballerForm as ff


def entry(request):
    if request.method == "POST":
        form = ff(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/")
            except:
                pass
        else:
            print("NotValid===================================")
    else:
        form = ff()
    return render(request, "entry.html", {'form': form})


def show(request):
    footballers = fb.objects.all()
    return render(request, 'show.html', {'footballers': footballers})


def delete(request, id):
    footballer = fb.objects.get(F_id=id)
    footballer.delete()
    return redirect("/")


def edit(request, id):
    footballer = fb.objects.get(F_id=id)
    return render(request, 'edit.html', {"footballer": footballer})


def update(request, id):
    footballer = fb.objects.get(F_id=id)
    form = ff(request.POST or None, instance=footballer)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {"form": form})
