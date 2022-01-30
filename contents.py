from django.shortcuts import render
from dothack2022_app.views import reg_form

hostel1 = 34
hostel2 = 30

def page1(request):
    return render(request, 'dothack2022_app/index.html')

def page2(request):
    return render(request, 'dothack2022_app/Beauxbatons.html')

def page3(request):
    return render(request, 'dothack2022_app/Hogwarts.html')

def page4(request):
    return render(request, 'dothack2022_app/girlsbeaxubatons.html')

def page5(request):
    return render(request, 'dothack2022_app/boysbeauxbatons.html')

def page6(request):
    return render(request, 'dothack2022_app/girlshogwarts.html')

def page7(request):
    return render(request, 'dothack2022_app/boyshogwarts.html')

def page8(request):
    global hostel1
    available_seats = hostel1
    hostel1 -= 1
    return render(request, 'dothack2022_app/hostel1.html', {'seats':available_seats})

def page9(request):
    global hostel2
    available_seats = hostel2
    hostel2 -= 1
    print(hostel2)
    return render(request, 'dothack2022_app/hostel2.html', {'seats':available_seats})

def page10(request):
    return reg_form(request)

def page11(request):
    return render(request, 'dothack2022_app/thanks.html')

  
