# Generated by Django 5.0.6 on 2024-07-09 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0003_servico_identificador'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicoAdicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('preco', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='servico',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='servico',
            name='servicos_adicionais',
            field=models.ManyToManyField(to='servicos.servicoadicional'),
        ),
    ]