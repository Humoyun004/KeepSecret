from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Question, Comment
from .forms import QuestionForm, CommentForm
from django.db.models import Q

# Create your views here.
def Home(request):
    question = Question.objects.all()
    comment = Comment.objects.filter()
    return render(request, 'queries/index.html', context={'questions': question, 'comments': comment})


@login_required(login_url='/quests')
def QuestionAdd(request,question_p_id=None):
    question_p = None
    if question_p_id:
        question_p = Question.objects.get(id=question_p_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.user = request.user
            new_question.question_p = question_p
            new_question.save()
            return redirect('Home')
    else:
        form = QuestionForm()

    comment = Comment.objects.filter(question=question_p) if question_p else None

    return render(request, 'queries/questionAdd.html', context={'forms': form, 'question_p': question_p, 'comment': comment})


@login_required(login_url='/quests')
def CommentAdd(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    comments = Comment.objects.filter(question=question)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.question = question
            new_comment.save()

            question.comment_count = comments.count()
            question.save()

            return redirect('Home')
    else:
        form = CommentForm()

    return render(request, 'queries/commentAdd.html', {'question': question, 'comments': comments, 'form': form})

def Questions(request):
    questions = Question.objects.all()
    return render(request, 'queries/quests.html', {'questions': questions})

def Search(request):
    if request.method == 'POST':
        search_result = request.POST['searched']
        result = Question.objects.filter(Q(text__icontains=search_result) | Q(user__username__icontains=search_result))
        return render(request, 'queries/index.html', {'questions': result})
    else:
        return render(request, 'queries/index.html')


def Like(request, pk):
    question = get_object_or_404(Question, id=pk)
    if request.user in question.like.all():
        question.like.remove(request.user)
    else:
        question.like.add(request.user)
    return HttpResponseRedirect('/')


def Hashtag(request, hashtag):
    questions = Question.objects.filter(hashtag=hashtag)
    return render(request, 'queries/index.html', context={'questions': questions, 'hashtag': hashtag})








