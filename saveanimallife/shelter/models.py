from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    # Required
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Custom
    position = models.CharField(max_length=10, default="unverified")
    name = models.CharField(max_length=15, default="")
    surname = models.CharField(max_length=15, default="")
    deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return reverse('user', kwargs={'userslug': self.username})


class Animal(models.Model):
    name = models.CharField(max_length=30, default="")
    kind = models.CharField(max_length=15)
    breed = models.CharField(max_length=50)
    age = models.IntegerField(default="")
    color = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    discription = models.TextField(default='')
    health = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    favorite = models.ManyToManyField(Account, default=None, blank=True)
    fav_count = models.BigIntegerField(default='0')
    block_registration = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('animal', kwargs={'animalid': self.pk})

    class Meta:
        ordering = ('-added',)


class Walk(models.Model):
    status = models.CharField(max_length=14, default="free")
    walker = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=False, blank=False)
    starting = models.DateTimeField(null=False, blank=False)
    ending = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return str(self.id) + " " + str(self.starting)

    class Meta:
        ordering = ('-starting',)


class Task(models.Model):
    status = models.CharField(max_length=14, default="created")
    vet = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    task_start = models.DateTimeField(default=None, null=True)
    task_end = models.DateTimeField(default=None, null=True)
    created = models.DateTimeField(default=None, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('-created',)


class Fundraising(models.Model):
    amount = models.FloatField(null=False, blank=False)
    current_amount = models.FloatField(null=False, blank=False, default=0)
    description = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    end = models.BooleanField(default=False)

    def __str__(self):
        return str(self.description)

    class Meta:
        ordering = ('-created',)

class WalkDays(models.Model):
    date = models.DateField(null=False, blank=False, default=0)
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE, null=False, blank=False)
    time = models.CharField(max_length=100,default=None, null=True)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE, default=None, null=True)
 
    def __str__(self):
        return str(self.id) + " " + str(self.user_id) + " " + str(self.time)

    class Meta:
        ordering = ('date',)


class Donation(models.Model):
    fundraising = models.ForeignKey(Fundraising, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.FloatField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created)

    class Meta:
        ordering = ('-created',)
