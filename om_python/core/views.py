'''from django.shortcuts import render
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

def product_view(request):
    queryset =Category.objects.all()#select * from category
    context = {"queryset":queryset}
    return render(request, "product.html",context)

'''
from django.shortcuts import render
from django.http import JsonResponse
from core.models import Category

# Create your views here.
def home_api_view(request):
    # Sample fruit prices (this part seems unused in the final response)
    fruits_price = [
        {"name": "apple", "price": 200},
        {"name": "orange", "price": 100}
    ]
    
    # Get all categories from the database
    categories = Category.objects.all().values("name")
    
    # Create a response data list from the categories
    response_data = [
        {"name": category["name"]} for category in categories
    ]
    
    # Return the JSON response with category names
    return JsonResponse(response_data, safe=False)

def about_view(request):
    # Render the about.html template
    return render(request, "about.html")

def product_view(request):
   #print(request.post)
   data = request.POST
    # Retrieve all categories from the database
   queryset = Category.objects.all()  # Select all categories
   if data:
       # select * from coategory where name = data.get("search")
        queryset =queryset.filter(name=data.get("search"))
    # Prepare the context for the template
   context = {"queryset": queryset}
    # Render the product.html template with the context
   return render(request, "product.html", context)



