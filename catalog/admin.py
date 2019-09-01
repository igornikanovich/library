from django.contrib import admin
from .models import User, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', )
    list_filter = ['author', 'genre', ]
    search_fields = ['title', 'author', ]


admin.site.register(Book, BookAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', )
    list_filter = ['is_staff', ]


admin.site.register(User, UserAdmin)
