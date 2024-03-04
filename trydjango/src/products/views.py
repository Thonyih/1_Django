from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Product, SunburstData
from .forms import ProductForm, RawProductForm


def homepage_view(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)

    # products = Product.objects.all() first version of this code
    # context = {
    #     'products': products,
    # }

    sunburst_data = SunburstData.objects.all() #Gets all the data from database
    nodes_by_parent = {None: []}

    for node in sunburst_data:
        if node.parent_id not in nodes_by_parent:
            nodes_by_parent[node.parent_id] = []
        nodes_by_parent[node.parent_id].append(node)

    def build_hierarchy(node):
        children = nodes_by_parent.get(node.id, [])
        node_structure = {
            'name': node.name,
            'value': node.value
        }
        if children:
            node_structure['children'] = [build_hierarchy(child) for child in children]
        return node_structure
    
    root_nodes = [build_hierarchy(node) for node in nodes_by_parent[None]]

    sunburst_data = {'name': 'root', 'children': root_nodes} if len(root_nodes) > 1 else root_nodes[0]
    context = {
        'sunburst_data': sunburst_data
    }

    # context = {
    #     'sunburst_data': list(sunburst_data),
    # }

    print(list(sunburst_data))

    return render(request, "home.html", context)


def contact_view(request, *args, **kwargs):
    print(request)
    return render(request, "contact.html", {})


def about(request, *args, **kwargs):
    print(request)
    return render(request, "about.html", {})


def hometest(request, *args, **kwargs):
    print(request)

    my_context = {
        "my_text": "this text is in views.py",
        "this_is_true": True,
        "my_number": 123456789,
        "aListInPython": [10, "abc", 312, 14, 25, "abc"]
    }

    return render(request, "hometest.html", my_context)


def basehtml(request, *args, **kwargs):
    print(request)
    return render(request, "base.html", {})
    
######################################################################
######################################################################

#THIS IS TO CREATE PRODUCTS (I CAN VIEW THEM IN THE ADMIN)
# OR I CAN VIEW THEM IN THE def product_list_view(request):
def product_create_view(request):

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }    

    return render(request, "products/product_create.html", context)

#####################################################################

#THIS ONE IS TO VIEW THE PRODUCT
def product_detail_view(request, my_id):

    obj = get_object_or_404(Product, id=my_id) #This one is best one for this case

    # obj = Product.objects.get(id=my_id) THIS DOES NOT CHECK FOR OBJETS THAT DONT EXIST
     
    # try:
    #     obj = Product.objects.get(id=my_id) THIS DOES CHECK, BUT ITS MORE COMPLEX
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        'object': obj
        }

    return render(request, 'products/product_detail.html', context)


#THIS ONE IS TO DELETE
def product_delete_view(request, my_id):

    obj = get_object_or_404(Product, id=my_id)

    if request.method == "POST":
        # confirming the delete
        obj.delete()
        return redirect('productlist')

    context ={
        "object": obj
    }

    return render(request, "products/product_delete.html", context)

#THIS ONE ALLOWS ME TO VIEW THE PRODUCTS
def product_list_view(request):

    queryset = Product.objects.all()

    context = {
        "object_list": queryset
    }
    
    return render(request, "products/product_list.html", context)


###################################################################


def product_detailhtml(request):
    print(request), print("Here in detail")
    return render(request, "products/detail.html")


