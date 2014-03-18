# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from survey.models import Member
import uuid
def index(request):
    return render_to_response('index.html', {},
                               context_instance=RequestContext(request))
def makemember(request):
    m = Member(firstName=request.POST['first'], lastName=request.POST['second'], email=request.POST['email'], memberId = uuid.uuid4())
    m.save();
    return HttpResponse("Successfully made the member")