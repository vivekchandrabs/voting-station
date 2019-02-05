from django.shortcuts import render,redirect
from polling.models import Question,Choice

# Create your views here.

def question(request):

	question = Question.objects.all().first()
	choice_set = Choice.objects.filter(question = question)
	return render(request, "index.html", {'question':question, "choice_set":choice_set})

def answer(request, questionid):

	question = Question.objects.get(pk = questionid)
	choiceid = request.POST.get("vote")
	choice = Choice.objects.get(pk = choiceid, question=question)
	choice.votes+=1
	choice.save()
	return redirect('/thankyou/')

def thankyou(request):
	return render(request, "thankyou.html")




