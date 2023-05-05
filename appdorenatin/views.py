from django.shortcuts import render, redirect
from .models import Nacional
from .models import Artilheiro

def home(request):
  nacional = Nacional.objects.all()
  artilheiro = Artilheiro.objects.all()
  context = { "nacional": nacional , "artilheiro": artilheiro }
  return render(request, "RenatoRibeiro.html", context=context)

def create_artilheiro(request):
  if request.method == "POST":
    Artilheiro.objects.create(
      nome=request.POST["Nome"],
      jogos=request.POST["Jogos"],
      gols=request.POST["Gols"],
      titulos=False
    )
    return redirect("principal")
  
  return render(request, "artilheiro_form.html")

def create_nacional(request):
  if request.method == "POST":
    Nacional.objects.create(
      title=request.POST["Title"],
      ano=request.POST["Ano"],
      tipo=request.POST["Tipo"],
      invicto=False
    )
    return redirect("principal")
  
  return render(request, "nacional_form.html")

def update_artilheiro(request, artilheiro_id):
  artilheiro = Artilheiro.objects.get(id=artilheiro_id)
  if request.method == "POST":
    artilheiro.nome = request.POST["Nome"]
    artilheiro.jogos = request.POST["Jogos"]
    artilheiro.tipo = request.POST["Gols"]
    if "Títulos" not in request.POST:
      artilheiro.titulos = False
    else:
      artilheiro.titulos = True
    artilheiro.save()
    return redirect("principal")

  return render(request, "artilheiro_form.html", context={"artilheiro": artilheiro})

def update_nacional(request, nacional_id):
  nacional = Nacional.objects.get(id=nacional_id)
  if request.method == "POST":
    nacional.title = request.POST["Title"]
    nacional.ano = request.POST["Ano"]
    nacional.tipo = request.POST["Tipo"]
    if "Invicto" not in request.POST:
      nacional.invicto = False
    else:
      nacional.invicto = True
    nacional.save()
    return redirect("principal")

  return render(request, "nacional_form.html", context={"nacional": nacional})

def delete_artilheiro(request, artilheiro_id):
    artilheiro = Artilheiro.objects.get(id=artilheiro_id)
    if request.method == "POST":
      if "confirma" in request.POST:
        artilheiro.delete()
      return redirect("principal")

    return render(request, "delete_artilheiro.html", context={"artilheiro": artilheiro})

def delete_nacional(request, nacional_id):
    nacional = Nacional.objects.get(id=nacional_id)
    if request.method == "POST":
      if "confirma" in request.POST:
        nacional.delete()
      return redirect("principal")

    return render(request, "delete_nacional.html", context={"nacional": nacional})