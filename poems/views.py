from django.shortcuts import render
from .models import Poem
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    poems = Poem.objects.all().order_by('-pk')
    context = {
        'poems': poems
        }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def poem_detail(request, id):
    poem = get_object_or_404(Poem, pk=id)
    context = {
        'poem': poem
        }
    return render(request, 'poem_detail.html', context)
