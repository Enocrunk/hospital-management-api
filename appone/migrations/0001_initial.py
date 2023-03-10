# Generated by Django 3.2.15 on 2022-12-13 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apptwo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('start_time', models.TimeField(auto_now_add=True, null=True)),
                ('end_time', models.TimeField(auto_now_add=True, null=True)),
                ('desc', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.TextField(max_length=15, null=True)),
                ('rooms', models.IntegerField()),
                ('location', models.CharField(max_length=50, null=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptwo.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True, verbose_name='gender')),
                ('d_o_b', models.DateTimeField(auto_now_add=True, verbose_name='Date of Birth')),
                ('phone', models.IntegerField(unique=True, verbose_name='phone number')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('photo', models.ImageField(upload_to=None, verbose_name='image')),
                ('work_hrs', models.CharField(max_length=250, null=True, verbose_name='working hours')),
                ('equipment', models.TextField(max_length=50, null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.appointment', verbose_name='appointments')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.branche')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('mr.', 'Mr.'), ('mrs.', 'Mrs.'), ('miss', 'Miss')], max_length=10, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.TextField(max_length=15, null=True)),
                ('address', models.TextField(max_length=15, null=True)),
                ('allargies', models.TextField(blank=True, max_length=100, null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.appointment')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.branche')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.doctor')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptwo.payment')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_id', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=25, null=True)),
                ('cost', models.PositiveIntegerField()),
                ('suggested_price', models.PositiveIntegerField()),
                ('batch_details', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('desc', models.TextField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.TimeField(auto_now_add=True)),
                ('time_out', models.TimeField(auto_now_add=True)),
                ('line', models.IntegerField(choices=[(1, 'Dematology'), (2, 'Allergy and Immuninology'), (3, 'Cardiolog'), (4, 'Dentist'), (5, 'Dentist')], null=True)),
                ('status', models.TextField(max_length=50, null=True)),
                ('wait_time', models.TextField(max_length=50, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.patient')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.doctor')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='visits',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appone.visit'),
        ),
    ]
