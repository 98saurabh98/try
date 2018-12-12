from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.

from .models import CreateExam, Section, MakeExamLive, McqQuestion, TextQuestion

admin.site.register(CreateExam)
#admin.site.register(TextAnswer)
#admin.site.register(Question)
#admin.site.register(Tag)
admin.site.register(Section)
admin.site.register(MakeExamLive)
#admin.site.register(SectionAnswerSheet)
#admin.site.register(Answer)
admin.site.register(McqQuestion)
#admin.site.register(Option)
#admin.site.register(McqAnswer)
admin.site.register(TextQuestion)
#admin.site.register(McqAnswerToMcqOption)