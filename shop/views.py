from django.shortcuts import render
from django.http import HttpResponse
from .models import product,Contact,Orders,orderUpdate
from math import ceil
import json
# Create your views here.

def index(request):
    products = product.objects.all()
    # print(products)
    n = len(products)
    nslides = n//4 + ceil((n/4)-(n//4))
    params = {'product':products}
    return render(request,'shop/index.html',params)

def search(request):
    query = request.GET.get('search')

    allprods = []
    catprods = product.objects.values('category','id','image','desc','product_name','price')
    for item in catprods:
        if query == item['product_name']:
            print(item)
            para = {'para':item}
            return render(request,'shop/search.html',para)
    # para = {"allprods":item}
    # catprods = product.objects.values('category','id')
    # cats = {item['category'] for item in catprods}
    # print(catprods)
    # print(cats)
    # for cat in cats:
        # prodtemp = product.objects.filter(category=cat)
        # print(prodtemp)
        # prod = [item for item in prodtemp if searchMatch(query,item)]
        # print(prod)
        # n=len(prod)
        # print(prod)
    #     if len(prod) != 0:
    #         allprods.append(prod)
    #         print(allprods)
    # para = {'allprods':allprods}
    # return render(request,'shop/search.html',para)




def about(request):
    return render(request,'shop/about.html')


def Contacts(request):
    if request.method == "POST":
        # print(request)
        name= request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        print(name,phone,email,desc)
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId')
        email = request.POST.get('email')
        try:
            order = Orders.objects.get(order_id=orderId)
            if order:
                update = orderUpdate.objects.get(order_id=order.order_id)
                updates = []
                # for item in update:
                #     updates.append({'text':item.update_desc, 'time': item.timestamp})
                    # response = json.dumps(updates,default=str)
                    # ruetrn HttpResponse(response)
                response = f"order id{update.order_id} desction{update.update_desc}"
                # return HttpResponse(response)
                return render(request, 'shop/tracker.html',{'response':response})
            else:
                return HttpResponse("{}")
        except Exception as e:
            print(e)
    return render(request,'shop/tracker.html',)



def productive(request,myid):
    products = product.objects.filter(id=myid)
    # print(products)
    return render(request,'shop/preview.html',{'products':products[0]})


def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('items_json')
        name = request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip_code=request.POST.get('zip_code')
        order =Orders(name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,items_json=items_json)
        order.save()
        thank = True
        id = order.order_id
        update = orderUpdate(order_id=order.order_id,update_desc="The order has been placed")
        update.save()
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
    return render(request,'shop/checkout.html')



















