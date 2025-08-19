from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        for i in range(10):
            Listing.objects.create(
                title=f"Sample Listing {i+1}",
                description="This is a sample listing description",
                price_per_night=random.randint(50, 500)
            )
        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
