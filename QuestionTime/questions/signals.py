from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from core.utils import generate_random_string
from .models import Question


@receiver(pre_save, sender=Question)
def add_slug_to_question(sender, instance, *args, **kwargs):
    '''
    Fill the "slug" attribute for the Question model using
    the 'slugify' function to obtain the slug of the content
    field.
    To mantain its uniqueness, adds a random string on it.
    '''
    if instance and not instance.slug:
        slug = slugify(instance.content)
        random_string = generate_random_string()
        instance.slug = slug + '-' + random_string
