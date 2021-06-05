from django.test import TestCase

from pcf.models import Customer


class CustomerTest(TestCase):

    def test_customer_creation(self):
        """
        Test that customer can be created
        """
        name = 'Lazarus Henry'
        email = 'laz@gmail.com'
        subscription = 'Free'

        customer = Customer.objects.create(name=name, email=email, subscription=subscription)

        self.assertIs(customer.name, name)
