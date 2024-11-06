# Generated by Django 5.0.6 on 2024-11-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screener_daily_USA', '0005_stock_data_performance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_Data_Profitability',
            fields=[
                ('symbol', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('exchange', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True)),
                ('logoid', models.CharField(max_length=255, null=True)),
                ('update_mode', models.CharField(max_length=255, null=True)),
                ('type', models.CharField(max_length=255, null=True)),
                ('typespecs', models.CharField(max_length=255, null=True)),
                ('gross_margin_ttm', models.FloatField(null=True)),
                ('operating_margin_ttm', models.FloatField(null=True)),
                ('pre_tax_margin_ttm', models.FloatField(null=True)),
                ('net_margin_ttm', models.FloatField(null=True)),
                ('free_cash_flow_margin_ttm', models.FloatField(null=True)),
                ('return_on_assets_fq', models.FloatField(null=True)),
                ('return_on_equity_fq', models.FloatField(null=True)),
                ('return_on_invested_capital_fq', models.FloatField(null=True)),
                ('research_and_dev_ratio_ttm', models.FloatField(null=True)),
                ('sell_gen_admin_exp_other_ratio_ttm', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'stock_data_profitability_USA',
            },
        ),
    ]
