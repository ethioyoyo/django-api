import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostgen01.settings')

from faker import Faker

import django
django.setup()

from hostgenapp.models import hosts
faker = Faker()

def populate(N=5):
   for entry in range(N):
      fake_host_name = faker.first_name()
      fake_ip = faker.ipv4()

      fake_hosts = hosts.objects.get_or_create(h_host=fake_host_name,h_ip=fake_ip)[0]


if __name__ == '__main__':
   print("Populating hosts...")
   populate(20)
   print("complete...")
