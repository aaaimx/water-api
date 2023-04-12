# Generated by Django 3.2.6 on 2023-04-12 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crop_products', '0002_suministrytype'),
        ('states', '0003_alter_state_name'),
        ('classification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultClassification',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classification.realclassification')),
                ('crop_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crop_products.cropproduct')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.state')),
                ('sum_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crop_products.suministrytype')),
            ],
        ),
    ]