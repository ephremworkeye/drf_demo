from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer

@api_view(['GET','POST', 'DELETE', 'PUT'])
def all_movies(request):
    movies = Movie.objects.all()
    movie_serializer = MovieSerializer(movies, many=True)
    return Response(movie_serializer.data)

