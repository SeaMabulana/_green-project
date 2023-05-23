# from django.shortcuts import render
# from _fundraiser.models import Event, UserEvent, Beneficiary, BeneficiaryClaim
# from _users.models import User, UserWallet
# import random

# def event_types():
#   item_list = [
#     'fundraiser',
#     'donor'
#   ]
#   return item_list

# for event in event_types():
#   if not Event.objects.filter(event_name=event, is_active=True):
#     x = Event.objects.create(event_name=event, is_active=True)
#     x.save()
