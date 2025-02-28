# Generated by Django 5.1.6 on 2025-02-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('prime_id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('image', models.ImageField(blank=True, default='def.png', upload_to='images/')),
                ('mother_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Hindu', 'Hindu'), ('Khristian', 'Khristian'), ('Buddho', 'Buddho'), ('Atheist', 'Atheist'), ('Others', 'Others')], max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('date_of_birth', models.DateField()),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('is_Bangladeshi', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
    ]
