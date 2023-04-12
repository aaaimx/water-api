# Generated by Django 3.2.6 on 2023-04-12 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('states', '0003_alter_state_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_consult', models.DateField()),
                ('lat', models.DecimalField(decimal_places=4, max_digits=6)),
                ('long', models.DecimalField(decimal_places=4, max_digits=6)),
                ('year_consult', models.IntegerField(max_length=4)),
                ('state_consult', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.state')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
