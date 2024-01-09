# initdata.py

from django.core.management.base import BaseCommand
from HotWheelz.models import CarBrand, CarModel, Collection, Owner

class Command(BaseCommand):
    help = 'Initialize data for HotWheelz app'

    def handle(self, *args, **options):
        # Create Car Brands
        ferrari = CarBrand.objects.create(name='Ferrari')
        lamborghini = CarBrand.objects.create(name='Lamborghini')
        honda = CarBrand.objects.create(name='Honda')
        mclaren = CarBrand.objects.create(name='McLaren')
        porsche = CarBrand.objects.create(name='Porsche')

        # Create Car Models
        ferrari_model = CarModel.objects.create(brand=ferrari, name='Ferrari GT', description='A powerful GT car from Ferrari.')
        lambo_model = CarModel.objects.create(brand=lamborghini, name='Lamborghini Aventador', description='The iconic Aventador from Lamborghini.')
        honda_model = CarModel.objects.create(brand=honda, name='Honda Civic', description='The popular Civic model from Honda.')
        mclaren_model = CarModel.objects.create(brand=mclaren, name='McLaren 720S', description='The sleek and fast 720S from McLaren.')
        porsche_model = CarModel.objects.create(brand=porsche, name='Porsche 911', description='Classic Porsche 911 sports car.')

        # Create Collections
        collection_gt = Collection.objects.create(name='GT Collection')
        collection_gt.cars.add(ferrari_model, lambo_model)

        collection_sports = Collection.objects.create(name='Sports Collection')
        collection_sports.cars.add(honda_model, mclaren_model, porsche_model)

        # Create Owners
        owner_john = Owner.objects.create(name='John Doe', collection=collection_gt)
        owner_emma = Owner.objects.create(name='Emma Smith', collection=collection_sports)

        self.stdout.write(self.style.SUCCESS('Data successfully initialized.'))
