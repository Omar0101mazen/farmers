from django.urls import reverse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import  product
from .forms import add_product

# Create your views here.




@login_required
def dashboard(request):
    product_list = product.objects.filter(farmer_id=request.user.id)      
    if request.method == 'POST':
        form = add_product(request.POST,request.FILES)
        if form.is_valid:
            product_form = form.save(commit = False)
            product_form.farmer = request.user
            product_form.save() 
            
    else:
        form = add_product()
            
    context = {
        'product_list':product_list,
        'herbs':product.objects.filter(farmer_id=request.user.id,PROcategory = '4').count(),
        'fruits':product.objects.filter(farmer_id=request.user.id,PROcategory = '3').count(),
        'vegetable':product.objects.filter(farmer_id=request.user.id,PROcategory = '2').count(),
        'form':form,
    }
    return render(request,'Dashboard/dashboard.html',context)

     
    
def delete(request,id):
    delete_id = get_object_or_404(product,id=id)
    delete_id.delete()
    return redirect(reverse('dashboard:dashboard'))
