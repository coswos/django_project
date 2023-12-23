import json

from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse

from .models import User

# здесь будут обращения к бд через ОРМ


def all_users(request):
    users = User.objects.all()
    fields = ["email", "first_name", "last_name", "id"]
    results = []

    for user in users:
        data_presentation = {attr: getattr(user, attr) for attr in fields}
        results.append(data_presentation)
    return JsonResponse({"result": results})


def create_user(request):
    if request.method != "POST":
        raise NotImplementedError("Only POST requests")

    data: dict = json.loads(request.body)
    try:
        user: User = User.objects.create(**data)
    # TODO may be replace data['email] -> user.email later
    except IntegrityError as error:
        # return HttpResponse("Try another email." f"\nUser with {data['email']} already exist!")
        return HttpResponse(error)

    fields = ["email", "first_name", "last_name", "id"]
    data_presentation = {attr: getattr(user, attr) for attr in fields}

    if not user:
        raise NotImplementedError("Can not create user!")

    return JsonResponse(data_presentation)
