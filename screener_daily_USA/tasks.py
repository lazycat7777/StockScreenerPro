from screener_website.celery_app import app
from .screener_daily_USA_main import calculate_and_aggregate_results


@app.task
def calculate_and_aggregate_results_USA():
    calculate_and_aggregate_results()
    print('Данные успешно обновлены')  