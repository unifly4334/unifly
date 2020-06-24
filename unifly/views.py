from django.shortcuts import render,redirect
from django.http import HttpResponse
from webnews.models import newsinfo,adv,application,contact
#from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User,Group

from .forms import createuserform,updateform,viewform,contactform
from .decorators import unauthenticated_user,allowed_users,admin_only
from .filters import appfilter

from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail
from django.conf import settings

#below are for pdf files rendering
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template

import urllib.request
import urllib.parse
import json

# Create your views here.

@login_required(login_url='login')
#we can keep this login required for each page that we want if some should login to view this page
def mainpage(request):
	top_news1=newsinfo.objects.all().order_by('-datetime')[:1]
	top_news2=newsinfo.objects.all().order_by('-datetime')[1:2]
	top_news3=newsinfo.objects.all().order_by('-datetime')[2:3]
	sub_news11=newsinfo.objects.all().order_by('-datetime')[3:4]
	sub_news12=newsinfo.objects.all().order_by('-datetime')[4:5]
	sub_news13=newsinfo.objects.all().order_by('-datetime')[5:6]
	sub_news21=newsinfo.objects.all().order_by('-datetime')[6:7]
	sub_news22=newsinfo.objects.all().order_by('-datetime')[7:8]
	sub_news23=newsinfo.objects.all().order_by('-datetime')[8:9]
	sub_news31=newsinfo.objects.all().order_by('-datetime')[9:10]
	sub_news32=newsinfo.objects.all().order_by('-datetime')[10:11]
	sub_news33=newsinfo.objects.all().order_by('-datetime')[11:12]
	sub_news41=newsinfo.objects.all().order_by('-datetime')[12:13]
	sub_news42=newsinfo.objects.all().order_by('-datetime')[13:14]
	sub_news43=newsinfo.objects.all().order_by('-datetime')[14:15]
	sub_news51=newsinfo.objects.all().order_by('-datetime')[15:16]
	sub_news52=newsinfo.objects.all().order_by('-datetime')[16:17]
	sub_news53=newsinfo.objects.all().order_by('-datetime')[17:18]
	sub_news61=newsinfo.objects.all().order_by('-datetime')[18:19]
	sub_news62=newsinfo.objects.all().order_by('-datetime')[19:20]
	sub_news63=newsinfo.objects.all().order_by('-datetime')[20:21]
	sub_news71=newsinfo.objects.all().order_by('-datetime')[21:22]
	sub_news72=newsinfo.objects.all().order_by('-datetime')[22:23]
	sub_news73=newsinfo.objects.all().order_by('-datetime')[23:24]
	sub_news81=newsinfo.objects.all().order_by('-datetime')[24:25]
	sub_news82=newsinfo.objects.all().order_by('-datetime')[25:26]
	sub_news83=newsinfo.objects.all().order_by('-datetime')[26:27]
	sub_news91=newsinfo.objects.all().order_by('-datetime')[27:28]
	sub_news92=newsinfo.objects.all().order_by('-datetime')[28:29]
	sub_news93=newsinfo.objects.all().order_by('-datetime')[29:30]
	sub_news101=newsinfo.objects.all().order_by('-datetime')[30:31]
	sub_news102=newsinfo.objects.all().order_by('-datetime')[31:32]
	sub_news103=newsinfo.objects.all().order_by('-datetime')[32:33]
	sub_news111=newsinfo.objects.all().order_by('-datetime')[33:34]
	sub_news112=newsinfo.objects.all().order_by('-datetime')[34:35]
	sub_news113=newsinfo.objects.all().order_by('-datetime')[35:36]
	sub_news121=newsinfo.objects.all().order_by('-datetime')[36:37]
	sub_news122=newsinfo.objects.all().order_by('-datetime')[37:38]
	sub_news123=newsinfo.objects.all().order_by('-datetime')[38:39]
	sub_news131=newsinfo.objects.all().order_by('-datetime')[39:40]
	sub_news132=newsinfo.objects.all().order_by('-datetime')[40:41]
	sub_news133=newsinfo.objects.all().order_by('-datetime')[41:42]
	sub_news141=newsinfo.objects.all().order_by('-datetime')[42:43]
	sub_news142=newsinfo.objects.all().order_by('-datetime')[43:44]
	sub_news143=newsinfo.objects.all().order_by('-datetime')[44:45]
	sub_news151=newsinfo.objects.all().order_by('-datetime')[45:46]
	sub_news152=newsinfo.objects.all().order_by('-datetime')[46:47]
	sub_news153=newsinfo.objects.all().order_by('-datetime')[47:48]
	sub_news161=newsinfo.objects.all().order_by('-datetime')[48:49]
	sub_news162=newsinfo.objects.all().order_by('-datetime')[49:50]
	sub_news163=newsinfo.objects.all().order_by('-datetime')[50:51]
	sub_news171=newsinfo.objects.all().order_by('-datetime')[51:52]
	sub_news172=newsinfo.objects.all().order_by('-datetime')[52:53]
	sub_news173=newsinfo.objects.all().order_by('-datetime')[53:54]
	sub_news181=newsinfo.objects.all().order_by('-datetime')[54:55]
	sub_news182=newsinfo.objects.all().order_by('-datetime')[55:56]
	sub_news183=newsinfo.objects.all().order_by('-datetime')[56:57]
	sub_news191=newsinfo.objects.all().order_by('-datetime')[57:58]
	sub_news192=newsinfo.objects.all().order_by('-datetime')[58:59]
	sub_news193=newsinfo.objects.all().order_by('-datetime')[59:60]
	sub_news201=newsinfo.objects.all().order_by('-datetime')[60:61]
	sub_news202=newsinfo.objects.all().order_by('-datetime')[61:62]
	sub_news203=newsinfo.objects.all().order_by('-datetime')[62:63]

# Left adv data
	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	mynews={'top_news1':top_news1,'top_news2':top_news2,'top_news3':top_news3,'sub_news11':sub_news11,'sub_news12':sub_news12,'sub_news13':sub_news13,'sub_news21':sub_news21,'sub_news22':sub_news22,'sub_news23':sub_news23,'sub_news31':sub_news31,	'sub_news32':sub_news32,	'sub_news33':sub_news33,'sub_news41':sub_news41,'sub_news42':sub_news42,'sub_news43':sub_news43,'sub_news51':sub_news51,'sub_news52':sub_news52,'sub_news53':sub_news53,'sub_news61':sub_news61,'sub_news62':sub_news62,'sub_news63':sub_news63,'sub_news71':sub_news71,'sub_news72':sub_news72,'sub_news73':sub_news73,'sub_news81':sub_news81,'sub_news82':sub_news82,'sub_news83':sub_news83,'sub_news91':sub_news91,'sub_news92':sub_news92,'sub_news93':sub_news93,'sub_news101':sub_news101,'sub_news102':sub_news102,'sub_news103':sub_news103,
	'sub_news111':sub_news111,'sub_news112':sub_news112,'sub_news113':sub_news113,'sub_news121':sub_news121,'sub_news122':sub_news122,'sub_news123':sub_news123,'sub_news131':sub_news131,'sub_news132':sub_news132,'sub_news133':sub_news133,'sub_news141':sub_news141,'sub_news142':sub_news142,'sub_news143':sub_news143,'sub_news151':sub_news151,'sub_news152':sub_news152,'sub_news153':sub_news153,'sub_news161':sub_news161,'sub_news162':sub_news162,'sub_news163':sub_news163,
    'sub_news171':sub_news171,'sub_news172':sub_news172,'sub_news173':sub_news173,'sub_news181':sub_news181,'sub_news182':sub_news182,'sub_news183':sub_news183,'sub_news191':sub_news191,'sub_news192':sub_news192,'sub_news193':sub_news193,'sub_news201':sub_news201,'sub_news202':sub_news202,'sub_news203':sub_news203,'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5}
	return render(request,'main.html',context=mynews)

def subpage(request,title):
	all_news=newsinfo.objects.all()
	t_news=filter(lambda x: (x.newstitle == title), all_news)
	t_news1=filter(lambda x: (x.newstitle == title), all_news)
	top_news1=newsinfo.objects.all().order_by('-datetime')[:1]
	top_news2=newsinfo.objects.all().order_by('-datetime')[1:2]
	top_news3=newsinfo.objects.all().order_by('-datetime')[2:3]
	sub_news11=newsinfo.objects.all().order_by('-datetime')[3:4]
	sub_news12=newsinfo.objects.all().order_by('-datetime')[4:5]
	sub_news13=newsinfo.objects.all().order_by('-datetime')[5:6]
	sub_news21=newsinfo.objects.all().order_by('-datetime')[6:7]
	sub_news22=newsinfo.objects.all().order_by('-datetime')[7:8]
	sub_news23=newsinfo.objects.all().order_by('-datetime')[8:9]
	sub_news31=newsinfo.objects.all().order_by('-datetime')[9:10]
	sub_news32=newsinfo.objects.all().order_by('-datetime')[10:11]
	sub_news33=newsinfo.objects.all().order_by('-datetime')[11:12]
	sub_news41=newsinfo.objects.all().order_by('-datetime')[12:13]
	sub_news42=newsinfo.objects.all().order_by('-datetime')[13:14]
	sub_news43=newsinfo.objects.all().order_by('-datetime')[14:15]
	sub_news51=newsinfo.objects.all().order_by('-datetime')[15:16]
	sub_news52=newsinfo.objects.all().order_by('-datetime')[16:17]
	sub_news53=newsinfo.objects.all().order_by('-datetime')[17:18]
	sub_news61=newsinfo.objects.all().order_by('-datetime')[18:19]
	sub_news62=newsinfo.objects.all().order_by('-datetime')[19:20]
	sub_news63=newsinfo.objects.all().order_by('-datetime')[20:21]
	sub_news71=newsinfo.objects.all().order_by('-datetime')[21:22]
	sub_news72=newsinfo.objects.all().order_by('-datetime')[22:23]
	sub_news73=newsinfo.objects.all().order_by('-datetime')[23:24]
	sub_news81=newsinfo.objects.all().order_by('-datetime')[24:25]
	sub_news82=newsinfo.objects.all().order_by('-datetime')[25:26]
	sub_news83=newsinfo.objects.all().order_by('-datetime')[26:27]
	sub_news91=newsinfo.objects.all().order_by('-datetime')[27:28]
	sub_news92=newsinfo.objects.all().order_by('-datetime')[28:29]
	sub_news93=newsinfo.objects.all().order_by('-datetime')[29:30]
	sub_news101=newsinfo.objects.all().order_by('-datetime')[30:31]
	sub_news102=newsinfo.objects.all().order_by('-datetime')[31:32]
	sub_news103=newsinfo.objects.all().order_by('-datetime')[32:33]
	sub_news111=newsinfo.objects.all().order_by('-datetime')[33:34]
	sub_news112=newsinfo.objects.all().order_by('-datetime')[34:35]
	sub_news113=newsinfo.objects.all().order_by('-datetime')[35:36]
	sub_news121=newsinfo.objects.all().order_by('-datetime')[36:37]
	sub_news122=newsinfo.objects.all().order_by('-datetime')[37:38]
	sub_news123=newsinfo.objects.all().order_by('-datetime')[38:39]
	sub_news131=newsinfo.objects.all().order_by('-datetime')[39:40]
	sub_news132=newsinfo.objects.all().order_by('-datetime')[40:41]
	sub_news133=newsinfo.objects.all().order_by('-datetime')[41:42]
	sub_news141=newsinfo.objects.all().order_by('-datetime')[42:43]
	sub_news142=newsinfo.objects.all().order_by('-datetime')[43:44]
	sub_news143=newsinfo.objects.all().order_by('-datetime')[44:45]
	sub_news151=newsinfo.objects.all().order_by('-datetime')[45:46]
	sub_news152=newsinfo.objects.all().order_by('-datetime')[46:47]
	sub_news153=newsinfo.objects.all().order_by('-datetime')[47:48]
	sub_news161=newsinfo.objects.all().order_by('-datetime')[48:49]
	sub_news162=newsinfo.objects.all().order_by('-datetime')[49:50]
	sub_news163=newsinfo.objects.all().order_by('-datetime')[50:51]
	sub_news171=newsinfo.objects.all().order_by('-datetime')[51:52]
	sub_news172=newsinfo.objects.all().order_by('-datetime')[52:53]
	sub_news173=newsinfo.objects.all().order_by('-datetime')[53:54]
	sub_news181=newsinfo.objects.all().order_by('-datetime')[54:55]
	sub_news182=newsinfo.objects.all().order_by('-datetime')[55:56]
	sub_news183=newsinfo.objects.all().order_by('-datetime')[56:57]
	sub_news191=newsinfo.objects.all().order_by('-datetime')[57:58]
	sub_news192=newsinfo.objects.all().order_by('-datetime')[58:59]
	sub_news193=newsinfo.objects.all().order_by('-datetime')[59:60]
	sub_news201=newsinfo.objects.all().order_by('-datetime')[60:61]
	sub_news202=newsinfo.objects.all().order_by('-datetime')[61:62]
	sub_news203=newsinfo.objects.all().order_by('-datetime')[62:63]


	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	text={'t_news':t_news,'t_news1':t_news1,'top_news1':top_news1,'top_news2':top_news2,'top_news3':top_news3,'sub_news11':sub_news11,'sub_news12':sub_news12,'sub_news13':sub_news13,'sub_news21':sub_news21,'sub_news22':sub_news22,'sub_news23':sub_news23,'sub_news31':sub_news31,	'sub_news32':sub_news32,	'sub_news33':sub_news33,'sub_news41':sub_news41,'sub_news42':sub_news42,'sub_news43':sub_news43,'sub_news51':sub_news51,'sub_news52':sub_news52,'sub_news53':sub_news53,'sub_news61':sub_news61,'sub_news62':sub_news62,'sub_news63':sub_news63,'sub_news71':sub_news71,'sub_news72':sub_news72,'sub_news73':sub_news73,
	 	'sub_news81':sub_news81,'sub_news82':sub_news82,'sub_news83':sub_news83,'sub_news91':sub_news91,'sub_news92':sub_news92,'sub_news93':sub_news93,'sub_news101':sub_news101,'sub_news102':sub_news102,'sub_news103':sub_news103,
	'sub_news111':sub_news111,'sub_news112':sub_news112,'sub_news113':sub_news113,'sub_news121':sub_news121,'sub_news122':sub_news122,'sub_news123':sub_news123,'sub_news131':sub_news131,'sub_news132':sub_news132,'sub_news133':sub_news133,'sub_news141':sub_news141,'sub_news142':sub_news142,'sub_news143':sub_news143,'sub_news151':sub_news151,'sub_news152':sub_news152,'sub_news153':sub_news153,'sub_news161':sub_news161,'sub_news162':sub_news162,'sub_news163':sub_news163,
    'sub_news171':sub_news171,'sub_news172':sub_news172,'sub_news173':sub_news173,'sub_news181':sub_news181,'sub_news182':sub_news182,'sub_news183':sub_news183,'sub_news191':sub_news191,'sub_news192':sub_news192,'sub_news193':sub_news193,'sub_news201':sub_news201,'sub_news202':sub_news202,'sub_news203':sub_news203,
	'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5}
	return render(request,'inner1.html',context=text)

def national(request):
	nationalnews=newsinfo.objects.all().filter(newscategory='national')
	national11=nationalnews.order_by('-datetime')[:1]
	national12=nationalnews.order_by('-datetime')[1:2]
	national13=nationalnews.order_by('-datetime')[2:3]
	national21=nationalnews.order_by('-datetime')[3:4]
	national22=nationalnews.order_by('-datetime')[4:5]
	national23=nationalnews.order_by('-datetime')[5:6]
	national31=nationalnews.order_by('-datetime')[6:7]
	national32=nationalnews.order_by('-datetime')[7:8]
	national33=nationalnews.order_by('-datetime')[8:9]
	national41=nationalnews.order_by('-datetime')[9:10]
	national42=nationalnews.order_by('-datetime')[10:11]
	national43=nationalnews.order_by('-datetime')[11:12]
	national51=nationalnews.order_by('-datetime')[12:13]
	national52=nationalnews.order_by('-datetime')[13:14]
	national53=nationalnews.order_by('-datetime')[14:15]
	national61=nationalnews.order_by('-datetime')[15:16]
	national62=nationalnews.order_by('-datetime')[16:17]
	national63=nationalnews.order_by('-datetime')[17:18]
	national71=nationalnews.order_by('-datetime')[18:19]
	national72=nationalnews.order_by('-datetime')[19:20]
	national73=nationalnews.order_by('-datetime')[20:21]
	national81=nationalnews.order_by('-datetime')[21:22]
	national82=nationalnews.order_by('-datetime')[22:23]
	national83=nationalnews.order_by('-datetime')[23:24]
	national91=nationalnews.order_by('-datetime')[24:25]
	national92=nationalnews.order_by('-datetime')[25:26]
	national93=nationalnews.order_by('-datetime')[26:27]
	national101=nationalnews.order_by('-datetime')[27:28]
	national102=nationalnews.order_by('-datetime')[28:29]
	national103=nationalnews.order_by('-datetime')[29:30]

	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	national_news={'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5,'national11':national11,'national12':national12,'national13':national13,'national21':national21,'national22':national22,'national23':national23,'national31':national31,'national32':national32,'national33':national33,'national41':national41,'national42':national42,'national43':national43,'national51':national51,'national52':national52,'national53':national53,'national61':national61,'national62':national62,'national63':national63,'national71':national71,'national72':national72,'national73':national73,'national81':national81,'national82':national82,'national83':national83,'national91':national91,'national92':national92,'national93':national93,'national101':national101,'national102':national102,'national103':national103}
	return render(request,'national.html',context=national_news)

def international(request):
	internationalnews=newsinfo.objects.all().filter(newscategory='international')
	international11=internationalnews.order_by('-datetime')[:1]
	international12=internationalnews.order_by('-datetime')[1:2]
	international13=internationalnews.order_by('-datetime')[2:3]
	international21=internationalnews.order_by('-datetime')[3:4]
	international22=internationalnews.order_by('-datetime')[4:5]
	international23=internationalnews.order_by('-datetime')[5:6]
	international31=internationalnews.order_by('-datetime')[6:7]
	international32=internationalnews.order_by('-datetime')[7:8]
	international33=internationalnews.order_by('-datetime')[8:9]
	international41=internationalnews.order_by('-datetime')[9:10]
	international42=internationalnews.order_by('-datetime')[10:11]
	international43=internationalnews.order_by('-datetime')[11:12]
	international51=internationalnews.order_by('-datetime')[12:13]
	international52=internationalnews.order_by('-datetime')[13:14]
	international53=internationalnews.order_by('-datetime')[14:15]
	international61=internationalnews.order_by('-datetime')[15:16]
	international62=internationalnews.order_by('-datetime')[16:17]
	international63=internationalnews.order_by('-datetime')[17:18]
	international71=internationalnews.order_by('-datetime')[18:19]
	international72=internationalnews.order_by('-datetime')[19:20]
	international73=internationalnews.order_by('-datetime')[20:21]
	international81=internationalnews.order_by('-datetime')[21:22]
	international82=internationalnews.order_by('-datetime')[22:23]
	international83=internationalnews.order_by('-datetime')[23:24]
	international91=internationalnews.order_by('-datetime')[24:25]
	international92=internationalnews.order_by('-datetime')[25:26]
	international93=internationalnews.order_by('-datetime')[26:27]
	international101=internationalnews.order_by('-datetime')[27:28]
	international102=internationalnews.order_by('-datetime')[28:29]
	international103=internationalnews.order_by('-datetime')[29:30]

	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	international_news={'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5,'international11':international11,'international12':international12,'international13':international13,'international21':international21,'international22':international22,'international23':international23,'international31':international31,'international32':international32,'international33':international33,'international41':international41,'international42':international42,'international43':international43,'international51':international51,'international52':international52,'international53':international53,'international61':international61,'international62':international62,'international63':international63,'international71':international71,'international72':international72,'international73':international73,'international81':international81,'international82':international82,'international83':international83,'international91':international91,'international92':international92,'international93':international93,'international101':international101,'international102':international102,'international103':international103}
	return render(request,'international.html',context=international_news)


def local(request):
	localnews=newsinfo.objects.all().filter(newscategory='local')
	local11=localnews.order_by('-datetime')[:1]
	local12=localnews.order_by('-datetime')[1:2]
	local13=localnews.order_by('-datetime')[2:3]
	local21=localnews.order_by('-datetime')[3:4]
	local22=localnews.order_by('-datetime')[4:5]
	local23=localnews.order_by('-datetime')[5:6]
	local31=localnews.order_by('-datetime')[6:7]
	local32=localnews.order_by('-datetime')[7:8]
	local33=localnews.order_by('-datetime')[8:9]
	local41=localnews.order_by('-datetime')[9:10]
	local42=localnews.order_by('-datetime')[10:11]
	local43=localnews.order_by('-datetime')[11:12]
	local51=localnews.order_by('-datetime')[12:13]
	local52=localnews.order_by('-datetime')[13:14]
	local53=localnews.order_by('-datetime')[14:15]
	local61=localnews.order_by('-datetime')[15:16]
	local62=localnews.order_by('-datetime')[16:17]
	local63=localnews.order_by('-datetime')[17:18]
	local71=localnews.order_by('-datetime')[18:19]
	local72=localnews.order_by('-datetime')[19:20]
	local73=localnews.order_by('-datetime')[20:21]
	local81=localnews.order_by('-datetime')[21:22]
	local82=localnews.order_by('-datetime')[22:23]
	local83=localnews.order_by('-datetime')[23:24]
	local91=localnews.order_by('-datetime')[24:25]
	local92=localnews.order_by('-datetime')[25:26]
	local93=localnews.order_by('-datetime')[26:27]
	local101=localnews.order_by('-datetime')[27:28]
	local102=localnews.order_by('-datetime')[28:29]
	local103=localnews.order_by('-datetime')[29:30]
	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	local_news={'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5,'local11':local11,'local12':local12,'local13':local13,'local21':local21,'local22':local22,'local23':local23,'local31':local31,'local32':local32,'local33':local33,'local41':local41,'local42':local42,'local43':local43,'local51':local51,'local52':local52,'local53':local53,'local61':local61,'local62':local62,'local63':local63,'local71':local71,'local72':local72,'local73':local73,'local81':local81,'local82':local82,'local83':local83,'local91':local91,'local92':local92,'local93':local93,'local101':local101,'local102':local102,'local103':local103}
	return render(request,'local.html',context=local_news)

def cinema(request):
	cinemanews=newsinfo.objects.all().filter(newscategory='cinema')
	cinema11=cinemanews.order_by('-datetime')[:1]
	cinema12=cinemanews.order_by('-datetime')[1:2]
	cinema13=cinemanews.order_by('-datetime')[2:3]
	cinema21=cinemanews.order_by('-datetime')[3:4]
	cinema22=cinemanews.order_by('-datetime')[4:5]
	cinema23=cinemanews.order_by('-datetime')[5:6]
	cinema31=cinemanews.order_by('-datetime')[6:7]
	cinema32=cinemanews.order_by('-datetime')[7:8]
	cinema33=cinemanews.order_by('-datetime')[8:9]
	cinema41=cinemanews.order_by('-datetime')[9:10]
	cinema42=cinemanews.order_by('-datetime')[10:11]
	cinema43=cinemanews.order_by('-datetime')[11:12]
	cinema51=cinemanews.order_by('-datetime')[12:13]
	cinema52=cinemanews.order_by('-datetime')[13:14]
	cinema53=cinemanews.order_by('-datetime')[14:15]
	cinema61=cinemanews.order_by('-datetime')[15:16]
	cinema62=cinemanews.order_by('-datetime')[16:17]
	cinema63=cinemanews.order_by('-datetime')[17:18]
	cinema71=cinemanews.order_by('-datetime')[18:19]
	cinema72=cinemanews.order_by('-datetime')[19:20]
	cinema73=cinemanews.order_by('-datetime')[20:21]
	cinema81=cinemanews.order_by('-datetime')[21:22]
	cinema82=cinemanews.order_by('-datetime')[22:23]
	cinema83=cinemanews.order_by('-datetime')[23:24]
	cinema91=cinemanews.order_by('-datetime')[24:25]
	cinema92=cinemanews.order_by('-datetime')[25:26]
	cinema93=cinemanews.order_by('-datetime')[26:27]
	cinema101=cinemanews.order_by('-datetime')[27:28]
	cinema102=cinemanews.order_by('-datetime')[28:29]
	cinema103=cinemanews.order_by('-datetime')[29:30]

	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	cinema_news={'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5,'cinema11':cinema11,'cinema12':cinema12,'cinema13':cinema13,'cinema21':cinema21,'cinema22':cinema22,'cinema23':cinema23,'cinema31':cinema31,'cinema32':cinema32,'cinema33':cinema33,'cinema41':cinema41,'cinema42':cinema42,'cinema43':cinema43,'cinema51':cinema51,'cinema52':cinema52,'cinema53':cinema53,'cinema61':cinema61,'cinema62':cinema62,'cinema63':cinema63,'cinema71':cinema71,'cinema72':cinema72,'cinema73':cinema73,'cinema81':cinema81,'cinema82':cinema82,'cinema83':cinema83,'cinema91':cinema91,'cinema92':cinema92,'cinema93':cinema93,'cinema101':cinema101,'cinema102':cinema102,'cinema103':cinema103}
	return render(request,'cinema.html',context=cinema_news)

def sports(request):
	sportsnews=newsinfo.objects.all().filter(newscategory='sports')
	sports11=sportsnews.order_by('-datetime')[:1]
	sports12=sportsnews.order_by('-datetime')[1:2]
	sports13=sportsnews.order_by('-datetime')[2:3]
	sports21=sportsnews.order_by('-datetime')[3:4]
	sports22=sportsnews.order_by('-datetime')[4:5]
	sports23=sportsnews.order_by('-datetime')[5:6]
	sports31=sportsnews.order_by('-datetime')[6:7]
	sports32=sportsnews.order_by('-datetime')[7:8]
	sports33=sportsnews.order_by('-datetime')[8:9]
	sports41=sportsnews.order_by('-datetime')[9:10]
	sports42=sportsnews.order_by('-datetime')[10:11]
	sports43=sportsnews.order_by('-datetime')[11:12]
	sports51=sportsnews.order_by('-datetime')[12:13]
	sports52=sportsnews.order_by('-datetime')[13:14]
	sports53=sportsnews.order_by('-datetime')[14:15]
	sports61=sportsnews.order_by('-datetime')[15:16]
	sports62=sportsnews.order_by('-datetime')[16:17]
	sports63=sportsnews.order_by('-datetime')[17:18]
	sports71=sportsnews.order_by('-datetime')[18:19]
	sports72=sportsnews.order_by('-datetime')[19:20]
	sports73=sportsnews.order_by('-datetime')[20:21]
	sports81=sportsnews.order_by('-datetime')[21:22]
	sports82=sportsnews.order_by('-datetime')[22:23]
	sports83=sportsnews.order_by('-datetime')[23:24]
	sports91=sportsnews.order_by('-datetime')[24:25]
	sports92=sportsnews.order_by('-datetime')[25:26]
	sports93=sportsnews.order_by('-datetime')[26:27]
	sports101=sportsnews.order_by('-datetime')[27:28]
	sports102=sportsnews.order_by('-datetime')[28:29]
	sports103=sportsnews.order_by('-datetime')[29:30]
	leftadvfil=adv.objects.all().filter(advside='left')
	leftadv1=leftadvfil.order_by('-datetime')[:1]
	leftadv2=leftadvfil.order_by('-datetime')[1:2]
	leftadv3=leftadvfil.order_by('-datetime')[2:3]
	leftadv4=leftadvfil.order_by('-datetime')[3:4]
	leftadv5=leftadvfil.order_by('-datetime')[4:5]
# rightadvdata(request):
	rightadvfil=adv.objects.all().filter(advside='right')
	rightadv1=rightadvfil.order_by('-datetime')[:1]
	rightadv2=rightadvfil.order_by('-datetime')[1:2]
	rightadv3=rightadvfil.order_by('-datetime')[2:3]
	rightadv4=rightadvfil.order_by('-datetime')[3:4]
	rightadv5=rightadvfil.order_by('-datetime')[4:5]
	sports_news={'leftadv1':leftadv1,'leftadv2':leftadv2,'leftadv3':leftadv3,'leftadv4':leftadv4,'leftadv5':leftadv5,'rightadv1':rightadv1,'rightadv2':rightadv2,'rightadv3':rightadv3,'rightadv4':rightadv4,'rightadv5':rightadv5,'sports11':sports11,'sports12':sports12,'sports13':sports13,'sports21':sports21,'sports22':sports22,'sports23':sports23,'sports31':sports31,'sports32':sports32,'sports33':sports33,'sports41':sports41,'sports42':sports42,'sports43':sports43,'sports51':sports51,'sports52':sports52,'sports53':sports53,'sports61':sports61,'sports62':sports62,'sports63':sports63,'sports71':sports71,'sports72':sports72,'sports73':sports73,'sports81':sports81,'sports82':sports82,'sports83':sports83,'sports91':sports91,'sports92':sports92,'sports93':sports93,'sports101':sports101,'sports102':sports102,'sports103':sports103}
	return render(request,'sports.html',context=sports_news)

""" def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('main')
    return render(request, 'signup.html', {'form': form})
    """
@csrf_exempt
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        form=createuserform()

        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid():
                user=form.save()
                username=form.cleaned_data.get('username')

                group=Group.objects.get(name='customer')
                user.groups.add(group)

                messages.success(request,"Account Created successfully for " + username)
                return redirect('login')

        context={'form':form}
        return render(request,'signup.html',context)

@unauthenticated_user
@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
	            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
	            'response': recaptcha_response
                    }
            data = urllib.parse.urlencode(values)
            data = data.encode('utf-8')
            req = urllib.request.Request(url, data)
            response = urllib.request.urlopen(req)
            result = json.load(response)
            if user is not None:
                if result['success']:
                    login(request,user)
                    return redirect('main')
                else:
                    messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            else:
                messages.info(request,'Username or Password Invalid')

        context={}
        return render(request,'login.html',context)

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def application_view(request):
    apps={}
    return render(request,'application.html',context=apps)


#@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
@admin_only
def admin_view(request):
    allapp=application.objects.all().order_by('-datetime')

    myfilter=appfilter(request.GET,queryset=allapp)
    allapp=myfilter.qs

    allapps={'allapp':allapp,'myfilter':myfilter,}
    return render(request,'admin1.html',context=allapps)

@login_required(login_url='login')
def track_view(request):
    myapp=application.objects.all().filter(user=User.objects.get(username=request.user.username))
    myapps={'myapp':myapp}
    return render(request,'track.html',context=myapps)

def submit_application(request):
    firstname=request.POST.get('firstname',None)
    lastname=request.POST.get('lastname',None)
    email=request.POST.get('email',None)
    city=request.POST.get('city',None)
    dob=request.POST.get('dob',None)
    user=User.objects.get(username=request.user.username)

    appl=application(firstname=firstname,lastname=lastname,city=city,dob=dob,email=email,user=user)

    appl.save()

    send_mail('Telugu Power Application Created',
              'You have successfully created the new application',settings.EMAIL_HOST_USER,[email],fail_silently=False)

    return redirect('track')


def contact_view(request):
    form = contactform()
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            data = request.POST.copy()
            name = data.get('name')
            email = data.get('email')
            subject = data.get('subject')
            description = data.get('description')
            mail_sub=str(name) + " : " + str(subject)
            mail_desc=str(email) + " : " + str(description)
            send_mail(mail_sub,
            mail_desc,settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER],fail_silently=False)
            messages.success(request,"Thank you " + str(name) + " for contacting us we will get back to you soon on this " )
            return redirect('contact')
    context={'form':form}
    return render(request,'contact.html',context)

def aboutus_view(request):
    apps={}
    return render(request,'aboutus.html',context=apps)


def update_view(request,appid):

    appinfo=application.objects.get(application_id=appid)

    form=updateform(instance=appinfo)

    if request.method=='POST':
        form=updateform(request.POST,instance=appinfo)
        if form.is_valid():
            form.save()

            send_mail('Telugu Power Application Update',
              'Your Application '+str(appinfo.application_id)+' is updated ',settings.EMAIL_HOST_USER,[appinfo.email],fail_silently=False)
            messages.success(request,"Application " +str(appid)+ " Updated successfully" )
            return redirect('adminconsole')

    context={'form':form}

    return render(request,'update.html',context)


def view_app(request,appid):

    vapp=application.objects.filter(application_id=appid)
    vapps={'vapp':vapp}
    return render(request,'view.html',context=vapps)

"""
def save_application(request):
    firstname=request.POST.get('firstname',None)
    lastname=request.POST.get('lastname',None)
    email=request.POST.get('email',None)
    city=request.POST.get('city',None)
    dob=request.POST.get('dob',None)
    user=request.POST.get('user',None)
    status=request.POST.get('status',None)
    appl=application(firstname=firstname,lastname=lastname,city=city,dob=dob,email=email,user=user,status=status)

    appl.save()
    messages.success(request,"Application Updated successfully" )

    return render(request,'admin1.html')
"""