from django.shortcuts import render
from dothack2022_app.forms import Newstudform
# Create your views here.

def thankyou(request):
    return render(request, 'dothack2022_app/thanks.html')

def reg_form(request):
    form = Newstudform()
    if request.method == 'POST':
        form = Newstudform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = Newstudform()
            return thankyou(request)
    return render(request, 'dothack2022_app/forms.html', {'form': form})
