from django.db import migrations, models


def copiar_categoria(apps, schema_editor):
    Producto = apps.get_model('deportesApp', 'Producto')
    for producto in Producto.objects.select_related('categoria'):
        producto.categoria_nueva = producto.categoria.nombre.capitalize()
        producto.save(update_fields=['categoria_nueva'])


class Migration(migrations.Migration):

    dependencies = [
        ('deportesApp', '0005_alter_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria_nueva',
            field=models.CharField(
                max_length=50,
                default='',
                choices=[
                    ('Fútbol', 'Fútbol'),
                    ('Running', 'Running'),
                    ('Tenis', 'Tenis'),
                    ('Básquetbol', 'Básquetbol'),
                    ('Natación', 'Natación'),
                ],
            ),
            preserve_default=False,
        ),
        migrations.RunPython(copiar_categoria, migrations.RunPython.noop),
        migrations.RemoveField(model_name='producto', name='categoria'),
        migrations.RenameField(
            model_name='producto',
            old_name='categoria_nueva',
            new_name='categoria',
        ),
        migrations.DeleteModel(name='Categoria'),
    ]