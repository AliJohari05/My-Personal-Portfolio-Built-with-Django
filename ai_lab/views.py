from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import AICreation
# Create your views here.
def ai_lab_page(request):
    ai_list = AICreation.objects.all().order_by('-created_on')
    paginator = Paginator(ai_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'ai_lab/ai_lab.html', context)
def ai_lab_detail(request, ai_lab_id):
    ai_creation = get_object_or_404(AICreation, id=ai_lab_id)
    context = {'ai_creation': ai_creation}
    return render(request, 'ai_lab/ai_lab_detail.html', context)