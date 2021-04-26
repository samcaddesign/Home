from django.shortcuts import render
from .models import need, services, values, contact, softwares, features, company, members, about, header

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
        'softwares_head': instance_2
    }
    return render(request, "services_id.html", context)


def contact_view(request):
    ins = contact.objects.all()
    need_ins = need.objects.all()
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
        need_value    = request.POST['need']
        get_need_ins = need.objects.get(name=need_value)
        obj = contact.objects.create(name=get_need_ins, first_name=firstname, last_name=lastname, number=number, email_id=email, message=message)
        obj.save()
        contextq = {
            'key' : "submitted",
            'title': "form",
            "bg": "lightyellow"
        }
        return render(request, "form.html", contextq)
   
    context = {
        'key': "enter details",
        'title': "form",
        "need": need_list,
        "bg": "grey"
    }
    return render(request, "form.html", context)

def softwares_view(request):
    instance_1 = softwares.objects.all()    
    softwares_list = []
    for obj_1 in instance_1:
        instance_2 = obj_1.head.all()
        head_list = []
        for obj_2 in instance_2:
            head_dict = {
                "head": obj_2.head,
                "content": obj_2.content.split(",")
            }
            head_list.append(head_dict)
        softwares_dict = {
            "name": obj_1.name,
            "head": head_list,
            "image": obj_1.logo
        }
        softwares_list.append(softwares_dict)
    context = {
        "softwares": softwares_list,
        "title": "Softwares"
    }
    return render(request, "soft.html", context)



def services_view(request):
    instance = services.objects.all()
    instance_1 = header.objects.all()
    instance_2 = softwares.objects.all()        
    context = {
        "services": instance,
        'header': instance_1,
        'softwares_head': instance_2,
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
        'softwares_head': instance_2,
        'company': instance_3,
        'title': "Home"
    }
    return render(request, "base.html", context)
