# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import django.utils.timezone
from django.conf import settings
import django.core.validators
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('display_name', models.CharField(max_length=50)),
                ('modification_date', models.DateTimeField(null=True)),
                ('language', models.CharField(max_length=50)),
                ('avatar', models.ImageField(null=True, upload_to=b'avatars/', blank=True)),
                ('website', models.URLField(null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
                ('position', positions.fields.PositionField(default=-1)),
            ],
            options={
                'ordering': ['position'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('main_image', models.ImageField(upload_to=b'images/recipe/')),
                ('serves', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('notes', models.TextField(null=True)),
                ('language', models.CharField(max_length=50)),
                ('is_published', models.BooleanField(default=False)),
                ('is_draft', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(related_name=b'recipes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=b'images/recipe/', blank=True)),
                ('position', positions.fields.PositionField(default=-1)),
                ('recipe', models.ForeignKey(related_name=b'steps', to='core.Recipe')),
            ],
            options={
                'ordering': ['position'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(related_name=b'ingredients', to='core.Recipe'),
            preserve_default=True,
        ),
    ]
