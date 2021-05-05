from django.shortcuts import render
from .models import need, services, values, contact, softwares, features, company, members, about, header
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def need_view(request):
    instance = features.objects.all()
    need_list = []
    for obj in instance:
        need_dict = {
            "name": obj.content.split(",")
        }
        need_list.append(need_dict)
    context = {
        "key": need_list
    }
    return render(request, "index.html", context)



def serives_id(request, id):
    instance = services.objects.get(pk=id)
    instance_0 = services.objects.all()
    instance_1 = header.objects.all()
    instance_2 = softwares.objects.all()
    name = instance.name
    thumb_image = instance.thumb_image
    description_1 = instance.description_1
    description_2 = instance.description_2
    description_3 = instance.description_3
    head_1 = instance.head_1
    head_1_info = instance.head_1_info.split(";")
    head_2 = instance.head_2
    head_2_info = instance.head_2_info.split(";")
    image_1 = instance.image_1
    image_2 = instance.image_2
    image_active = instance.image_active
    context = {
        "name": name,
        "thumb_image": thumb_image,
        "description_1": description_1,
        "description_2": description_2,
        "description_3": description_3,
        "head_1": head_1,
        "head_1_info": head_1_info,
        "head_2": head_2,
        "head_2_info": head_2_info,
        "title": name,
        "image_1": image_1,
        "image_2": image_2,
        "image_active": image_active,
        'services': instance_0,
        'header': instance_1,
        'softwares': instance_2
    }
    return render(request, "services_id.html", context)


def contact_view(request):
    ins = contact.objects.all()
    need_ins = need.objects.all()
    instance_1 = softwares.objects.all()
    instance_2 = services.objects.all()
    need_list = []
    for obj in need_ins:
        need_dict = {
            "need": obj,
            "active": True
        }
        need_list.append(need_dict)

    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        number = request.POST['number']
        email = request.POST['email']
        message = request.POST['message']
        need_value = request.POST['need']
        get_need_ins = need.objects.get(name=need_value)
        obj = contact.objects.create(need=get_need_ins, first_name=firstname, last_name=lastname, number=number, email_id=email, message=message)
        obj.save()
        contextq = {
            'key' : "<em>Thanks</em> for contacting us!<br>We will get back to you soon!",
            'first_name': firstname,
            'title': "Contact",
            "need": need_list,
            'softwares': instance_1,
            'services': instance_2,
            "bg": "lightyellow"
        }
        send_mail('Request Received to us - SAM CADDesign', 'Thanks for Contacting us! We will get back to you soon..!', 'munigopalakrishna@gmail.com', [email], fail_silently=False)
        return render(request, "form.html", contextq)
   
    context = {
        'key': "",
        'title': "Contact",
        "need": need_list,
        'softwares': instance_1,
        'services': instance_2,
        "bg": "grey"
    }
    return render(request, "form.html", context)

def softwares_view(request):
    instance = services.objects.all()
    instance_1 = softwares.objects.all() 
    context = {
        'softwares': instance_1,
        'services': instance,
        "title": "Softwares"
    }
    return render(request, "softwares.html", context)


def softwares_id(request, id):
    instance = softwares.objects.get(pk=id)
    instance_0 = services.objects.all()
    instance_1 = softwares.objects.all()
    instance_2 = instance.head.all()
    name = instance.name
    thumb_image = instance.thumb_image
    logo = instance.logo
    description_1 = instance.description_1
    description_2 = instance.description_2
    description_3 = instance.description_3
    description_4 = instance.description_4
    description_active = instance.description_active
    image_1 = instance.image_1
    image_2 = instance.image_2
    image_active = instance.image_active
    head_list = []
    for obj_2 in instance_2:
        head_dict = {
            "head": obj_2.head,
            "content": obj_2.content.split(";")
        }
        head_list.append(head_dict)
    context = {
        "name": name,
        "thumb_image": thumb_image,
        "logo": logo,
        "description_1": description_1,
        "description_2": description_2,
        "description_3": description_3,
        "description_4": description_4,
        "description_active": description_active,
        "title": name,
        "image_1": image_1,
        "image_2": image_2,
        "image_active": image_active,
        'head': head_list,
        'services': instance_0,
        'softwares': instance_1
    }
    return render(request, "softwares_id.html", context)


def services_view(request):
    instance = services.objects.all()
    instance_1 = softwares.objects.all()        
    context = {
        "services": instance,
        'softwares': instance_1,
        "title": "Services",        
    }
    return render(request, "services.html", context)


def header_view(request):
    instance = header.objects.all()
    instance_1 = services.objects.all()
    instance_2 = softwares.objects.all()
    instance_3 = company.objects.all()
    context = {
        'header': instance,
        'services': instance_1,
        'softwares': instance_2,
        'company': instance_3,
        'title': "Home"
    }
    return render(request, "base.html", context)
