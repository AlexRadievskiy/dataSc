import pandas as pd
import plotly.express as px

# Загрузка данных
df = pd.read_csv('result_15.csv')

# Преобразование столбцов с датами
df['player_registration'] = pd.to_datetime(df['player_registration'])
df['date_start'] = pd.to_datetime(df['date_start'])

# Многомерный анализ (OLAP-подход)

# 1. Анализ продаж по регионам и времени
sales_by_region_time = df.groupby([pd.Grouper(key='date_start', freq='M'), 'region'])['money'].sum().reset_index()

# 2. Анализ среднего чека по категориям товаров
average_receipt_by_category = df.groupby('description')['money'].mean().reset_index()

# 3. Анализ количества успешных транзакций по платежным шлюзам
successful_transactions_by_gw = df[df['is_successful'] == 1].groupby('payment_gw').size().reset_index(name='transactions')

# Визуализация результатов с Plotly

# Географическое распределение продаж
fig = px.bar(sales_by_region_time, x='date_start', y='money', color='region', title='Продажи по регионам и времени')
fig.show()

# Средний чек по категориям товаров
fig = px.bar(average_receipt_by_category, x='description', y='money', title='Средний чек по категориям товаров')
fig.show()

# Успешные транзакции по платежным шлюзам
fig = px.bar(successful_transactions_by_gw, x='payment_gw', y='transactions', title='Успешные транзакции по платежным шлюзам')
fig.show()

# Дополнительный анализ и визуализации могут быть добавлены по аналогии