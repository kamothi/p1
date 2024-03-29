# Generated by Django 4.2.1 on 2023-05-14 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataTest', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='board',
            fields=[
                ('board_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, null=True)),
                ('content', models.TextField(null=True)),
                ('update_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('views', models.PositiveIntegerField()),
                ('comment', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataTest.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataTest.customer')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_posts', through='dataTest.Like', to='dataTest.customer'),
        ),
    ]
