# Generated by Django 4.1.5 on 2023-02-21 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0002_cheese_alter_pizza_crust_alter_pizza_sauce_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('added', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='templates.topping'),
        ),
    ]
