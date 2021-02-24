from django.contrib import admin

# Register your models here.
# IF We want to add poles or questions and Chocies to the admin area
# we Must Interact with this file

from .models import Question, Choice

# customize site header
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster  Admin Area"
admin.site.index_title = "Weclome to the Pollster Admin area"

# Registering my models
# admin.site.register(Question)
# admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}), ]

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
