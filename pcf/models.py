from django.db import models

SUBSCRIPTION_TYPE = [
    ('Free', 'Free'),
    ('Plus', 'Plus'),
    ('Pro', 'Pro'),
]


class Customer(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subscription = models.CharField(max_length=50, choices=SUBSCRIPTION_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
