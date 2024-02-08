from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from category.models import Category

def categoryList(request):
  context={'categories':Category.objects.all()}
  return render(request, 'category/index.html', context)


def categoryAddNew(request):
  if request.method == "POST":
    Category.objects.create(name=request.POST['cname'], img=request.FILES['cimg']) 
    r=reverse('categories')    
    return HttpResponseRedirect(r)
  return render(request, 'category/categoryAdd.html')


def categoryDetails(request, cid):
  obj1 = Category.objects.get(id=cid)
  context={'category':obj1}
  return render(request, 'category/categoryDetails.html', context)


def categoryDelete(request, cid):
  Category.objects.get(id=cid).delete()
  return HttpResponseRedirect('/categories')

def categoryUpdate(request, cid):
  obj1 = Category.objects.get(id=cid)
  context={'category':obj1}
    # imgpath=request.FILES['cimg']
    # print(imgpath)
  if request.method == "POST":
    if request.POST['cname'] != "":
      obj = Category.objects.filter(id=cid)[0]
      obj.name = request.POST['cname'] 
      obj.img = request.FILES['cimg']
      obj.save()
      r=reverse('categories')    
      return HttpResponseRedirect(r)
    else:
      context={'errMsg':"all are required"}
  return render(request, 'category/categoryUpdate.html', context)