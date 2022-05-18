from django.apps import AppConfig
import joblib


class LoadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    """
    fashion matching ai model
    """
    classifier = joblib.load('/Users/koh/develop/django/ootd/app/ai/fashion/models/colorfit.pkl')
    scaler = joblib.load('/Users/koh/develop/django/ootd/app/ai/fashion/models/scaler.pkl')
