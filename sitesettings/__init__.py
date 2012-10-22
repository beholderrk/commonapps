from django.conf import settings
from django.db.models.signals import post_syncdb
from sitesettings.models import SettingsGroup, Settings
from sitesettings import models as settings_app
import copy

def init_settings():
    if getattr(settings, 'DEFAULT_SITE_SETTINGS', {}):
        DEFAULT_SITE_SETTINGS = copy.deepcopy(settings.DEFAULT_SITE_SETTINGS)
        for d in DEFAULT_SITE_SETTINGS:
            group_settings = d.pop('settings')
            print "Creating Settings Groups %s" % d['code']
            group, created = SettingsGroup.objects.get_or_create(**d)
            for one_conf_d in group_settings:
                default_value = one_conf_d.pop('default')
                print "Creating Settings %s" % one_conf_d['code']
                one_conf, created = Settings.objects.get_or_create(group_id=group.pk, **one_conf_d)
                if created:
                    one_conf.value = default_value
                    one_conf.save()


def create_default_settings(app, created_models, verbosity, db, **kwargs):
    if SettingsGroup in created_models or Settings in created_models:
        init_settings()

post_syncdb.connect(create_default_settings, settings_app)