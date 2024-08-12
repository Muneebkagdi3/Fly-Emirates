from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import fly,category, Ticket, Passenger
from django.db.models import Q
import razorpay
import random
from django.views.decorators.csrf import csrf_exempt




# Create your views here.


def Home(request):
    return render(request,"index.html")


class FlightList(ListView):
    model = fly
    context_object_name = "list"


class FlightDetail(DetailView):
    model = fly
    context_object_name = "detail"
    template_name = "fly/fly_detail.html"


def search(request):
    from_ = request.GET.get("from")
    to = request.GET.get("to")
    date = request.GET.get("date")

    flight = fly.objects.filter(Q(From = from_) & Q(To=to) )

    return render(request, "fly/search.html", {"flight": flight})

class CategoryDetailView(DetailView):
    model=category
    template_name="category/category.html"
    context_object_name="categoryob"


def payment(request,planeId):

     flyId = fly.objects.get(id = planeId)

     name = request.GET.get("name")
     age = request.GET.get("age")
     gender = request.GET.get("gender")

     passenger = Passenger.objects.create(Name =name, Age=age, Gender=gender, fly_id = flyId )

     request.session["P_id"]= passenger.id




     plane = fly.objects.get(id = planeId)
     amount = plane.Price*100

     TicketNo = str(random.randint(21212,937237)*planeId)
     print(TicketNo)


     client=razorpay.Client(auth=("rzp_test_tXhb7aXiGBGPzD","9tr12zxl6DeyAEAQdkHAGShJ"))
     data={"amount": amount,"currency":"INR","receipt": TicketNo}
     payment=client.order.create(data=data)
     print(payment)
     return render(request,"fly/payment.html",{"payment":payment, "TicketNo":TicketNo})


@csrf_exempt
def book(request, TicketNo):

    p = Passenger.objects.get(id = request.session.get("P_id"))
    ticket = Ticket.objects.create(TicketNo = int(TicketNo), Name = p.Name , Flight_Name = p.fly_id.Flight_Name,
    From = p.fly_id.From, To = p.fly_id.To)
    return render(request, "fly/ticket.html", {"Ticket": ticket})



