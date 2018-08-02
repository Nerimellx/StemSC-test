# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from .models import *
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import AddForm
from django.db.models import Q



def main(request):
    title = 'Primary'

    humans = Human.objects.all()

    content = {
        'title' : title,
        'humans' : humans
    }

    return render(request, 'index.html', content)


def delete(request, number):
    human = get_object_or_404(Human, id = number)
    human.delete()
    return HttpResponseRedirect('/')


def add(request):
    endpoint = 'https://maps.googleapis.com/maps/api/geocode/json?'
    api_key = 'AIzaSyBeVeatzzWO7Cy2-rIPgxcDPFeoVo_ss0g'
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            post = form.save()
            address = request.POST.get('address').replace(' ', '+')
            finishpoint = 'address={}&key={}&sensor=false&language=ru'.format(address, api_key)
            req = endpoint + finishpoint
            response = requests.get(req)
            request = response.json()
            post.address = request['results'][0]['formatted_address']
            post.lat = request['results'][0]['geometry']['bounds']['northeast']['lat']
            post.lon = request['results'][0]['geometry']['bounds']['northeast']['lng']
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = AddForm()
    return render(request, 'create.html', {'form': form})


def edit(request, number):
    human = get_object_or_404(Human, id = number)
    endpoint = 'https://maps.googleapis.com/maps/api/geocode/json?'
    api_key = 'AIzaSyBeVeatzzWO7Cy2-rIPgxcDPFeoVo_ss0g'
    if request.method == 'POST':
        form = AddForm(request.POST, instance = human)
        if form.is_valid():
            post = form.save()
            address = request.POST.get('address').replace(' ', '+')
            finishpoint = 'address={}&key={}&sensor=false&language=ru'.format(address, api_key)
            req = endpoint + finishpoint
            response = requests.get(req)
            request = response.json()
            post.address = request['results'][0]['formatted_address']
            post.lat = request['results'][0]['geometry']['location']['lat']
            post.lon = request['results'][0]['geometry']['location']['lng']
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = AddForm(instance = human)
    return render(request, 'create.html', {'form': form})


def search(request):
    title = 'Результаты поиска'
    if request.method == 'POST':
        question = request.POST.get('q')
        result = Human.objects.filter(Q(firstName=question) | Q(lastName=question) | Q(address=question) | Q(phone_number=question))
        content = {
            'humans':result,
            'title':title,
        }
        return render(request,'index.html', content)



