from django.contrib import admin

# Register your models here.
from .models import Articles_2, Articles



class ChoiceInline(admin.TabularInline):
    model = Articles_2
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Район', {'fields': ['title']}),
        ('Дата публикации', {'fields': ['time']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('title', 'time')
admin.site.register(Articles, QuestionAdmin)


