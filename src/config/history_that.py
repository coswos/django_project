from django.http import HttpResponse


def show_history(_):
    data = []
    with open("history.json", "r") as json_file:
        for line in json_file:
            data.append(line)
        return HttpResponse(data)
