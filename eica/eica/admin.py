from django.contrib import admin
from django.apps import apps

ban = ['django_session',
       'django_migrations',
       'django_content_type',
       'auth_user_user_permissions',
       'auth_group',
       'auth_group_permissions',
       'auth_permission',
       'auth_user',
       'auth_user_groups',
       'django_admin_log']

models = apps.get_models()

for model in models:
    if model._meta.db_table not in ban:
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass
