# Generated by Django 3.1.2 on 2021-01-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=30)),
                ('cust_id', models.CharField(max_length=30)),
                ('prod_id', models.CharField(max_length=30)),
                ('prod_name', models.CharField(max_length=30)),
                ('order_qty', models.FloatField()),
                ('prod_price', models.FloatField()),
            ],
            options={
                'db_table': 'tbl_cart',
            },
        ),
        migrations.CreateModel(
            name='tbl_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_id', models.CharField(max_length=30)),
                ('cat_name', models.CharField(max_length=30)),
                ('cat_desc', models.CharField(max_length=100)),
                ('cat_img', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'tbl_category',
            },
        ),
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_id', models.CharField(max_length=30)),
                ('cust_id', models.CharField(max_length=30)),
                ('prod_id', models.CharField(max_length=30)),
                ('complaint', models.CharField(max_length=500)),
                ('comp_date', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_compalint',
            },
        ),
        migrations.CreateModel(
            name='tbl_customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.CharField(max_length=30)),
                ('cust_name', models.CharField(max_length=30)),
                ('cust_address', models.CharField(max_length=100)),
                ('cust_phno', models.BigIntegerField()),
                ('cust_email', models.CharField(max_length=50)),
                ('cust_status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_customer',
            },
        ),
        migrations.CreateModel(
            name='tbl_delvrydtls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delvry_id', models.CharField(max_length=30)),
                ('order_id', models.CharField(max_length=30)),
                ('delvry_dt', models.CharField(max_length=30)),
                ('courier_name', models.CharField(max_length=30)),
                ('delvry_remark', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_delvrydtls',
            },
        ),
        migrations.CreateModel(
            name='tbl_idgen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stfid', models.IntegerField()),
                ('ctyid', models.IntegerField()),
                ('pdtid', models.IntegerField()),
                ('ctrid', models.IntegerField()),
                ('ctid', models.IntegerField()),
                ('odrid', models.IntegerField()),
                ('odtlsid', models.IntegerField()),
                ('dvryid', models.IntegerField()),
                ('revwid', models.IntegerField()),
                ('comid', models.IntegerField()),
                ('podrid', models.IntegerField()),
                ('pmntid', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_idgen',
            },
        ),
        migrations.CreateModel(
            name='tbl_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_login',
            },
        ),
        migrations.CreateModel(
            name='tbl_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=30)),
                ('order_dt', models.DateField()),
                ('order_amt', models.FloatField()),
                ('cust_id', models.CharField(max_length=30)),
                ('order_status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_order',
            },
        ),
        migrations.CreateModel(
            name='tbl_orderdtls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderdtls_id', models.CharField(max_length=30)),
                ('order_id', models.CharField(max_length=30)),
                ('prod_id', models.CharField(max_length=30)),
                ('prod_name', models.CharField(max_length=30)),
                ('order_qty', models.FloatField()),
                ('prod_amt', models.FloatField()),
                ('order_status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_orderdtls',
            },
        ),
        migrations.CreateModel(
            name='tbl_payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=30)),
                ('order_id', models.CharField(max_length=30)),
                ('cust_id', models.CharField(max_length=30)),
                ('payment_amt', models.FloatField()),
                ('bank_name', models.CharField(max_length=30)),
                ('ifsc_code', models.CharField(max_length=50)),
                ('acc_no', models.CharField(max_length=30)),
                ('payment_dt', models.DateTimeField()),
                ('payment_status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_payment',
            },
        ),
        migrations.CreateModel(
            name='tbl_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_id', models.CharField(max_length=30)),
                ('cat_id', models.CharField(max_length=30)),
                ('prod_name', models.CharField(max_length=30)),
                ('prod_desc', models.CharField(max_length=100)),
                ('prod_unit', models.CharField(max_length=30)),
                ('prod_price', models.FloatField()),
                ('prod_img', models.CharField(max_length=300)),
                ('prod_stkqty', models.FloatField()),
                ('prod_rol', models.IntegerField()),
                ('prod_status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_product',
            },
        ),
        migrations.CreateModel(
            name='tbl_purchaseorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porder_id', models.CharField(max_length=30)),
                ('prod_id', models.CharField(max_length=30)),
                ('prod_name', models.CharField(max_length=30)),
                ('req_qty', models.FloatField()),
                ('porder_dt', models.DateField()),
            ],
            options={
                'db_table': 'tbl_purchaseorder',
            },
        ),
        migrations.CreateModel(
            name='tbl_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev_id', models.CharField(max_length=30)),
                ('prod_id', models.CharField(max_length=30)),
                ('cust_id', models.CharField(max_length=30)),
                ('review', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'tbl_review',
            },
        ),
        migrations.CreateModel(
            name='tbl_staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=30)),
                ('staff_name', models.CharField(max_length=30)),
                ('staff_address', models.CharField(max_length=100)),
                ('join_date', models.CharField(max_length=30)),
                ('staff_phno', models.BigIntegerField()),
                ('staff_email', models.CharField(max_length=50)),
                ('staff_status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_staff',
            },
        ),
    ]
