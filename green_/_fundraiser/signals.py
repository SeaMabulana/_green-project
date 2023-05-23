# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from .models import Event, UserEvent, Beneficiary, BeneficiaryClaim
# from .views import event_types
# import random


# @receiver(post_save, sender=UserEvent)
# def user_event(sender, instance, **kwargs):
#   for event in event_types():
#     event_obj = Event.objects.filter(event_name=event, is_active=True)
#     if event_obj.exists():
#       get_event = event_obj.get()
#       if get_event.user.all().count() == 2:
#         event_obj.update(is_active=False)
#         new_event = Event.objects.create(event_name=get_event.event_name, is_active=True)
#         new_event.save()
#     process_event = Event.objects.filter(is_active=False, is_processed=False)
#     if process_event.exists():
#       user_ = UserEvent.objects.filter(event_id__is_active=False, event_id__is_processed=False)
#       beneficiary = random.choice(user_)
#       Beneficiary.objects.create(user_event=beneficiary)
#       process_event.update(is_processed=True)

# @receiver(post_save, sender=BeneficiaryClaim)
# def beneficiary_claim(sender, instance, **kwargs):
#   x = Beneficiary.objects.filter(id=instance.beneficiary.id)
#   x.update(is_claimed=True)
