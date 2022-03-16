from django.contrib import admin
from .models import Casting
from .models import Character
from .models import Casting_Vote
from .models import Character_Vote
#from django.contrib.auth.models import User
#
# Register your models here.
# admin.site.unregister(User)
#admin.site.register(User)
admin.site.register(Casting)
admin.site.register(Character)
admin.site.register(Casting_Vote)
admin.site.register(Character_Vote)