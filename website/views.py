from django.shortcuts import render
from .models import need, services, values, contact, softwares, features, company, members, about, header

def base_view(request):
    instance_1 = softwares.objects.all()
    instance_2 = services.objects.all()
    softwares_list = []
    service_list = []
    for obj_1 in instance_1:
        instance_3 = obj_1.head.all()
        head_list = []
        for obj_3 in instance_3:
            head_dict = {
                "head": obj_3.head,
                "content": obj_3.content.split(",")
            }
            head_list.append(head_dict)            
        softwares_dict = {
            "name": obj_1.name,
            "head": head_list,
            "image": obj_1.logo
        }
        softwares_list.append(softwares_dict)
        for obj_2 in instance_2:
            service_dict = {
                "name": obj_2.name,
                "id": obj_2.pk,
                "active": obj_2.services_active,
                "images": obj_2.thumb_image,
                "softwares": softwares_list
            }
        service_list.append(service_dict) 
    context = {
        "services": service_list
    }
    return render(request, "base.html", context)

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



def ser_det(request, id):
    instance = services.objects.get(pk=id)
    instance_0 = services.objects.all()
    instance_1 = header.objects.all()
    instance_2 = softwares.objects.all()
    name = instance.name
    thumb_image = instance.thumb_image
    description_1 = instance.description_1
    description_2 = instance.description_2
    role = instance.role.split(",")
    tools = instance.tools.split(",")
    context = {
        "name": name,
        "thumb_image": thumb_image,
        "description_1": description_1,
        "description_2": description_2,
        "role": role,
        "tools": tools,
        "title": name,
        'services': instance_0,
        'header': instance_1,
        'softwares_head': instance_2
    }
    return render(request, "services-industrial-design.html", context)


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
