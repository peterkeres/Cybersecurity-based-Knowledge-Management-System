# Generated by Django 2.2.6 on 2020-04-20 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0018_auto_20200420_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnerability',
            name='ciaaKey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='KnowledgeBase.CiaaCategory'),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='countermeasureKey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='KnowledgeBase.Countermeasure'),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='severityLevelKey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='KnowledgeBase.SeverityLevel'),
        ),
    ]