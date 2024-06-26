from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about(request):
    """
    Renders the About page
    Displays an instance of :model:`about:About`.
    **Context
    ``about``
    the instance of model:`about.About`
    ``collaborate_form``
    the instance of :form:`about.CollaborateForm`
    ``HTML template``
    templates:`about/about.html`
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Thank you for your request. I will contact you during"
                "5 working days."
            )

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )
