from uuid import uuid4

from django.db.models import (CASCADE, BooleanField, CharField, ForeignKey,
                              IntegerField, Model, UUIDField)
from django.utils.translation import gettext_lazy as _

__all__ = [
    'Album',
    'Song'
]


class Album(Model):
    id = UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    title = CharField(
        max_length=100,
        # drf_spectacular ignores trivial title variations
        verbose_name=_("Nice Title"),
        help_text=_("The title of the Album"))
    genre = CharField(
        choices=(('POP', 'Pop'), ('ROCK', 'Rock')),
        max_length=10,
        # drf_spectacular ignores trivial title variations
        verbose_name=_("Nice Genre"),
        help_text=_("Wich kind of genre this Album represents")
    )
    year = IntegerField(
        verbose_name=_("Nice Year"),
        help_text=_("The release year"))
    released = BooleanField(
        verbose_name=_("Nice Released"),
        help_text=_("Is this Album released or not?")
    )


class User(Model):

    username = CharField(max_length=50, primary_key=True)
    password = CharField(max_length=128)

class Song(Model):
    id = UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False)
    title = CharField(
        max_length=100
    )
    length = IntegerField()
    album = ForeignKey(
        to=Album,
        related_name="singles",
        related_query_name="single",
        on_delete=CASCADE
    )
    
    created_by = ForeignKey(
        to=User,
        related_name="singles",
        related_query_name="single",
        on_delete=CASCADE,
    )
