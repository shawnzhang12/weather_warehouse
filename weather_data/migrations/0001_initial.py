# Generated by Django 4.1.7 on 2023-04-01 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WideWind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('wind_speed_10m_ms', models.FloatField(blank=True, null=True)),
                ('wind_dir_10_d', models.FloatField(blank=True, null=True)),
                ('wind_gusts_10m_1h_ms', models.FloatField()),
                ('wind_gusts_10m_1h_bft', models.FloatField()),
                ('wind_gusts_10m_1h_kmh', models.FloatField()),
                ('wind_gusts_10m_1h_kn', models.FloatField()),
                ('wind_gusts_10m_24h_ms', models.FloatField()),
                ('wind_gusts_10m_24h_bft', models.FloatField()),
                ('wind_gusts_10m_24h_kmh', models.FloatField()),
                ('wind_gusts_10m_24h_kn', models.FloatField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_data.location')),
            ],
        ),
        migrations.CreateModel(
            name='WideTemperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('temp_inst_celsius', models.FloatField(blank=True, null=True)),
                ('temp_inst_fahrenheit', models.FloatField(blank=True, null=True)),
                ('temp_inst_kelvin', models.FloatField(blank=True, null=True)),
                ('temp_max24_celsius', models.FloatField(blank=True, null=True)),
                ('temp_max24_fahrenheit', models.FloatField(blank=True, null=True)),
                ('temp_max24_kelvin', models.FloatField(blank=True, null=True)),
                ('temp_min24_celsius', models.FloatField(blank=True, null=True)),
                ('temp_min24_fahrenheit', models.FloatField(blank=True, null=True)),
                ('temp_min24_kelvin', models.FloatField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_data.location')),
            ],
        ),
        migrations.CreateModel(
            name='WideOther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('msl_pressure_hPa', models.FloatField(blank=True, null=True)),
                ('precip_1h_mm', models.FloatField(blank=True, null=True)),
                ('precip_24h_mm', models.FloatField(blank=True, null=True)),
                ('weather_symbol_1h_idx', models.IntegerField(blank=True, null=True)),
                ('weather_symbol_24h_idx', models.IntegerField(blank=True, null=True)),
                ('uv_idx', models.FloatField(blank=True, null=True)),
                ('sunrise', models.DateTimeField(blank=True, null=True)),
                ('sunset', models.DateTimeField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_data.location')),
            ],
        ),
        migrations.CreateModel(
            name='LongWind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('wind_unit', models.CharField(choices=[('BFT', 'Beaufort'), ('KMH', 'Kilometers/hour'), ('KN', 'Knots'), ('MS', 'Meters/second'), ('DEG', 'Degrees')], max_length=3)),
                ('wind_type', models.CharField(choices=[('SPEED', 'Instantaneous wind Speed at 10m above ground'), ('DIR', 'Instantaneous wind direction at 10m above ground in degrees'), ('GUST1', 'Wind gusts in 10 m in the previous 1h'), ('GUST24', 'Wind gusts in 10 m in the previous 24h')], max_length=6)),
                ('wind_speed_10m_ms', models.FloatField(blank=True, null=True)),
                ('wind_dir_10_d', models.FloatField(blank=True, null=True)),
                ('wind_gusts_10m_1h_ms', models.FloatField(blank=True, null=True)),
                ('wind_gusts_10m_24h_ms', models.FloatField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_data.location')),
            ],
        ),
        migrations.CreateModel(
            name='LongTemperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('temperature', models.FloatField()),
                ('temp_unit', models.CharField(choices=[('C', 'Celsius'), ('F', 'Fahrenheit'), ('K', 'Kelvin')], max_length=2)),
                ('temp_type', models.CharField(choices=[('INST', 'Instantaneous'), ('MAX24', 'Previous 24-hour Max'), ('MIN24', 'Previous 24-hour Min')], max_length=5)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_data.location')),
            ],
        ),
        migrations.CreateModel(
            name='Landing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('wind_speed_10m_ms', models.FloatField(blank=True, null=True)),
                ('wind_dir_10_d', models.FloatField(blank=True, null=True)),
                ('wind_gusts_10m_1h_ms', models.FloatField(blank=True, null=True)),
                ('wind_gusts_10m_24h_ms', models.FloatField(blank=True, null=True)),
                ('t_2m_C', models.FloatField(blank=True, null=True)),
                ('t_max_2m_24h_C', models.FloatField(blank=True, null=True)),
                ('t_min_2m_24h_C', models.FloatField(blank=True, null=True)),
                ('msl_pressure_hPa', models.FloatField(blank=True, null=True)),
                ('precip_1h_mm', models.FloatField(blank=True, null=True)),
                ('precip_24h_mm', models.FloatField(blank=True, null=True)),
                ('weather_symbol_1h_idx', models.IntegerField(blank=True, null=True)),
                ('weather_symbol_24h_idx', models.IntegerField(blank=True, null=True)),
                ('uv_idx', models.FloatField(blank=True, null=True)),
                ('sunrise', models.DateTimeField(blank=True, null=True)),
                ('sunset', models.DateTimeField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_data.location')),
            ],
        ),
    ]