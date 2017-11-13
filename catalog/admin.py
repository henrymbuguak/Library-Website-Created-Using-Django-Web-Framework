from django.contrib import admin
from .models import Book, BookInstance, Genre, Author, Language


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


class BookInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth','date_of_death')
    inlines = [BookInline]
    fields = [
        'first_name','last_name',
        (
            'date_of_birth',
            'date_of_death'
        )
    ]


admin.site.register(Author, AuthorAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','due_back','id')
    list_filter = ('status','due_back')
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        (
            'availability', {
                'fields' : ('status','due_back')
            }
        )
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

