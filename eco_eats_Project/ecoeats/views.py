from django.shortcuts import render
from ecoeats.forms import FeedbackForm

# Create your views here.
from django.http import HttpResponse
from rango.models import Feedback

def index(request):
   
    return render(request, 'ecoeats/index.html')

def add_feedback(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            # Now call the login() view.
            # The user will be shown the homepage.
            return login(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = FeedbackForm()

    
    feedback_list = Feedback.objects.order_by('-created_at')
    context_dict = {'feedbacks': feedback_list}

    # Render the response and send it back!
    
    return render(request, 'ecoeats/feedback.html', {'form': form}, context_dict)