from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib import messages 
from .forms import CustomUserChangeForm


from .models import Election , Candidate

def home(request):
    elections = Election.objects.all()
    return render(request, 'home.html', {'elections': elections})

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Election, Candidate

def election_detail(request, election_id):
    election = get_object_or_404(Election, id=election_id)

    # Check if the election status is 'upcoming'
    if election.status == 'upcoming':
        return HttpResponse("This Election is not available yet. Please check back later.")

    candidates = Candidate.objects.filter(election=election)
    return render(request, 'election_detail.html', {'election': election, 'candidates': candidates})

from .models import BlockchainCode
from .blockchain import create_blockchain_code  # Import the create_blockchain_code function
from .models import BlockchainCode

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import BlockchainCode, Candidate

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Election, Candidate, BlockchainCode

def vote(request, election_id, candidate_id):
    user = request.user
    candidate = get_object_or_404(Candidate, id=candidate_id)

    # Check if the election is completed
    election = get_object_or_404(Election, id=election_id)
    if election.status == 'completed':
        return HttpResponse("Voting for this election has ended. You can no longer vote.")

    # Check if the user has already voted in this election
    if BlockchainCode.objects.filter(user=user, candidate__election=election).exists():
        return HttpResponse("You have already voted in this election.")

    # Create a blockchain code for the vote
    blockchain_code = create_blockchain_code(user, candidate)

    # Save the blockchain code in the database
    blockchain_entry = BlockchainCode(user=user, candidate=candidate, blockchain_code=blockchain_code)
    blockchain_entry.save()

    return HttpResponse("Your vote has been recorded with blockchain code: " + blockchain_code)

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('home')

def custom_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})




@login_required
def update_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')  # Add a success message
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'update_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'change_password.html', {'form': form})


from django.shortcuts import render
from django.http import HttpResponse
from .models import Election, BlockchainCode, Candidate
from collections import Counter

from django.shortcuts import render, get_object_or_404
from .models import Election, BlockchainCode, Candidate
from collections import Counter

def election_winners(request):
    user = request.user

    # Get a list of all completed elections
    completed_elections = Election.objects.filter(status='completed')

    # Check if the user has voted in these elections and find the winners
    election_winners = []
    for election in completed_elections:
        has_voted = BlockchainCode.objects.filter(user=user, candidate__election=election).exists()

        if has_voted:
            candidates = Candidate.objects.filter(election=election)

            # Count the votes for each candidate in the election
            candidate_votes = Counter(
                BlockchainCode.objects.filter(candidate__election=election).values_list('candidate_id', flat=True)
            )

            # Find the candidate with the most votes
            winner_candidate_id = candidate_votes.most_common(1)[0][0]
            winner_candidate = get_object_or_404(Candidate, id=winner_candidate_id)

            # Calculate the total votes for the winner candidate
            total_votes = candidate_votes[winner_candidate_id]

            election_winners.append({'election': election, 'winner_candidate': winner_candidate, 'total_votes': total_votes})

    return render(request, 'election_winner.html', {'election_winners': election_winners})
