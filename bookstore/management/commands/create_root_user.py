from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from bookstore.models import UserProfile

class Command(BaseCommand):
    help = 'Creates the root user profile for the first superuser'

    def handle(self, *args, **options):
        # Get the first superuser
        superuser = User.objects.filter(is_superuser=True).first()
        
        if not superuser:
            self.stdout.write(self.style.ERROR('No superuser found. Please create one first with:'))
            self.stdout.write(self.style.WARNING('python manage.py createsuperuser'))
            return

        # Create or update the user profile
        profile, created = UserProfile.objects.get_or_create(user=superuser)
        profile.is_root_user = True
        profile.save()
        
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created root user profile for {superuser.username}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Updated root user profile for {superuser.username}'))