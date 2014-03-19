# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from survey.models import Member
from survey.models import Relation
import uuid
def index(request):
  return render_to_response('index.html', {},
     context_instance=RequestContext(request))
def makesun(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    post_email = request.POST['email']
    post_address = request.POST['address']
    post_income = request.POST['income']
    post_profession = request.POST['profession']
    post_homeValue = 0 
    post_squareFootage = 0
    if request.POST.get('homevalue',0):
        post_homeValue = request.POST['homevalue']
    if request.POST.get('squareFootage',0):
        post_squareFootage = request.POST['squarefootage']
    energyList = request.POST.getlist('energy[]')
    post_memberType = "S"
    energyString = ",".join(energyList)
    m = Member(memberId= uuid.uuid4(), firstName = first_name, lastName=last_name, email=post_email, address=post_address, income=post_income,profession=post_profession,homeValue=post_homeValue, 
        squareFootage=post_squareFootage, memberType=post_memberType,adoption=energyString)
    m.save();
    return render_to_response('graph.html', {"sun":m.memberId},context_instance=RequestContext(request))
def makeplanet(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    post_email = request.POST['email']
    post_address = request.POST['address']
    post_income = ""
    post_profession = request.POST['profession']
    post_frequency = 0 
    if request.POST.get('frequency',0):
        post_frequency = request.POST.get('frequency')
    post_homeValue = 0 
    post_squareFootage = 0
    conversationList = request.POST.getlist('conversation[]')
    post_memberType = "F"
    conversationString = ",".join(conversationList)
    post_sunId = request.POST['sunid']
    post_trustLevel = request.POST['trust']
    post_actualRingLevel = 0
    for key in request.POST:
        value = request.POST[key]
        print value
    energyString=""
    m = Member(memberId= uuid.uuid4(), firstName = first_name, lastName=last_name, email=post_email, address=post_address, income=post_income,profession=post_profession,homeValue=post_homeValue, 
     squareFootage=post_squareFootage, memberType=post_memberType,adoption=energyString)
    m.save();
    relation = Relation(sunId = post_sunId, friendId = m.memberId, trustLevel = post_trustLevel, frequency = post_frequency, conversationTopic = conversationString, actualRingLevel = post_actualRingLevel)
    relation.save()
    return HttpResponse("Success")