from django.shortcuts import render, redirect, get_object_or_404
from .forms import Pizzaform, Orderform
from .models import Pizza, Order, Topping


def index(request):
    if request.method == "POST":
        form = Pizzaform(request.POST)
        if form.is_valid():
            pizza = form.save()
            
            topping_id = request.POST.getlist('toppings')
        
            
            request.session['topping_id'] = topping_id

            
            return redirect("order", pizza_id=pizza.id)
        else:
            return render(request, "index.html", {"form": form})
    form = Pizzaform()
    return render(request, "index.html", {"form": form})


def order(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    if request.method == "POST":
        form = Orderform(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.pizza = pizza
           
            order.save()
            return redirect("confirmation", order_id=order.id)
        else:
            
            return render(request,"order.html", {"form": form, "pizza": pizza},)
    form = Orderform()
    return render(request, "order.html", {"form": form, "pizza": pizza})



def confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    toppings_list = []
    topping_id = request.session.get('topping_id')
    for t_id in topping_id:
        topping = Topping.objects.get(id=t_id)
        toppings_list.append(topping)
        
    return render(request, "confirmation.html", {"order": order, "toppings": toppings_list})



