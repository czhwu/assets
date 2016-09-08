# coding:utf-8
from django.shortcuts import render_to_response
from itassets import models

# Create your views here.


def asset_list(request):
    assets = models.Assets.objects.all()

    return render_to_response('home.html', {'assets': assets})


def update(request):
    assets = models.Assets.objects.all()

    return render_to_response('update.html')


# todo:增加detail视图
def detail(request,fgdzc):
    asset = models.Assets.objects.get(fgdzc=fgdzc)

    return render_to_response('detail.html', {'asset': asset})
