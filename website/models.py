from django.db import models
from django.contrib.auth.forms import User

class company (models.Model):
    name = models.CharField(max_length=15)
    head = models.CharField(max_length=15)
    logo = models.ImageField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    mailid = models.CharField(max_length=30)
    skypeid = models.CharField(max_length=15)
    location = models.TextField()

    def __str__(self):
        return self.name

class members (models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50, null=True)
    image = models.ImageField(default=True)
    profile = models.CharField(max_length=50, null=True)
    twitter = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    profile_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class aboutus (models.Model):
    about_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    description_1 = models.TextField()
    description_2 = models.TextField()
    description_3 = models.TextField(blank=True)
    description_4 = models.TextField(blank=True)
    disclaimer = models.TextField(default=True)
    mission = models.TextField(default=True)
    vision = models.TextField(default=True)

    def __str__(self):
        return self.name

class header (models.Model):
    # header_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    name_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class carousel (models.Model):
    carousel_active = models.BooleanField(default=True)
    head_1 = models.CharField(max_length=50, blank=True)
    head_2 = models.TextField(blank=True)
    head_3 = models.TextField(blank=True)
    image = models.ImageField()
    image_active = models.BooleanField(default=True)

    def __str__(self):
        return self.head_1

class marquee (models.Model):
    info = models.TextField()
    info_active = models.BooleanField(default=True)
    logo = models.ImageField()
    logo_active = models.BooleanField(default=True)

    def __str__(self):
        return self.info

class services (models.Model):
    services_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, null=True)
    percentage = models.CharField(default=True, max_length=3)
    thumb_image = models.ImageField()
    name_active = models.BooleanField(default=True)
    description_1 = models.TextField()
    description_2 = models.TextField(null=True, blank=True)
    description_3 = models.TextField(null=True, blank=True)
    head_1 = models.CharField(max_length=100, null=True)
    head_1_info = models.TextField(null=True)
    image_active = models.BooleanField(default=True)
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    head_2 = models.CharField(max_length=100, null=True)
    head_2_info = models.TextField(null=True)

    def __str__(self):
        return self.name

class features (models.Model):
    head = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.head

class softwares (models.Model):
    softwares_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    thumb_image = models.ImageField()
    description_1 = models.TextField()
    description_2 = models.TextField(null=True, blank=True)
    description_3 = models.TextField(null=True, blank=True)
    description_4 = models.TextField(blank=True)
    description_active = models.BooleanField(default=True)
    image_active = models.BooleanField(default=True)
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    logo = models.ImageField()
    head = models.ManyToManyField('features')
    
    def __str__(self):
        return self.name

class values (models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50, default=True)
    count = models.CharField(max_length=50)
    quote = models.CharField(max_length=100)
    description_1 = models.TextField(blank=True)

    def __str__(self):
        return self.name

class need (models.Model):
    name = models.CharField(max_length=100, default=True)

    def __str__(self):
        return self.name

class contact (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    need = models.ForeignKey('need', on_delete=models.CASCADE, null=True)
    message = models.TextField()

    def __str__(self):
        return self.first_name


class user_profile(models.Model):
    
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, default=None)
    gender= models.CharField(max_length=10, default="")
    phone_number = models.CharField(max_length=50)
    # timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.phone_number}'