from .update_stock_data_USA.calculate_results_main import calculate_and_aggregate_results
from screener_website.celery_app import app


@app.task
def calculate_results_USA():
    calculate_and_aggregate_results()
    print('Данные успешно обновлены')  