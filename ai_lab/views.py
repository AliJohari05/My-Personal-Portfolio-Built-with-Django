from django.shortcuts import render,get_object_or_404

from .models import AICreation
# Create your views here.
def ai_lab_page(request):
    ai_creations = AICreation.objects.all()
    context = {'ai_creations': ai_creations}
    return render(request, 'ai_lab.html', context)
def ai_lab_detail(request, ai_lab_id):
    ai_creation = get_object_or_404(AICreation, id=ai_lab_id)
    context = {'ai_creation': ai_creation}
    return render(request, 'ai_lab_detail.html', context)