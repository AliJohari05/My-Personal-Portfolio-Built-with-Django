from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import AICreation


def ai_lab_page(request):
    ai_list = AICreation.objects.all().order_by('-created_on')

    paginator = Paginator(ai_list, 6)
    try:
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(1)

    context = {
        'page_obj': page_obj
    }
    return render(request, 'ai_lab/ai_lab.html', context)


def ai_lab_detail(request, slug):
    ai_creation = get_object_or_404(AICreation, slug=slug)

    context = {
        'ai_creation': ai_creation
    }
    return render(request, 'ai_lab/ai_lab_detail.html', context)
