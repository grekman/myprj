# -*- coding: utf-8 -*-
""" models of blog app
"""
from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from tinymce.models import HTMLField

class Category(models.Model):
    """ Category in admin page
    """
    name = models.CharField(max_length=100, verbose_name='name')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='slug')

    description = models.TextField(max_length=4096)

    views_count = models.IntegerField(default=0, verbose_name='views count')

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    """ tags in admin page
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='slug')

    views_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    """ articles in admin page
    """
    DRAFT = 'D'
    PUBLISHED = 'P'
    EXPIRED = 'E'
    ARTICLE_STATUS = (
        (DRAFT, 'Not Reviewed'),
        (PUBLISHED, 'Published'),
        (EXPIRED, 'Expired'),
    )


    def was_published_recently(self):
        """ field in admin page
        """
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'publish_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='slug')

    status = models.CharField(max_length=1, choices=ARTICLE_STATUS, default=DRAFT)
    enable_comment = models.BooleanField(default=True)
    content = models.TextField()

    category = models.ForeignKey(Category, verbose_name="the related category")
    tags = models.ManyToManyField(Tag, verbose_name="the related tags", blank=True)

    publish_date = models.DateTimeField(auto_now=False, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")

    created_date = models.DateTimeField(auto_now_add=False)

    views_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
