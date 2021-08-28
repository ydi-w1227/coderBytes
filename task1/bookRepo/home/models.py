from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from modelcluster.fields import ParentalManyToManyField
from wagtail.search import index
from django import forms

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class Book(Page):
    name = models.CharField(max_length = 200, blank=True)
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('name'),
    ]

class Author(Page):
    name = models.CharField(max_length = 100, blank=True)
    description = RichTextField(blank=True)
    books = ParentalManyToManyField('book', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('books', widget=forms.CheckboxSelectMultiple),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('name'),
    ]
