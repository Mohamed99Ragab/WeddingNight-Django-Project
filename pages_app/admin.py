from django.contrib import admin
from .models import Contact , HallCard , SessionCard , MakeupCard,About,ServicesCard
from .models import Footer , Categories,FeaturedProduct,Banner


admin.site.register((Contact,HallCard,SessionCard,MakeupCard,About,ServicesCard))

admin.site.register((Footer,Categories,FeaturedProduct,Banner))