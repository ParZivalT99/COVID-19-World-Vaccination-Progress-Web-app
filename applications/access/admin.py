from django.contrib import admin
from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "is_active",
        "is_superuser",
        "is_staff",
        "last_login",
        "created_at",
    )
    search_fields = ("username",)
    # list_filter = () #filtro por categorias


admin.site.register(User, UserAdmin)
