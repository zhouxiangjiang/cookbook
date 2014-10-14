from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic

from vip.models import VIPUser


def index(request):
    context = {
        'id': 100,
    }
    return render(request, 'vip/index.html', context)
    
    
class IndexView(generic.ListView):
    '''
    @see https://docs.djangoproject.com/en/1.7/topics/class-based-views/
    '''
    template_name = 'vip/index.html'
    context_object_name = 'id'
    
    def get_queryset(self):
        return 1000
    

def detail(request, id):
    user = get_object_or_404(VIPUser, id=id)
    return HttpResponse("VIP's phone: {0}.".format(user.phone))
    
    
def result(request, id):
    return HttpResponse("You're looking at result of VIP {0}.".format(id))
