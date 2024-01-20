from django.shortcuts import render

codes_list = ["4ZN52", "77JRE", "QYFNA", "2KK9B", "B7GEG", "998ZK"]

# Mapowanie kodów do numerów stolików
code_to_table_map = {code: index + 1 for index, code in enumerate(codes_list)}

def index(request):
    # Przykład wykorzystania wartości z sesji w widoku 'index'
    code = request.session.get('user_code', '')
    return render(request, 'Core/index.html', {'code': code})

def user(request):
    code = request.GET.get('code', '')
    if code:
        request.session['user_code'] = code  # Zapisz kod w sesji jeśli jest dostępny
        table_number = code_to_table_map.get(code)
    else:
        code = request.session.get('user_code', '')  # Pobierz kod z sesji jeśli nie ma go w URL
        table_number = code_to_table_map.get(code, None)
    return render(request, 'Core/user.html', {'code': code, 'table_number': table_number})

def call_page(request):
    code = request.session.get('user_code', '')  # Pobierz kod z sesji
    return render(request, 'Core/call_page.html', {'code': code})

def go_back_action(request):
    code = request.session.get('user_code', '')  # Pobierz kod z sesji
    return render(request, 'Core/index.html', {'code': code})

def menu_page(request):
    code = request.session.get('user_code', '')  # Pobierz kod z sesji
    return render(request, 'Core/menu_page.html', {'code': code})

def newsletter_page(request):
    code = request.session.get('user_code', '')  # Pobierz kod z sesji
    return render(request, 'Core/newsletter_page.html', {'code': code})


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
