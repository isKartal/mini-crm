import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Customer, Deal, Note
from faker import Faker

class Command(BaseCommand):
    help = 'Generate fake data for testing'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of customers to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker(['tr_TR'])  # Turkish locale
        
        # Get the first user or creating one if none exists (for development)
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR('No user found! Please create a user first.'))
            return

        self.stdout.write(self.style.SUCCESS(f'Generating {total} customers for user: {user.username}...'))

        for _ in range(total):
            # Create Customer
            customer = Customer.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number()[:20],
                address=fake.address(),
                created_by=user
            )

            # Create Deals (0 to 3 per customer)
            for _ in range(random.randint(0, 3)):
                status = random.choice([choice[0] for choice in Deal.STATUS_CHOICES])
                Deal.objects.create(
                    customer=customer,
                    title=f"{fake.company()} - {fake.bs()}",
                    amount=random.uniform(1000, 50000),
                    status=status,
                    created_by=user
                )

            # Create Notes (0 to 5 per customer)
            for _ in range(random.randint(0, 5)):
                Note.objects.create(
                    customer=customer,
                    content=fake.paragraph(),
                    created_by=user
                )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} customers with deals and notes!'))
