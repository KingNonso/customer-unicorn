from django.contrib import messages
from django_unicorn.components import UnicornView

from pcf.forms import CustomerForm
from pcf.models import Customer, SUBSCRIPTION_TYPE


class CustomerView(UnicornView):
    form_class = CustomerForm
    name = ""
    email = ""
    subscription = ""
    subscriptions = []
    customers = []

    def mount(self):
        self.customers = Customer.objects.all()
        self.subscriptions = [s[0] for s in SUBSCRIPTION_TYPE]

    def save(self):
        if self.is_valid():  # checks with the form class for server side validation
            # print(self.name, self.email)
            customer = Customer(name=self.name, email=self.email, subscription=self.subscription)
            customer.save()
            self.customers = Customer.objects.all()
            messages.success(self.request, "Customer was created successfully")
            self.name = ''
            self.email = ''
            self.subscription = ''
        else:
            messages.error(self.request, "There was a problem with your last request")

    def update(self, idx: int):  # not implemented
        self.customers[idx].save()
