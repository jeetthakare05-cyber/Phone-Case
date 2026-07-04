from django.contrib import admin

from .models import Product
from .models import Suggestion
from .models import Contact , Cart

admin.site.register(Product)

admin.site.register(Suggestion)

admin.site.register(Contact)

admin.site.register(Cart)
