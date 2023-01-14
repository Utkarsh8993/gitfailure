from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth import get_user_model


from .forms import Candidateform
from .models import Candidate 
from users.models import User
User = get_user_model()
# Create your views here.

def home(request):
    return render(request, "elections/homepage.html", {})


def addcandidate(request):
    
    if request.method=="POST":
        if request.user.is_authenticated:
            form=Candidateform(request.POST, request.FILES)
            if form.is_valid:
                form.save()
                candidate=Candidate.objects.get(name=request.POST["name"])
                if  candidate.email == request.user.email :
                    messages.success(request, "You are now a candidate")
                    return redirect('home')
                else :
                    messages.success(request , "This is not you!! , Please enter your login email")
                    return redirect('addcandidate')
            else:
                messages.success(request , "Please enter valid information.")
                return redirect('addcandidate')

        else:
            messages.success(request , "Please login first.")                        
            return redirect('login')
    else:
        form=Candidateform()
        return render(request, "elections/Newcandidate.html",{
                "form":form     
        })
                    


def vote1(request, candidate_id):
    candidate=Candidate.objects.get(pk=candidate_id)
    voter=request.user
    if not voter.vote_1_bool:
        candidate.votes+=3
        voter.vote_1_bool=True
        candidate.save()
        voter.save()
        messages.success(request , "Vote for your second preferance now")
    else: 
        messages.success(request , "You have voted for this Preferance")
    return render(request, "elections/candidates.html",{})

def vote2(request, candidate_id):
    
    candidate = Candidate.objects.get(pk=candidate_id)
    voter = request.user
    if not voter.vote_2_bool:
        candidate.votes+=3
        voter.vote_2_bool=True
        candidate.save()
        voter.save()
    else:
        messages.success(request , "You have voted for this Preferance")
    return render(request, "elections/candidates.html",)

def vote3(request, candidate_id):
    candidate=Candidate.objects.get(pk=candidate_id)
    voter=request.user
    if not voter.vote_3_bool:
        candidate.votes += 1
        voter.vote_3_bool=True
        candidate.save()
        voter.save()
    else:
        messages.success(request , "You have voted for this Preferance")
    return render(request, "elections/candidates.html",)

def all_candidates(request):
    candidates=Candidate.objects.all()
    return render(request, "elections/candidates.html",{
        "candidates":candidates
    })

def show_candidate(request, candidate_id):
    candidate=Candidate.objects.get(pk=candidate_id)
    return render(request, "elections/candidate.html",{
        "candidate":candidate
    })






def result(request):
    branch = request.user.branch
    all_candidates= Candidate.objects.filter(branch = branch)
    votes=[]
    for cand in all_candidates:
        v=cand.votes
        votes.append(v)

    winner_votes=max(votes)
    winner_candidates=Candidate.objects.filter(votes=winner_votes)
    return render(request, "elections/result.html",{
        "winner_votes":winner_votes,
        "winner_candidates":winner_candidates,
        
    })    


def update(request, candidate_id):
    candidate=Candidate.objects.get(pk=candidate_id)
    if request.method == "POST": 
        form = Candidateform(request.POST or None ,  instance=candidate)
        if form.is_valid():
            form.save()
            return render(request, "elections/candidates.html",)
    else:
        form = Candidateform(instance=candidate)
        return render(request , "elections/Newcandidate.html", {
            "form" : form
        } )



            