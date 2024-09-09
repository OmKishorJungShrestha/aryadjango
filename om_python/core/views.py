from django.shortcuts import render
from django.http import JsonResponse
from core.models import Category

# Create your views here.
def home_api_view(request):
    fruits_price=[{"name":"apple","price":200},
                  {"name":"orange","price":100}]
    response_data=fruits_price
    categories = Category.objects.objects.all().values("name")
    response_data=[
        {"name":category.get("name")} for category in categories
    ]
    return JsonResponse(categories,safe=False)

def about_view(request):
    return render(request,"about.html")