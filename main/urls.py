from django.urls import path
from .views import home, form, success, generate_card, view_card

urlpatterns = [
    path("", home, name="home"),
    path("form/", form, name="form"),
    path("success/", success, name="success"),
    path("card/<int:convert_id>/download/", generate_card, name="card_download"),
    path("card/<int:convert_id>/", view_card, name="card_view"),
]
