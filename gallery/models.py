
from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    @classmethod
    def get_locations_id(cls, id):
        locations = Location.objects.all(pk=id)
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.name = update
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=50)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk=id)
        return category

    def __str__(self):
        return self.name 