from django.contrib import admin
from django.db.models import get_models, get_app
# Register your models here.

from member.models import *

for model in get_models(get_app('member')):
    admin.site.register(model)
