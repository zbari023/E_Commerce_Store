import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random 
from products.models import Product , Brand


def seed_brand(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg','19.jpg','20.jpg','21.jpg','22.jpg','23.jpg','24.jpg','25.jpg']
    for x in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f'brand/{images[random.randint(1, 25)]}'
            
            
        )
    print(f'{n} Brands was Created succesfuly ...')
        
def seed_product(n):
    pass

seed_brand(2)