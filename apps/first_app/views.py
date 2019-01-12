from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    variables = {
        'people' : Person.objects.all()
    }
    return render(request, 'first_app/index.html', variables)

def vote(request):
    person = Person.objects.get(id=request.POST["person"])
    totalvote = int(request.POST["vote"])*int(request.POST["weight"])
    person.total_vote += totalvote
    person.people_voted += 1
    person.save()
    return redirect("/")

def view_votes(request):
    for p in Person.objects.all():
        if p.people_voted > 0:
            p.average_vote = int(p.total_vote / p.people_voted)
            p.save()
        else:
            p.average_vote = p.total_vote
            p.save()

    return redirect("/votes")

def see_votes(request):
    variables = {
        'people' : Person.objects.all()
    }
    return render(request, 'first_app/votes.html', variables)