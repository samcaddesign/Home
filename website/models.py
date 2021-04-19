from django.db import models

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
    profile = models.CharField(max_length=50, null=True)
    profile_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class about (models.Model):
    about_active = models.BooleanField(default=True)
    heading = models.CharField(max_length=50)
    description_1 = models.TextField(blank=True)
    description_2 = models.TextField(blank=True)

    def __str__(self):
        return self.heading

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
    name = models.CharField(max_length=50)
    thumb_image = models.ImageField()
    name_active = models.BooleanField(default=True)
    description_1 = models.TextField()
    description_2 = models.TextField(null=True)
    role = models.TextField()
    image_active = models.BooleanField(default=True)
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    tools = models.TextField()

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
    description_2 = models.TextField()
    description_active = models.BooleanField(default=True)
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    logo = models.ImageField()
    # image_3 = models.ImageField()
    head = models.ManyToManyField('features')
    
    def __str__(self):
        return self.name

class values (models.Model):
    image = models.ImageField()
    count = models.TextField()
    name = models.CharField(max_length=50)
    quote = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class progress (models.Model):
    name = models.ForeignKey('services', on_delete=models.CASCADE, null=True)
    percentage = models.CharField(max_length=10)

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
    name = models.ForeignKey('need', on_delete=models.CASCADE, null=True)
    message = models.TextField()

    def __str__(self):
        return self.first_name


