from django.shortcuts import render
from cbvapp.models import Cloth
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class ClothListView(ListView):
    model=Cloth

class ClothDetailView(DetailView):
    model=Cloth

class ClothCreateView(CreateView):
    model=Cloth
    fields=('name', 'color', 'size', 'price')

class ClothUpdateView(UpdateView):
    model=Cloth
    fields=('color', 'size', 'price')

class ClothDeleteView(DeleteView):
    model=Cloth
    success_url=reverse_lazy('home')
def contact_view(request):
    return render(request, 'cbvapp/contact.html')
