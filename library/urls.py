from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import BookViewSet, AuthorViewSet, MemberViewSet, BorrowRecordViewSet

router = DefaultRouter()
router.register('books', BookViewSet,basename='books')
router.register('authors', AuthorViewSet,basename='authors')
router.register('members', MemberViewSet, basename='members')
router.register('borrow', BorrowRecordViewSet, basename='borrow-records')

urlpatterns = [
    path('', include(router.urls)),
]
