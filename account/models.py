from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email, name, date_of_birth, date_of_join, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not date_of_join:
            raise ValueError('Soldier must have Join date')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            date_of_birth=date_of_birth,
            date_of_join=date_of_join,
        )
        user.is_admin = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, date_of_birth, date_of_join, password):
        user = self.create_user(
            email,
            password=password,
            name=name,
            date_of_birth=date_of_birth,
            date_of_join=date_of_join,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    date_of_join = models.DateField()
    is_air_force = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'date_of_birth', 'date_of_join']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin