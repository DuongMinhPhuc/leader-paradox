from datetime import timedelta, datetime, timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Member

class Index(View):
    def get(self,request):
        members = Member.objects.all()
        today = datetime.now(timezone.utc)
        leader = Member()
        if today > members[len(members)-1].end:
            members = Index().generate(today)
            for i in members:
                i.save()
        for mem in members:
            if (mem.start <= today and mem.end >= today):
                leader = mem
        context = {
            'leader': leader,
            'members': members
        }
        return render(request,'leader/homepage.html',context)

    def post(self, request):
        startDate = request.POST.get('startDate')
        #.date()
        startDate = datetime.strptime(startDate,'%d-%m-%Y')
        members = Member.objects.all()
        for i in range(len(members)):
            if i == 0:
                members[i].start = startDate
                members[i].end = startDate + timedelta(days=7)
                members[i].save()
            else:
                members[i].start = members[i-1].end + timedelta(days=1)
                members[i].end = members[i].start + timedelta(days=7)
                members[i].save()

        return Index.get(self,request)

    def generate(self,day):
        members = Member.objects.all()
        for i in range(len(members)):
            if i == 0:
                members[i].start = day
                members[i].end = day + timedelta(days=7)
                members[i].save()
            else:
                members[i].start = members[i-1].end + timedelta(days=1)
                members[i].end = members[i].start + timedelta(days=7)
                members[i].save()
        return members

class addMember(View):
    def get(self, request):
        return render(request, 'leader/index.html')

    def post(self,request):
        name = request.POST.get('name')
        members = Member.objects.all()
        newmem = Member(name=name)
        newmem.start = members[len(members)-1].end + timedelta(days=1)
        newmem.end = newmem.start + timedelta(days=7)
        newmem.save()
        return HttpResponseRedirect('')






