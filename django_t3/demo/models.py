import datetime
from django.db import models
from django.utils import timezone
from .apps import app_label


class DOptions(models.Model):
    database_name = app_label

    option_id = models.AutoField(primary_key=True)
    option_name = models.CharField(max_length=191, default='', db_index=True)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20, default='yes')

    class Meta:
        db_table = 'd_options'


class DUsers(models.Model):
    database_name = app_label

    id = models.AutoField(primary_key=True)
    user_login = models.CharField(max_length=60, default='', db_index=True)
    user_pass = models.CharField(max_length=255, default='')
    user_nicename = models.CharField(max_length=50, default='', db_index=True)
    user_email = models.CharField(max_length=100, default='', db_index=True)
    user_url = models.CharField(max_length=100, default='', null=True, blank=True)
    user_registered = models.DateTimeField(null=True, blank=True)
    user_activation_key = models.CharField(max_length=255, default='', null=True, blank=True)
    user_status = models.IntegerField(default=0)
    display_name = models.CharField(max_length=250, default='')

    class Meta:
        db_table = 'd_users'


class DUsermeta(models.Model):
    database_name = app_label

    umeta_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(DUsers, related_name='usersmetas', on_delete=models.CASCADE, db_index=True, default=0)
    meta_key = models.CharField(max_length=255, default='', db_index=True)
    meta_value = models.TextField()

    class Meta:
        db_table = 'd_usermeta'


class DPosts(models.Model):
    database_name = app_label

    id = models.AutoField(primary_key=True)
    post_author = models.IntegerField(db_index=True)
    post_date = models.DateTimeField(null=True, blank=True)
    post_date_gmt = models.DateTimeField(null=True, blank=True)
    post_content = models.TextField(null=True, blank=True)
    post_title = models.CharField(max_length=255)
    post_excerpt = models.TextField(default='')
    post_status = models.CharField(max_length=20, default='publish')
    comment_status = models.CharField(max_length=20, default='open')
    ping_status = models.CharField(max_length=20, default='open')
    post_password = models.CharField(max_length=255, default='')
    post_name = models.CharField(max_length=200, default='', db_index=True)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField(null=True, blank=True)
    post_modified_gmt = models.DateTimeField(null=True, blank=True)
    post_content_filtered = models.TextField()
    post_parent = models.IntegerField(default=0, db_index=True)
    guid = models.CharField(max_length=255, default='')
    menu_order = models.IntegerField(default=0)
    post_type = models.CharField(max_length=20, default='post')
    post_mime_type = models.CharField(max_length=100, default='')
    comment_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'd_posts'


class DPostmeta(models.Model):
    database_name = app_label

    meta_id = models.AutoField(primary_key=True)
    post_id = models.IntegerField(db_index=True, default=0)
    meta_key = models.CharField(max_length=255, default='', db_index=True)
    meta_value = models.TextField()

    class Meta:
        db_table = 'd_postmeta'


class DComments(models.Model):
    database_name = app_label

    comment_id = models.AutoField(primary_key=True)
    comment_post_id = models.IntegerField(db_index=True, default=0)
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100, default='')
    comment_author_url = models.CharField(max_length=200, default='')
    comment_author_ip = models.CharField(max_length=100, default='')
    comment_date = models.DateTimeField(null=True, blank=True, db_index=True)
    comment_date_gmt = models.DateTimeField(null=True, blank=True)
    comment_content = models.TextField()
    comment_karma = models.IntegerField(default=0)
    comment_approved = models.CharField(max_length=20, default='1', db_index=True)
    comment_agent = models.CharField(max_length=255, default='')
    comment_type = models.CharField(max_length=20, default='comment')
    comment_parent = models.IntegerField(db_index=True, default=0)
    user_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'd_comments'


class DCommentmeta(models.Model):
    database_name = app_label

    meta_id = models.AutoField(primary_key=True)
    comment_id = models.IntegerField(db_index=True, default=0)
    meta_key = models.CharField(max_length=255, default='', db_index=True)
    meta_value = models.TextField()

    class Meta:
        db_table = 'd_commentmeta'

