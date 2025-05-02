from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book, Author, Member, BorrowRecord
from .serializers import BookSerializer, AuthorSerializer, MemberSerializer, BorrowRecordSerializer
from library.permissions import IsLibrarian, IsMember
from rest_framework.permissions import SAFE_METHODS





class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    
    - Librarians can perform all actions (create, read, update, delete)
    - Members can only view books (list and retrieve)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_permissions(self):
        # Members can read-only (GET, HEAD, OPTIONS)
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        # Librarians can write
        return [IsAuthenticated(), IsLibrarian()]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]


# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def get_permissions(self):
#         if self.request.method in SAFE_METHODS:
#             return [IsAuthenticated()]
#         return [IsAuthenticated(), IsLibrarian()]


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]


class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsMember() | IsLibrarian()]
        elif self.request.method in ['PATCH']:
            return [IsAuthenticated(), IsMember() | IsLibrarian()]
        elif self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        else:
            return [IsAuthenticated(), IsLibrarian()]
