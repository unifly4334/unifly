from django.db import models


class contact(models.Model):
    name=models.CharField(null=False,blank=False,max_length=30)
    email=models.EmailField(null=False,blank=False,max_length=50)
    subject=models.CharField(null=False,blank=False,max_length=100)
    description=models.TextField(null=False,blank=False,max_length=2000)

    def __str__(self):
	    return self.email


# Create your models here.
country_name=[
    ("India","India"),
    ("UK","UK"),
    ("USA","USA"),

    ]


class university(models.Model):
    country=models.CharField(null=False,blank=False,default='UK',max_length=20,choices=country_name)
    uniname=models.CharField(max_length=100)
    loc=models.CharField(max_length=200)

    def __str__(self):
	    return self.uniname



possible_values =[
    ("Pending","Pending"),
    ("In-Review","In-Review"),
    ("Approved","Approved"),
    ("Rejected","Rejected"),
    ("Cancelled","Cancelled"),
    ("Waiting-Info","Waiting-Info"),

    ]

class application(models.Model):
    application_id=models.AutoField(primary_key=True)
    user=models.CharField(null=False,blank=False,default='None',max_length=200)
    firstname=models.CharField(null=False,blank=False,default=' ',max_length=200)
    lastname=models.CharField(null=False,blank=False,default=' ',max_length=200)
    email=models.EmailField(null=False,blank=False,default=' ',max_length=254)
    city=models.CharField(null=False,blank=False,default=' ',max_length=200)
    dob=models.DateField()
    status=models.CharField(null=False,blank=False,default='Pending',max_length=200,choices=possible_values)
    datetime=models.DateTimeField(auto_now=True)
    file1=models.FileField(null=False,blank=False,upload_to='images/',default='images/dummy.pdf')
    file2=models.FileField(null=False,blank=False,upload_to='images/',default='images/dummy.pdf')



    def __str__(self):
	    return self.email


class newsinfo(models.Model):
	newstitle=models.CharField(primary_key=True,max_length=200)
	newsheading=models.CharField(null=False,blank=False,default=' ',max_length=200)
	newsimage1=models.ImageField(null=False,blank=False,upload_to='images/')
	newsimage2=models.ImageField(null=True,blank=True,upload_to='images/')
	datetime=models.DateTimeField(auto_now=True)
	newscategory=models.CharField(null=False,blank=False,max_length=15)
	newstext1=models.TextField(null=False,blank=False,max_length=2000)
	newstext2=models.TextField(null=False,blank=False,max_length=2000)
	newstext3=models.TextField(null=True,blank=True,max_length=2000)

	def __str__(self):
		return self.newstitle

class adv(models.Model):
	advid=models.IntegerField(primary_key=True)
	advname=models.CharField(max_length=100)
	advimg=models.ImageField(null=False,blank=False,upload_to='images/')
	advheight=models.IntegerField(null=True,blank=True)
	advside=models.CharField(default='left',max_length=10)
	datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.advname



