from django.shortcuts import render, redirect

# Create your views here.
from . import models

def index (req):

    task = models.Task.objects.all()
    return render(req, 'task/index.html', {
        'data': task,
    })

def input (req):
    if req.POST:
        models.Task.objects.create(name=req.POST['name'], genre=req.POST['genre'], artis=req.POST['artis'], th=req.POST['th'], lirik=req.POST['lirik'], link=req.POST['link'])
        return redirect('/')

    task = models.Task.objects.all()
    return render(req, 'task/input.html', {
        'data': task,
    })

def inputmovie (req):
    if req.POST:
        models.Movie.objects.create(title=req.POST['title'], gen=req.POST['gen'], rate=req.POST['rate'], years=req.POST['years'], des=req.POST['des'])
        return redirect('/')

    task = models.Movie.objects.all()
    return render(req, 'task/input_mov.html', {
        'data': task,
    })

def detail(req, id):
    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/detail.html', {
        'data': task,
    })

def detailmovie(req, id):
    task = models.Movie.objects.filter(pk=id).first()
    return render(req, 'task/detail_mov.html', {
        'data': task,
    })

def delete(req, id):
    models.Task.objects.filter(pk=id).delete()
    return redirect('/')

def deletemovie(req, id):
    models.Movie.objects.filter(pk=id).delete()
    return redirect('/')

def update (req, id):
    if req.POST:
        task = models.Task.objects.filter(pk=id).update(name=req.POST['name'], genre=req.POST['genre'], artis=req.POST['artis'], th=req.POST['th'], lirik=req.POST['lirik'], link=req.POST['link'])
        return redirect('/')

    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/update.html', {
        'data': task,
    })

def updatemovie (req, id):
    if req.POST:
        task = models.Movie.objects.filter(pk=id).update(title=req.POST['title'], gen=req.POST['gen'], rate=req.POST['rate'], years=req.POST['years'], des=req.POST['des'])
        return redirect('/')

    task = models.Movie.objects.filter(pk=id).first()
    return render(req, 'task/update_mov.html', {
        'data': task,
    })


