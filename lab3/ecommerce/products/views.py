from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from products.models import Product
from .forms import *

# products=[{'id':1, 'name':'iphone', 'src':'1.jpeg'},{'id':2, 'name':'redmi', 'src':'2.jpeg'}, {'id':3, 'name':'samsung', 'src':'3.jpeg'}]
# # Create your views here.
# def helloworld(request):
#   context = {}
#   context['products'] = products
#   return render(request, 'products/index.html', context)
# def helloworld2(request, pid):
#   myItem = list(filter(lambda t:t['id']==pid, products))  
#   if myItem:
#     return HttpResponse(f"hello world from products of {myItem}")
#   else:
#     return HttpResponse(f"item not found")
def productList(request):
  context={'products':Product.productList()}
  return render(request, 'products/index.html', context)


def productAddNew(request):
  if request.method == "POST":
    Product.objects.create(name=request.POST['pname'], img=request.FILES['pimg']) 
    r=reverse('products')    
    return HttpResponseRedirect(r)
    # return HttpResponseRedirect('/products')
  return render(request, 'products/productAdd.html')


def productAddNewForm(request):
  form=productForm()
  context={'form': form}
  if request.method == "POST":
    form=productForm(request, request.POST, request.FILES)
    if form.is_valid  :
      Product.objects.create(name= request.POST['name'],img= request.FILES['img'], category=Category.objects.get(id=request.POST['category'])) 
      r=reverse('products')    
      return HttpResponseRedirect(r)
    else:
      context['msg':"name is required"]
  return render(request, 'products/productAddForm.html', context)


def productDetails(request, pid):
  # obj1 = Product.objects.get(id=pid)
  obj1 = Product.productDetails(pid)
  context={'product':obj1}
  return render(request, 'products/productDetails.html', context)

def productUpdate(request, pid):
  obj1 = Product.objects.get(id=pid)
  context={'product':obj1}
  if request.method == "POST":
    if request.POST['pname'] != "":
      obj = Product.objects.filter(id=pid)[0]
      obj.name = request.POST['pname'] 
      obj.img = img=request.FILES['pimg']
      obj.save()
      r=reverse('products')    
      return HttpResponseRedirect(r)
    else:
      context={'errMsg':"all are required"}
  return render(request, 'products/productUpdate.html', context)


def productDelete(request, pid):
  Product.objects.get(id=pid).delete()
  return HttpResponseRedirect('/products')