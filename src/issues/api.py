import json

from django.http import HttpResponse, JsonResponse

from .models import Issue


def create_issue(request):
    if request.method != "POST":
        raise NotImplementedError("Only POST method!")
    data = json.loads(request.body)
    issue = Issue.objects.create(**data)
    return HttpResponse(f"Your {issue.title} was successful create!")


def all_issues(request):
    issues = Issue.objects.all()
    # serialized_data = serialize('json', issues)
    # deserialized_data = json.loads(serialized_data)
    # json_response = JsonResponse({'result': deserialized_data})
    # return json_response

    fields = ["title", "status", "body", "id"]
    results = []
    for issue in issues:
        give_data = {attr: getattr(issue, attr) for attr in fields}
        results.append(give_data)
    return JsonResponse({"result": results})
