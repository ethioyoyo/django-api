import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostgen01.settings')

from faker import Faker

import django
django.setup()

from hostgenapp.models import hosts
faker = Faker()

def populate(N=5):
   print("Populating hosts...")
   for entry in range(N):
      fake_host_name = faker.first_name()
      fake_ip = faker.ipv4()
      print("generating {}".format(fake_host_name))
      fake_hosts = hosts.objects.get_or_create(h_host=fake_host_name,h_ip=fake_ip)[0]


 

   print("complete...")
