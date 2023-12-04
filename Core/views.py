from django.shortcuts import render

def index(request):
    return render(request, 'Core/index.html')

def call_page(request):
    return render(request, 'Core/call_page.html')

def go_back_action(request):
    return render(request, 'Core/index.html')

def menu_page(request):
    return render(request, 'Core/menu_page.html')

def newsletter_page(request):
    return render(request, 'Core/newsletter_page.html')


