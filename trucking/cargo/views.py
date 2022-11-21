import datetime
from django.shortcuts import render, redirect
from .models import Request, Review
from .forms import AddRequest, AddUserForm
from django.contrib.auth.decorators import permission_required
from .forms import RegistrForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


def add_request(request):

    if request.method == 'POST':

        form = AddRequest(request.POST, request.FILES)

        if form.is_valid():
            new_request = Request()
            new_request.date = datetime.datetime.now()
            new_request.name = form.cleaned_data['name']
            new_request.surname = form.cleaned_data['surname']
            new_request.email = form.cleaned_data['email']
            new_request.company = form.cleaned_data['company']
            new_request.message = form.cleaned_data['message']
            new_request.save()
            return redirect('message_success')

    elif request.method == "GET":
        form = AddRequest()

    return render(request, 'add_request.html', {'form': form})


def message(request):
    success = Request.objects.last
    viewed_message = request.session.get("viewed_message",[])
    return render(request, 'message_success.html', {'message':success})


@permission_required('cargo.add_review')
def add_review(request):

    if request.method == 'POST':
        new_form = AddUserForm(request.POST, request.FILES)
        if new_form.is_valid():
            review = new_form.save(commit=False)
            review.date = datetime.datetime.now()
            review.save()
            new_form.save_m2m()

            return redirect('reviews')

    elif request.method == "GET":
        new_form = AddUserForm()

    return render(request, 'add_review.html', {'new_form': new_form})


def reviews(request):
    all_reviews = Review.objects.all().order_by('-date')
    viewed_reviews = request.session.get("viewed_reviews", [])
    return render(request, 'reviews.html', {'all_reviews':  all_reviews, 'viewed_reviews': viewed_reviews})


def review(request, id):
    try:
        review = Review.objects.get(id=id)
        viewed_reviews = request.session.get("viewed_reviews", [])
        if id not in viewed_reviews:
            viewed_reviews.append(id)
        request.session['viewed_reviews'] = viewed_reviews
    except:
        review = ""
    return render(request, 'review.html', {'review': review})

# def message2(request):
#     success = Review.objects.all
#     viewed_message = request.session.get("message2",[])
#     return render(request, 'message.html', {'message': success })





def regist(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = RegistrForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()

            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return render(request, 'registration/register_done.html', data)
    else: # Иначе
        # Создаём форму
        form = RegistrForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
    return render(request, 'registration/register.html', data)


# def reviews(request):
#     all_reviews = Review.objects.all()
#     viewed_reviews = request.session.get("viewed_reviews", [])
#     return render(request, 'reviews.html', {' reviews':  all_reviews})
#
#                   # , 'viewed_reviews': viewed_reviews})
#
# def review(request, id):
#     try:
#         review = Review.objects.get(id=id)
#         viewed_reviews = request.session.get("viewed_reviews", [])
#         if id not in viewed_reviews:
#             viewed_reviews.append(id)
#         request.session['viewed_reviews'] = viewed_reviews
#     except:
#         review = ""
#     return render(request, 'review.html', {'review': review})


