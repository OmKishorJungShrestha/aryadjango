from rest_framework.views import APIView
from rest_framework.response import Response
#from core.models import Genre
from core.models import Product
from core.api.serializers import ProductSerializer

class BookListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Create a list of books
        #products = Product.objects.all()
        '''genre = Genre.objects.all() # select * from genre
        print(type(genre))
        serializer= GenreSerializer(genre,many=true)
        #response =[{"name":"Think and grow rich", "author":"Nepoview"}]
        response={"genres": serializer.data}
        return Response(response)
    '''
        product = Product.objects.all()
        print(type(product))
        serializer= ProductSerializer(product, many=True)
        
       # response = [{"name": "Think and Grow Rich", "author": "Napoleon Hill","products": Product } ]
        # Return the response with the book data
        response ={"product":serializer.data}
        return Response(response)
    
    def post(self,request,*args,**kwargs):
        print(request.query_params)
        print(request.data)
        search = request.query_params.get("search")
        product=Product.objects.filter(name_icontains=search)
        serializer =ProductSerializer(product, many=True)
        return Response(serializer.data)
    
    #    return Response({"response":"request received"})
    
    
    