from django.shortcuts import render
from .forms import VisitorForm


def welcome_page(request):
    visitor_label = None

    if request.method == "POST":
        visitor_form = VisitorForm(request.POST)

        if visitor_form.is_valid():
            visitor = visitor_form.save()
            visitor_label = visitor.display_name
            visitor_form = VisitorForm()
    else:
        visitor_form = VisitorForm()

    return render(
        request,
        "greetings/home.html",
        {"visitor_form": visitor_form, "visitor_label": visitor_label},
    )
