from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user=CustomUser(name="gana",email="jayam.ganapathi12@gmail.com",
        is_staff=True,
        is_superuser=True,
        phone="7730098120",
        gender="Male"
        )

        user.set_password("18016")
        user.save()

    dependencies = [
        
    ]

    operations=[
        migrations.RunPython(seed_data),
    ]