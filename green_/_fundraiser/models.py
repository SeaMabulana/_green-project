from django.db import models
from _users.models import User
import datetime
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

import random
import string

class Event(models.Model):
  user = models.ManyToManyField(User, through='UserEvent', related_name='user')
  event_name =  models.CharField(max_length=150, null=True, blank=True)
  reference_token = models.CharField(
    unique=True, 
    max_length=32,
    editable=False,  
    null=True, 
    blank=True
  )
  poll_date = models.DateTimeField(auto_now_add=True)
  due_date = models.DateTimeField(null=True, blank=True, editable=False)
  is_active = models.CharField(max_length=150, default=True, editable=False)
  is_processed = models.CharField(max_length=150, default=False, editable=False)


  class Meta:
    verbose_name_plural = 'Events'

  def __str__(self) -> str:
    return f'[ {self.event_name} ] [ {self.reference_token} ]'

  # https://docs.djangoproject.com/en/4.1/topics/db/models/#overriding-predefined-model-methods
  # override Event due_date
  # override Event reference_token
  def save(self, *args, **kwargs) -> None:
    if not self.due_date:
      x = datetime.datetime.now() + datetime.timedelta(days=7)
      self.due_date = x
    _chars = ''.join((string.ascii_letters, string.digits))
    unique_token = str(''.join(random.choice(_chars) for _ in range(32)))
    while Event.objects.filter(ref_token=unique_token).exists():
      unique_token += str(''.join(random.choice(_chars) for _ in range(32)))
    else:
      self.reference_token = unique_token
    super(Event, self).save(*args, **kwargs)

class UserEvent(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  count = models.PositiveIntegerField(editable=False, null=True, blank=True)

  class Meta:
    verbose_name_plural = 'User Events'

  def __str__(self) -> str:
    return f'[ {self.user} ] [ {self.event} ]'
  
@receiver(pre_save, sender=UserEvent)
def user_event_count(sender, instance, **kwargs):
    try:
      obj = UserEvent.objects.filter(event=instance.event).count()
      instance.count = obj + 1
    except:
      instance.count = 1


class Beneficiary(models.Model):
  user_event = models.ForeignKey(UserEvent, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  funds = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
  is_claimed = models.CharField(max_length=10, default=False, editable=False) 


  class Meta:
    verbose_name_plural = 'Beneficiaries'
  
  def __str__(self) -> str:
    return f'[ {self.user_event} ] [ {self.date} ]'


class BeneficiaryClaim(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  date = models.DateTimeField(auto_now_add=True)
  beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)


  class Mwta:
    verbose_name_plural = 'Beneficiary Claims'

  def __str__(self) -> str:
    return f'[ {self.user} ] [ {self.date} ] [ {self.beneficiary} ]'
