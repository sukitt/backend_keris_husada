# Generated by Django 2.2 on 2020-01-28 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('akademik', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manajemen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nilaisemester',
            name='mahasiswa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manajemen.Mahasiswa'),
        ),
        migrations.AddField(
            model_name='nilaisemester',
            name='matakuliah',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akademik.Matakuliah'),
        ),
        migrations.AddField(
            model_name='matakuliah',
            name='program_studi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akademik.ProgramStudi'),
        ),
        migrations.AddField(
            model_name='krs',
            name='jadwal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='akademik.Jadwal', verbose_name='Jadwal Matakuliah'),
        ),
        migrations.AddField(
            model_name='krs',
            name='mahasiswa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manajemen.Mahasiswa'),
        ),
        migrations.AddField(
            model_name='jadwal',
            name='dosen',
            field=models.ManyToManyField(to='manajemen.Dosen'),
        ),
        migrations.AddField(
            model_name='jadwal',
            name='matakuliah',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='akademik.Matakuliah'),
        ),
        migrations.AddField(
            model_name='jadwal',
            name='ruang_kuliah',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='akademik.RuangKuliah'),
        ),
        migrations.AddField(
            model_name='absensi',
            name='dibuat_oleh',
            field=models.OneToOneField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='absensi',
            name='diperbarui_oleh',
            field=models.OneToOneField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='absensi',
            name='jadwal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akademik.Jadwal'),
        ),
        migrations.AddField(
            model_name='absensi',
            name='mahasiswa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manajemen.Mahasiswa'),
        ),
    ]
