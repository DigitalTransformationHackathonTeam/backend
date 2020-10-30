from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates grid for city"

    def handle(self, *args, **kwargs):
        print("Test command", flush=True)
