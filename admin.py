from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionInline(admin.TabularInline):
    model = Question

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text',)

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructor')

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)