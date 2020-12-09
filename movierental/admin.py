from django.contrib import admin
from .models import Account, Actor, Cast, Customer, Movie, Moviequeue, Orders

# Register your models here.
admin.site.register(Account)
admin.site.register(Actor)
admin.site.register(Cast)
admin.site.register(Customer)
admin.site.register(Movie)
admin.site.register(Moviequeue)
admin.site.register(Orders)