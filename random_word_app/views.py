from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    request.session['counter'] = 1
    request.session['word'] = get_random_string(length=14)
    return render(request, 'index.html')

def random(request):
    request.session['counter']
    request.session['word']
    return render(request, 'random.html')

def handle_random(request):
    request.session['counter'] += 1
    return redirect('/random')

def reset_random(request):
    request.session.flush()
    return redirect('/')