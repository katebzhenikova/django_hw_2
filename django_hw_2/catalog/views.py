from django.shortcuts import render


def home_page(request):
    return render(request, 'django_hw_2/home_page.html')


def info_page(request):
    return render(request, 'django_hw_2/info_page.html')



# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email}): {message}')
#     return render(request, 'django_hw_2/index.html')
