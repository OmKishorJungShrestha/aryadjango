from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Genre
from core.api.serializers import GenreSerializer

class BookListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Create a list of books
        #products = Product.objects.all()
        Genre = Genre.objects.all() # select * from genre
        print(type(genre))
        serializer= GenreSerializer(genre,many=true)
        #response =[{"name":"Think and grow rich", "author":"Nepoview"}]
        response={"genres": serializer.data}
        return Response(response)
        #response = [{"name": "Think and Grow Rich", "author": "Napoleon Hill","products": Product } ]
        # Return the response with the book data
        return Response(response)
    
    def post(self,request,*args,**kwargs):
        return Response({"response":"request received"})
    