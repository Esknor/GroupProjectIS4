from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import ProductForm
from django.http import HttpResponse, HttpResponseRedirect 
 #prod = form.save(commit=False)
	    #prod.created = timezone.now()
	    #prod.save()	                
            #return HttpResponseRedirect(prod.get_absolute_url())
def Post(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
           prod =form.save(commit=False)
           prod.save()
           return redirect('/')
    else:
        form = ProductForm()
    return render(request,'shop/post.html', {'form': form})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
