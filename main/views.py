from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
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
    
    try:
        # Import WeasyPrint only when needed to avoid import errors in development
        from weasyprint import HTML
        
        # Use WeasyPrint for both development and production
        html = HTML(string=html_content)
        png_bytes = html.write_png()
        response = HttpResponse(png_bytes, content_type='image/png')
        response['Content-Disposition'] = f'attachment; filename="convert_{convert.name}.png"'
        return response
    except Exception as e:
        # Fallback for development when WeasyPrint is not available (e.g., Windows without GTK)
        if settings.DEBUG:
            return HttpResponse(
                f"Card generation not available in development. Error: {str(e)}<br>"
                f"Please deploy to PythonAnywhere to test card generation.",
                content_type='text/html'
            )
        else:
            raise


def view_card(request, convert_id):
    convert = get_object_or_404(Convert_blank, id=convert_id)
    return render(request, "card.html", {"convert": convert})
