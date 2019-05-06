import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first.settings')

import django
django.setup()

import random
from first_app.models import info
from faker import Faker

fakethis = Faker()
def populate():
    a = fakethis.name().split(' ')
    q_name = a[0]
    w_name = a[1]
    aemail = fakethis.email()

    info.objects.get_or_create(f_name=q_name,l_name=w_name,email=aemail)
print('1')
for i in range(10):
    populate()
print('0')
