from django.shortcuts import render

from dashboard.models import product,Category


# Create your views here.




from dashboard.models import product

            
            

def product_list(request):
    product_all = product.objects.all()
    CAT_filer= Category.objects.all()
    cate = request.GET.get('Category')
    if cate:
        product_all = product.objects.filter(PROcategory=cate) 

        
    cont ={
        'pro':product_all,
        'CAT_filer':CAT_filer,
        
    }
    return render(request,'products/products.html',cont)




def product_detail(request,id):
    product_detail = product.objects.get(id=id)

        
    context = {'product_d':product_detail}
    return render(request,'Products/products_detail.html',context)