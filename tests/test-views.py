from django.test import TestCase

from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="IceCream1", price=30, inventory=40)
        Menu.objects.create(title="IceCream2", price=100, inventory=10)

    def test_getall(self):
        menu_items = Menu.objects.all()       
        expected_count = 3
        self.assertEqual(menu_items.count(), expected_count)