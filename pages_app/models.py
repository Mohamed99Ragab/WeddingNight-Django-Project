from email.headerregistry import Address
from django.db import models
from datetime import datetime    


class Categories(models.Model):
    category_image = models.ImageField(upload_to ='categories',null=True,blank=True)
    title = models.CharField(max_length=250)
    category_url = models.URLField()

    def __str__(self):
        return self.title


class HallCard(models.Model):

    
    Hospitality_Services = [
        ('Yes','Yes'),
        ('No',' No')
    ]
    sound_status = [
        ('Yes','Yes'),
        ('No',' No')
    ]

    photo_hall = models.ImageField(upload_to ='photos',null=True,blank=True)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    phone = models.CharField(max_length=12,null=True,blank=True)
    HospitalityServices = models.CharField(choices=Hospitality_Services,max_length=50,null=True,blank=True)
    provider = models.CharField(max_length=50,null=True,blank=True)
    hallto = models.CharField(max_length=100,blank=True,null=True,default='To Women and Man ')
    Total_capacity = models.IntegerField(null=True,blank=True)
    Sound_system = models.CharField(choices=sound_status,max_length=50,null=True,blank=True)
    info = models.TextField(null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    book_url = models.URLField(blank=True,null=True,default='http://127.0.0.1:8000/contact/')
    #category = models.ForeignKey(Categories,on_delete=models.CASCADE,null=True,blank=True,default=3)

    def __str__(self):
        return self.name


class SessionCard(models.Model):
    photo_session = models.ImageField(upload_to ='session',null=True,blank=True)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    phone = models.CharField(max_length=12,null=True,blank=True)
    Photographer = models.CharField(max_length=50,null=True,blank=True)
    info = models.TextField(null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    book_url = models.URLField(blank=True,null=True,default='http://127.0.0.1:8000/contact/')
    #category = models.ForeignKey(Categories,on_delete=models.CASCADE,null=True,blank=True,default=3)


    def __str__(self):
        return self.name

class MakeupCard(models.Model):
    photo_makeup = models.ImageField(upload_to ='makeup',null=True,blank=True)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    phone = models.CharField(max_length=12,null=True,blank=True)
    service_provide = models.CharField(max_length=50,null=True,blank=True)
    TimeToAppointment = models.CharField(max_length=50,null=True,blank=True)
    info = models.TextField(null=True,blank=True)
    Administrator = models.CharField(null=True,blank=True,max_length=50)
    address = models.CharField(max_length=50,null=True,blank=True)
    book_url = models.URLField(blank=True,null=True,default='http://127.0.0.1:8000/contact/')
    #category = models.ForeignKey(Categories,on_delete=models.CASCADE,null=True,blank=True,default=3)


    def __str__(self):
        return self.name


class ServicesCard(models.Model):
    photo_services = models.ImageField(upload_to ='services',null=True,blank=True)
    service = models.CharField(max_length=250)
    service_url = models.URLField()

    def __str__(self):
        return self.service

class About(models.Model):
    photo_about = models.ImageField(upload_to ='about',null=True,blank=True)
    heading_hero = models.CharField(max_length=250)
    title_hero = models.TextField()

    def __str__(self):
        return self.heading_hero

class Banner(models.Model):
    banner_image = models.ImageField(upload_to ='banner',null=True,blank=True)
    heading = models.CharField(max_length=250)
    title = models.TextField()

    def __str__(self):
        return self.heading




class FeaturedProduct(models.Model):
    product_image = models.ImageField(upload_to ='banner',null=True,blank=True)
    product_name = models.CharField(max_length=250)
    product_description = models.TextField()
    product_reviews = models.IntegerField()
    product_price = models.DecimalField(max_digits=7,decimal_places=2)
    product_url = models.URLField()

    def __str__(self):
        return self.product_name


class Footer(models.Model):
    Address = models.CharField(max_length=300)
    phone = models.IntegerField()
    email = models.EmailField()
    social_icon = models.ImageField(upload_to ='footer',null=True,blank=True)
    icon_url = models.URLField(null=True,blank=True)
    copyright = models.TextField(max_length=300)



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(blank=True,null=True)
    subject = models.CharField(max_length=250)
    service = models.ForeignKey(Categories,on_delete = models.CASCADE,blank=True,null=True)
    hall_card = models.ForeignKey(HallCard,on_delete = models.CASCADE,blank=True,null=True)
    session_card = models.ForeignKey(SessionCard,on_delete = models.CASCADE,blank=True,null=True)
    makeup_card = models.ForeignKey(MakeupCard,on_delete = models.CASCADE,blank=True,null=True)
    date = models.DateTimeField(default=datetime.now,blank=True,null=True)

    message = models.TextField()

    def __str__(self):
        return self.name


