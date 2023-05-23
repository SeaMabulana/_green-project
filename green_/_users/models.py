from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
  za_id_number = models.CharField(max_length=13, null=True, blank=True)


  class Meta:
    verbose_name_plural = 'User'

  def save(self, *args, **kwargs):
      for field_name in ['first_name', 'last_name']:
          val = getattr(self, field_name, False)
          if val:
              setattr(self, field_name, val.capitalize())
      super(User, self).save(*args, **kwargs)

  def __str__(self) -> str:
    return self.username


class UserWallet(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  tokens = models.BigIntegerField(default=0)


  class Meta:
    ordering = ['user']
    verbose_name_plural = 'User Wallet'
        
  def __str__(self) -> str:
    # avoid [ TypeError: __str__ returned non-string (type User) ] convert to str()
    return str(self.user)

class BankAccount(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  bank_account = models.CharField(max_length=13, null=True, blank=True)
  bank_name = models.CharField(max_length=13, null=True, blank=True)
  phone_number = PhoneNumberField(blank=True)

  class Meta:
    ordering = ['user']
    verbose_name_plural = 'Bank Accounts'

  def __str__(self) -> str:
    return str(self.user)
