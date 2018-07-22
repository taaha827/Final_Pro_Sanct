# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.html import format_html

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Brands(models.Model):
    brandname = models.CharField(db_column='BrandName', max_length=50)  # Field name made lowercase.
    brandurl = models.CharField(db_column='BrandURL', max_length=100)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=10)  # Field name made lowercase.
    attribute = models.CharField(db_column='Attribute', max_length=10)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brands'


class DarazData(models.Model):
    filepath = models.CharField(db_column='FilePath', max_length=300)  # Field name made lowercase.
    textread = models.CharField(db_column='TextRead', max_length=300)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=300, blank=True, null=True)  # Field name made lowercase.
    extractiondate = models.DateField(db_column='ExtractionDate', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=100, blank=True, null=True)  # Field name made lowercase.
    percentageoff = models.CharField(db_column='PercentageOff', max_length=5, blank=True, null=True)  # Field name made lowercase.
    salestype = models.CharField(db_column='SalesType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=500)
    brandname = models.CharField(max_length=300)
    bannertype = models.CharField(db_column='BannerType', max_length=6)  # Field name made lowercase.

    def image_tag(self):
        return format_html('<img hieght ="225px" width ="425px" src = "http://%s"/>' %self.address)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    def thumbnail_tag(self):
        return format_html('<img hieght ="280px" width ="280px" src = "http://%s"/>' %self.address)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
        
    class Meta:
        managed = False
        db_table = 'daraz_data'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Warnings(models.Model):
    sentby = models.TextField(db_column='SentBy')  # Field name made lowercase.
    warning = models.CharField(db_column='Warning', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'warnings'
