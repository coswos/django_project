from django.shortcuts import render

from src.config.exchange import main_exchange


def new_page(request):
    return render(request, "new.html")


def submit_form(request):
    if request.method == "POST":
        # Получить данные из формы
        from_cur: str = request.POST.get("from_ex")
        to_cur: str = request.POST.get("to_ex")
        from_cur = from_cur.strip()
        to_cur = to_cur.strip()

        result_data = main_exchange(request, currency_from=from_cur, currency_to=to_cur)
        return render(request, "last_page.html", {"result_data": result_data})

    return render(request, "form.html")
