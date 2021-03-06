# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from survey.models import Member
from survey.models import Relation
import uuid
import re
def index(request):
  return render_to_response('index.html', {},
     context_instance=RequestContext(request))
def start(request):
  return render_to_response('sun.html', {},
     context_instance=RequestContext(request))
def makesun(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    post_email = request.POST['email']
    try:
        m = Member.objects.get(email=post_email)
        return render_to_response('graph.html', {"sun":m.memberId,"sunname":m.firstName},context_instance=RequestContext(request))
    except Member.DoesNotExist:
        listing = None
    post_address = request.POST['address']
    formatted_num =  re.compile(r'[^\d.]+')
    post_income = formatted_num.sub('',request.POST['income'])
    post_profession = request.POST['profession']
    post_homeValue = 0 
    post_squareFootage = 0
    post_latitude = 0.0
    post_longitude = 0.0
    if request.POST.get('lat',0.0):
        post_latitude = request.POST['lat']
    if request.POST.get('lon',0.0):
        post_longitude= request.POST['lon']
    if request.POST.get('homevalue',0):
        post_homeValue = formatted_num.sub('',request.POST['homevalue'])
    if request.POST.get('squarefootage',0):
        post_squareFootage = formatted_num.sub('',request.POST['squarefootage'])
    energyList = request.POST.getlist('energy[]')
    post_memberType = "S"
    energyString = ",".join(energyList)
    m = Member(memberId= uuid.uuid4(), firstName = first_name, lastName=last_name, email=post_email, address=post_address, income=post_income,profession=post_profession,homeValue=post_homeValue, 
        squareFootage=post_squareFootage, memberType=post_memberType,adoption=energyString, latitude = post_latitude, longitude = post_longitude)
    m.save();
    return render_to_response('graph.html', {"sun":m.memberId,"sunname":m.firstName},context_instance=RequestContext(request))
def makeplanet(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    post_email = request.POST['email']
    post_sunId = request.POST['sunid']
    addMember = True
    foundRelation = False
    foundMember = None
    try:
        foundMember = Member.objects.get(email=post_email)
        addMember = False
        try:
            relation = Relation.objects.get(friendId=foundMember.memberId,sunId=post_sunId)
            foundRelation = True
        except Relation.DoesNotExist:
            relation = None
    except Member.DoesNotExist:
        listing = None
    post_address = request.POST['address']
    post_income = ""
    post_profession = request.POST['profession']
    post_frequency = "" 
    if request.POST.get('frequency',""):
        post_frequency = request.POST.get('frequency')
    post_homeValue = 0 
    post_squareFootage = 0
    conversationList = request.POST.getlist('conversation[]')
    post_memberType = "F"
    conversationString = ",".join(conversationList)
    post_trustLevel = request.POST['trust']
    post_actualRingLevel = 0
    for key in request.POST:
        value = request.POST[key]
        print value
    energyString=""
    if addMember == True:
        m = Member(memberId= uuid.uuid4(), firstName = first_name, lastName=last_name, email=post_email, address=post_address, income=post_income,profession=post_profession,homeValue=post_homeValue, 
            squareFootage=post_squareFootage, memberType=post_memberType,adoption=energyString, latitude = 0.0, longitude = 0.0)
        m.save();
        foundMember = m
    if foundRelation == False:
        print "Trying to add  a relation"
        print foundMember.firstName
        relation = Relation(sunId = post_sunId, friendId = foundMember.memberId, trustLevel = post_trustLevel, frequency = post_frequency, conversationTopic = conversationString, actualRingLevel = post_actualRingLevel)
        relation.save()
        print "Added a relation"
    return HttpResponse("Success")
def updateplanet(request):
    for key in request.POST:
        value = request.POST[key]
    print value
    post_email = request.POST['email']
    post_level = request.POST['level']
    m = Member.objects.get(email=post_email)
    r = Relation.objects.get(friendId = m.memberId) 
    r.actualRingLevel = post_level 
    r.save();
    return HttpResponse("Success")
