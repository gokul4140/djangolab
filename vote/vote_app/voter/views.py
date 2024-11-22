from django.shortcuts import render
from datetime import date
from .forms import VoterForm
from .models import Voter

def voter_application(request):
    message = None

    if request.method == "POST":
        form = VoterForm(request.POST)
        if form.is_valid():
            dob = form.cleaned_data['dob']
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            
            if age >= 18:
                form.save()
                message = "Success: Application submitted!"
            else:
                message = "Not eligible: Age must be at least 18."

    else:
        form = VoterForm()

    return render(request, 'voter/index.html', {'form': form, 'message': message})
