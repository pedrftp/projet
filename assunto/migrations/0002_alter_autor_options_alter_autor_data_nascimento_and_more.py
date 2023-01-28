from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterField(
            model_name='autor',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='endereco',
            field=models.CharField(max_length=200, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('conteudo', models.TextField(verbose_name='Conteudo')),
                ('data_pub', models.DateField(verbose_name='Data de publicação')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticia.autor')),
            ],
        ),
    ]