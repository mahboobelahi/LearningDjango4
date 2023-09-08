from django.contrib import admin
from .models import (Genre,Author,Language,
                     Book,BookInstance)
# Register your models here.
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(BookInstance)