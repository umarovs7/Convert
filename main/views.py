from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from playwright.sync_api import sync_playwright
import io

from .models import Convert_blank, Distination


DEFAULT_PLACES = ["Kafe", "Restoran", "Park", "Kino", "Muzey"]


def home(request):
    return render(request, "index.html")


def form(request):
    if not Distination.objects.exists():
        Distination.objects.bulk_create(
            [Distination(name=place) for place in DEFAULT_PLACES]
        )

    distinations = Distination.objects.all()

    if request.method == "POST":
        name = (request.POST.get("name") or "").strip()
        date_day = request.POST.get("date_day")
        date_time = request.POST.get("date_time")
        distination_id = request.POST.get("distination")

        if name and date_day and date_time and distination_id:
            Convert_blank.objects.create(
                name=name,
                date_day=date_day,
                date_time=date_time,
                distination_id=distination_id,
            )
            return redirect("success")

        return render(
            request,
            "form.html",
            {
                "distinations": distinations,
                "name": name,
                "date_day": date_day,
                "date_time": date_time,
                "distination_id": distination_id,
            },
        )

    return render(request, "form.html", {"distinations": distinations})


def success(request):
    last_convert = Convert_blank.objects.last()
    return render(request, "success.html", {"convert": last_convert})


def generate_card(request, convert_id):
    convert = get_object_or_404(Convert_blank, id=convert_id)
    
    html_content = render(request, "card.html", {"convert": convert}).content.decode("utf-8")
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html_content)
        
        # Get the card element dimensions
        card = page.locator('.invite-card')
        box = card.bounding_box()
        
        # Screenshot the card element
        screenshot = card.screenshot(type='png')
        
        browser.close()
    
    response = HttpResponse(screenshot, content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="convert_{convert.name}.png"'
    
    return response


def view_card(request, convert_id):
    convert = get_object_or_404(Convert_blank, id=convert_id)
    return render(request, "card.html", {"convert": convert})
