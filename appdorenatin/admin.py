
from django.contrib import admin
from .models import Nacional
from .models import Artilheiro

# registra no admin os models e suas informações para serem criados lá por meio do login (usuário do createsuperuser)
admin.site.register(Nacional)
admin.site.register(Artilheiro)
# Register your models here.
