import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Account(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    accounttype = models.CharField(db_column='AccountType', max_length=15, blank=True, null=True)  # Field name made lowercase.
    viewtimes = models.IntegerField(db_column='ViewTimes', blank=True, null=True)  # Field name made lowercase.
    acccreatetime = models.DateTimeField(db_column='AccCreateTime', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account'


class Actor(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=15)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=6, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actor'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cast(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    actorid = models.ForeignKey(Actor, models.DO_NOTHING, db_column='ActorId')  # Field name made lowercase.
    movieid = models.ForeignKey('Movie', models.DO_NOTHING, db_column='MovieId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cast'


class Customer(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=15)  # Field name made lowercase.
    si = models.CharField(db_column='Si', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gu = models.CharField(db_column='Gu', max_length=10, blank=True, null=True)  # Field name made lowercase.
    creditcard = models.CharField(db_column='CreditCard', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class Movie(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    moviename = models.CharField(db_column='MovieName', max_length=45)  # Field name made lowercase.
    directorname = models.CharField(db_column='DirectorName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    movietype = models.CharField(db_column='MovieType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numcopies = models.IntegerField(db_column='NumCopies', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movie'


class Moviequeue(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.
    movieid = models.ForeignKey(Movie, models.DO_NOTHING, db_column='MovieId')  # Field name made lowercase.
    queuenumber = models.IntegerField(db_column='QueueNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'moviequeue'


class Orders(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.
    movieid = models.ForeignKey(Movie, models.DO_NOTHING, db_column='MovieId')  # Field name made lowercase.
    borrowtime = models.DateTimeField(db_column='BorrowTime')  # Field name made lowercase.
    returntime = models.DateTimeField(db_column='ReturnTime', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'