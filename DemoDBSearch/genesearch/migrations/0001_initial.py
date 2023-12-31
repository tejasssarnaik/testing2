# Generated by Django 4.2.5 on 2023-09-14 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yellow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chr', models.CharField(max_length=200)),
                ('Start', models.IntegerField()),
                ('End', models.IntegerField()),
                ('Ref', models.CharField(max_length=10)),
                ('Alt', models.CharField(max_length=10)),
                ('Ref_Gene', models.CharField(max_length=200)),
                ('Func_refGene', models.CharField(max_length=200)),
                ('ExonicFunc_refGene', models.CharField(max_length=200)),
                ('OMIM', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Green',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbSNP_ID', models.CharField(max_length=200)),
                ('ClinVar_Sig', models.CharField(max_length=200)),
                ('Ref_Gene', models.CharField(max_length=200)),
                ('InterVa_InterVar_and_Evidence', models.CharField(max_length=1000)),
                ('Freq_gnomAD_genome_ALL', models.CharField(max_length=200)),
                ('Freq_esp6500siv2_all', models.CharField(max_length=200)),
                ('Freq_1000g2015aug_all', models.CharField(max_length=200)),
                ('CADD_raw', models.CharField(max_length=200)),
                ('CADD_phred', models.CharField(max_length=200)),
                ('SIFT_score', models.CharField(max_length=200)),
                ('yellow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genesearch.yellow')),
            ],
        ),
    ]
