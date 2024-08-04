from django.core.management import call_command
from django.core.management.base import BaseCommand

# This command is used to load the sample_user_data.json file into the database.
# Fixture - A fixture is a collection of data that Django knows how to import into a database.
# It must be in JSON format.
# Naming of db_user_fixture.json is arbitrary. You can name it anything you want.
# However, the project structure must be the appname > fixtures > db_user_fixture.json, management > commands > user-fixture.py
# As for the user-fixture.py, you can name it anything you want.
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "db_user_fixture.json")