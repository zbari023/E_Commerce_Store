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
            image = f'brand/{images[random.randint(0,24)]}'
        )
    print(f'{n} Brands was Created succesfuly ...')
        
def seed_product(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg','19.jpg','20.jpg','21.jpg','22.jpg','23.jpg','24.jpg','25.jpg']
    flag_types = ['New','Feature','Sale']
    for x in range(n):  
        Product.objects.create(
            name = fake.name(),
            description = fake.text(max_nb_chars=30000),
            sku = random.randint(100,100000),
            price = round(random.uniform(01.99,99.99),2),
            subtitle = fake.text(max_nb_chars=600),
            image = f'products/{images[random.randint(0,24)]}',
            brand = Brand.objects.get(id=random.randint(0,283)),
            flag = flag_types[random.randint(0,2)],
            
        )
    print(f'{n} Products was Created succesfuly ...')


# seed_brand(24)

seed_product(44)