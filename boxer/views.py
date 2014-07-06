from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from models import Email


def index(request):
    emails = Email.objects.order_by('-id')
    return render(request, 'boxer/index.html', locals())

def delete(request):
    try:
        id = request.POST['id']
    except Exception, e:
        print e
        return HttpResponseBadRequest()
    email = get_object_or_404(Email, pk=id)
    email.delete()
    return HttpResponse('true', content_type='application/json')

#def email_detail(request, pk):
#    email = get_object_or_404(Email, pk=pk)
#    return render(request, 'boxer/email.html', locals())
