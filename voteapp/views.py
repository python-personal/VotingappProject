from django.shortcuts import render,get_object_or_404
from .models import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

# Create your views here.
def HomeView(request):
    return render(request,'voteapp/home.html')

def QuestionView(request):
    questions=Question.objects.order_by('-pub_date')[:5]
    return render(request,'voteapp/questions.html',{'questions':questions})

def QuestionDetailView(request,id):
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'voteapp/question_detail.html', { 'question': question })

def resultsView(request,id):
    question=get_object_or_404(Question,id=id)
    return render(request,'voteapp/results.html',{'question':question})

def VoteView(request,id):
    question = Question.objects.get(pk=id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'voteapp/question_detail.html',{'question':question,'error_msg':'Please select the proper choice'})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results',args=(question.id,)))

def resultsData(request,obj):
    votesdata=[]
    question=Question.objects.get(id=obj)
    votes=question.choice_set.all()
    for i in votes:
        votesdata.append({i.choice_text:i.votes})
    return JsonResponse(votesdata,safe=False)
