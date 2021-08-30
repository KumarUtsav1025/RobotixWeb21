from django.contrib import admin
from .models import Questions, FormResponses, SubmittedUser, Recruitment
from import_export.admin import ImportExportModelAdmin
from import_export import resources


## Question For Recruitment
class QuestionsResource(resources.ModelResource):
    class Meta:
        model = Questions

## For Import export in the admin panel
class QuestionsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def shorten_ques(self, obj):
        if obj.question:
            shortend = ' '.join(str(obj.question).split(' ')[:7])+ "..."
            return shortend

    shorten_ques.short_description = "ShortQues"

    resource_class = QuestionsResource
    list_display = ['shorten_ques', 'question_id', 'question_type', 'question_for_domain', 'option1', 'option2', 'option3', 'option4']
    list_filter = ("question_for_domain",)

admin.site.register(Questions,QuestionsAdmin)



## Submitted candidate admin panel
class SubmittedUserResource(resources.ModelResource):
    class Meta:
        model = SubmittedUser

class SubmittedUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SubmittedUserResource
    list_display = ['candidate_name', 'candidate_mobile_number', 'candidate_emailid', 'candidate_domain_choices']

    

admin.site.register(SubmittedUser,SubmittedUserAdmin)




## Form Responses
class FormResponsesResource(resources.ModelResource):
    class Meta:
        model = FormResponses

class FormResponsesAdmin(ImportExportModelAdmin):
    resource_class = FormResponsesResource
    

admin.site.register(FormResponses,FormResponsesAdmin)
admin.site.register(Recruitment)