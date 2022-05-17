from rest_framework import generics
from .serializers import LikesSerializer
from .models import Likes

class LikesView(generics.ListAPIView):
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()