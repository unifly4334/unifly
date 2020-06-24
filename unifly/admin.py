from django.contrib import admin

# Register your models here.

# Register your models here.
from webnews.models import newsinfo,adv,application,university,contact

# Register your models here.

class newsinfoadmin(admin.ModelAdmin):
	list=['newstitle','newsheading','newsimage1','newsimage2','datetime','newscategory','newstext1','newstext2','newstext3']

class advadmin(admin.ModelAdmin):
	list=['advid','advname','advimg','advheight','advside','datetime']

class applicationadmin(admin.ModelAdmin):
    list=['application_id','user','firstname','lastname','email','city','dob','status','datetime']

class universityadmin(admin.ModelAdmin):
    list=['country','uniname','loc']

class contactadmin(admin.ModelAdmin):
    list=['name','email','subject','description']


admin.site.register(newsinfo,newsinfoadmin)
admin.site.register(adv,advadmin)
admin.site.register(application,applicationadmin)
admin.site.register(university,universityadmin)
admin.site.register(contact,contactadmin)
