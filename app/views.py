from django.shortcuts import render
from .llms import chain
# Create your views here.

def home(request):
    response = None
    if request.method == 'POST':
        user_input = request.POST['query']
        response = chain.invoke(user_input)
        response
    return render(request, 'app/home2.html', {'response':response})


