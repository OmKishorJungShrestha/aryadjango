from rest_framework.views import APIView
from rest_framework.response import Response

class BookListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Create a list of books
        response = [
            {"name": "Think and Grow Rich", "author": "Napoleon Hill"}
        ]
        # Return the response with the book data
        return Response(response)