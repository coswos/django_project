from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	exclude = [
		"last_login",
		"user_permissions",
		"groups",
		"username",
		"is_staff",
		"is_active",
		"Superuser status",
		"password",
	]

	readonly_fields = [
		"date_joined",
		"email",
	]
