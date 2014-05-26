from django.db.models import signals
from mrwolfe import models


def create_settings(**kwargs):
    models.Setting.objects.get_or_create(name='notification',
                                         defaults={'value': 'on'})


signals.post_syncdb.connect(create_settings, sender=models)
