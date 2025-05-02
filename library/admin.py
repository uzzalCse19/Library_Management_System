from django.contrib import admin
from library.models import Author, Member, Book, BorrowRecord

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'membership_date')
    search_fields = ('name', 'email')
    list_filter = ('membership_date',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'category', 'is_available')
    search_fields = ('title', 'isbn')
    list_filter = ('category', 'is_available')

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('book__title', 'member__name')
