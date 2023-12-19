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

def kelner_menu(request):
    return render(request, 'Users/kelner_menu.html')

def kelner_add_order(request):
    return render(request, 'Users/kelner_add_order.html')

def kelner_index(request):
    return render(request, 'Users/kelner_index.html')

def kelner_login(request):
    return render(request, 'Users/kelner_login.html')

def kelner_map(request):
    return render(request, 'Users/kelner_map.html')

def kelner_receipt(request):
    return render(request, 'Users/kelner_receipt.html')

def kelner_go_back_action(request):
    return render(request, 'Users/kelner_index.html')
