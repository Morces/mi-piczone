from unicodedata import category
from django.test import TestCase

from gallery.models import Category, Image, Location

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Africa')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.location.save_location()
        self.location.delete_location()
        local = Location.objects.all()
        self.assertTrue(len(local)> 0)

    def test_update_method(self):
        locay = Location.get_locations_id(self.location.id)
        locay.update_location('Asia')
        locay = Location.get_locations_id(self.location.id)
        self.assertTrue(locay.name == 'Asia')

class CategoryTestClass(TestCase):
    def setUp(self):
        self.cat = Category(name='Fashion')
        self.cat.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))

    def test_save_method(self):
        self.cat.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        self.cat.save_category()
        self.cat.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update_method(self):
        category = Category.get_category_id(self.cat.id)
        category.update_category('Fun')
        category = Category.get_category_id(self.cat.id)
        self.assertTrue(category.name == 'Fun')


class ImageTestCase(TestCase):
    def setUp(self):
        self.cat = Category(name='Fashion')
        self.cat.save_category()

        self.location = Location(name='Asia')
        self.location.save_location()

        self.image = Image(name='testing', description='image testing', image_location=self.location,image_category=self.cat)
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.iamge, Image))

    def tearDown(self):
        self.image.delete_image()
        self.cat.delete_category()
        self.location.delete_location()

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

    def test_get_image_by_id(self):
        images = Image.get_image_by_id(self.image.id)
        self.assertTrue(len(images)==1)

    def test_search_by_category(self):
        images = Image.filter_by_location('1')
        self.assertTrue(len(images)>0)

    def test_update_image(self):
        self.iamge.save_image()
        image = Image.update_image(self.image.id, 'test update', 'image testing', self.location, self.cat)
        upimage = Image.objects.filter(id= self.image.id)
        self.assertTrue(Image.name=='test update', upimage=upimage, image=image)


