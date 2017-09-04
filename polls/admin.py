from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class ChoiceInline(admin.TabularInline):
    """
    make 'Choice' in 'Question' detail page
    can use 'admin.TabularInline' or 'admin.StackedInline'
    """
    model = Choice
    extra = 0  # make 0 extra blank choice


class QuestionAdmin(admin.ModelAdmin):
    """
     make the 'pub_date' comes before the "Question"
    """
    # fields = ['pub_date', 'question_text']  # make the 'pub_date' comes before the "Question"
    fieldsets = [  # this is for group the field
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    # for the columns which is display
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 添加右侧筛选条件
    list_filter = ['pub_date']
    # 增加搜索框，确定搜索字段
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
