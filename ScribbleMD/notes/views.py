# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from markdown2 import Markdown
from models import Note
from forms import NewNote


def index(request):
    if 'username' not in request.session:
        return HttpResponseRedirect('../users')
    data = [ i for i in Note.objects.all() if i.owner == request.session['username']]
    context = dict()
    context['username'] = request.session['username']
    context['data'] = data
    temp = loader.get_template('notes/index.html')
    return HttpResponse(temp.render(context, request))


def new_note(request):
    if request.method == 'POST' and 'b2' in request.POST :
        form = NewNote(request.POST)
        if form.is_valid():
            new = Note()
            new.owner = request.session['username']
            new.head = form.cleaned_data["heading"]
            new.content = form.cleaned_data["content"]
            con = Markdown()
            new.md = con.convert(new.content)
            new.save()
            return HttpResponseRedirect("./")
    if request.method == 'POST' and 'b1' in request.POST :
        form = NewNote(request.POST)
        if form.is_valid():
            con=Markdown()
            request.session['temp'] = con.convert(form.cleaned_data['content'])
            return HttpResponseRedirect('preview')

    context = dict()
    context['form'] = NewNote()
    temp = loader.get_template('notes/newnote.html')
    return HttpResponse(temp.render(context, request))


def preview(request):
    context=dict()
    context['note'] = request.session['temp']
    request.session['temp'] = ''
    temp = loader.get_template('notes/preview.html')
    return HttpResponse(temp.render(context, request))

def view(request, note_id):
    try:

        note = Note.objects.filter(id=note_id)[0]
    except:
        return HttpResponse('404 Thats an Error!!<br><hr>', status=404)
    if note.owner!=request.session['username']:
        return HttpResponse('Unauthorized', status=401)
    context = dict()
    context['head'] = note.head
    context['body'] = note.md
    temp = loader.get_template('notes/view.html')
    return HttpResponse(temp.render(context,request))


def edit(request, note_id):
    if request.method == 'POST':
        try:

            note = Note.objects.filter(id=note_id)[0]

        except:

            return HttpResponse('404 Thats an Error!!<br><hr>', status=404)
        if note.owner != request.session['username']:
            return HttpResponse('Unauthorized', status=401)
        form = NewNote(request.POST)
        if form.is_valid():
            note.head = form.cleaned_data['heading']
            note.content = form.cleaned_data['content']
            con = Markdown()
            note.md = con.convert(note.content)
            note.save()

    try:

        note = Note.objects.filter(id=note_id)[0]

    except:
        return HttpResponse('404 Thats an Error!!<br><hr>', status=404)
    if note.owner!=request.session['username']:
        return HttpResponse('Unauthorized', status=401)
    data = dict()
    data['heading'] = note.head
    data['content'] = note.content

    form = NewNote(data)
    context = dict()
    context['form'] = form
    temp = loader.get_template('notes/edit.html')
    return HttpResponse(temp.render(context, request))


def delete(request, note_id):
    try:

        note = Note.objects.filter(id=note_id)[0]

    except:
        return HttpResponse('404 Thats an Error!!<br><hr>', status=404)
    if note.owner!=request.session['username']:
        return HttpResponse('Unauthorized', status=401)
    Note.objects.filter(id=note_id).delete()


def logout(request):
    request.session.pop('username')
    return HttpResponseRedirect('./users')

