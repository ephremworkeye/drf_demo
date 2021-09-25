from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer

# Create your views here.

class IsSuperUser(BasePermission):
    def has_permission(self, request, View):
        return request.user.is_superuser

    def has_object_permission(self, request, View, obj):
        return request.user.is_superuser

# object level permission
class IsIndy(BasePermission):
    def has_object_permission(self, request, View, obj):
        if not obj.restricted:
            return True
        return request.user.username == 'indy'

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated] 
    # permission_classes = [IsAdminUser] # will also allow staffuser
    # permission_classes = [IsSuperUser] # will also allow staffuser
    permission_classes = [IsIndy | IsSuperUser] # chaining permission

    def get_queryset(self):
        if self.request.user.is_staff:
            return Book.objects.all()
        return Book.objects.filter(restricted=False)


@login_required
def library(request):
    output = f"""
        <html>
            <body>
                <h2>Library</h2>
                <p>{request.user.username}</p>
                <a href="/book/books/">Book Api</a>
                <br>
                <a href="/accounts/logout/">Logout</a>
            </body>
        </html>
    """
    return HttpResponse(output)

    
