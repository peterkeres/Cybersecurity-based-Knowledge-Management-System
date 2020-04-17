# Generated by Django 3.0.4 on 2020-04-05 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0013_countermeasure'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attacker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attackerType', models.CharField(max_length=200)),
                ('vulnerabilityKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KnowledgeBase.Vulnerability')),
            ],
        ),
    ]