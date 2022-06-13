from django.shortcuts import render
from .forms import ContactForm
from .models import HallCard , SessionCard , MakeupCard , About,ServicesCard 
from .models import Banner,Categories,FeaturedProduct,Footer
from django.shortcuts import redirect




def home_page(request):

    banner = Banner.objects.all
    Category = Categories.objects.all
    products = FeaturedProduct.objects.all
    footer = Footer.objects.all

    return render(request,'pages/index.html',{
        'banner':banner,
        'Category':Category,
        'products':products,
        'footer':footer,
    })



def about_page(request):
    about = About.objects.get(pk=1)
    Services = ServicesCard.objects.all

    return render(request,'pages/about.html',{
        'about' : about,
        'Services' : Services,
    })

def halls_page(request):

    halls = HallCard.objects.all


    return render(request,'pages/halls.html',{
        'halls':halls,
    })

def makeup_page(request):

    makeups = MakeupCard.objects.all

    return render(request,'pages/makeup.html',{'makeups':makeups})

def session_page(request):

    sessions = SessionCard.objects.all 

    return render(request,'pages/session.html',{'sessions':sessions})


def single_hall_page(request,id):
    halls = HallCard.objects.get(id = id)
    return render(request,'pages/single-hall.html',{
        'halls':halls,
    })


def single_makeup_page(request,id):

    makeups = MakeupCard.objects.get(id = id)

    return render(request,'pages/single-makeup.html',{
        'makeups':makeups,
    })

def single_session_page(request,id):

    sessions = SessionCard.objects.get(id = id)

    return render(request,'pages/single-session.html',{
        'sessions' : sessions,
    }
    )

def contact_page(request):
    form = ContactForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()

    return render(request,'pages/contact.html',{'form':form})





