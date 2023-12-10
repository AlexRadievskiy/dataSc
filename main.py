import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
df = pd.read_csv('result_15.csv')

# Перевірка наявності даних
if df.isnull().values.any():
    print("Виявлено відсутні значення")
    # Обробка відсутніх значень (наприклад, видалення або заповнення)
    df = df.dropna()  # або df.fillna(0) або інша логіка обробки

# Перетворення стовпців з датами
df['player_registration'] = pd.to_datetime(df['player_registration'])
df['date_start'] = pd.to_datetime(df['date_start'])

# 1. Об'єм продажів
sales_volume = df['is_package'].sum()

# 2. Середній чек
average_receipt = df['money'].mean()

# 3. Географічне розподілення продажів
sales_distribution = df.groupby('region')['money'].sum().sort_values(ascending=False)

# 4. Частота повторних покупок
repeat_purchases = df.groupby('player_id').size().value_counts().sort_index()

# 5. Середній час від реєстрації до покупки
time_to_purchase = (df['date_start'] - df['player_registration']).dt.days.mean()

# 6. Процент успішних транзакцій
successful_transactions_percentage = (df['is_successful'].mean()) * 100

# 7. Процент повернень
refund_percentage = (df['is_refunded'].mean()) * 100

# 8. Середній час онлайн до покупки
average_online_time_before_purchase = df['player_seconds_online'].mean()

# 9. Ефективність маркетингових каналів
marketing_efficiency = df.groupby('payment_gw')['money'].sum().sort_values(ascending=False)

# 10. Рівень лояльності клієнтів
loyalty_level = df.groupby('player_id')['money'].sum().sort_values(ascending=False)

# Перевірка на викиди (приклад для 'money')
Q1 = df['money'].quantile(0.25)
Q3 = df['money'].quantile(0.75)
IQR = Q3 - Q1
filter = (df['money'] >= Q1 - 1.5 * IQR) & (df['money'] <= Q3 + 1.5 * IQR)
df_filtered = df.loc[filter]

# Візуалізація результатів
plt.figure(figsize=(10, 6))
sales_distribution.plot(kind='bar')
plt.title('Географічне розподілення продажів')
plt.xlabel('Регіон')
plt.ylabel('Сума продажів')
plt.show()

plt.figure(figsize=(10, 6))
repeat_purchases.plot(kind='bar')
plt.title('Частота ')
plt.xlabel('Кількість покупок')
plt.ylabel('Кількість клієнтів')
plt.show()

# Продовження аналізу

# 6. Процент успішних транзакцій
plt.figure(figsize=(6, 4))
plt.bar(['Успішні', 'Неуспішні'], [successful_transactions_percentage, 100 - successful_transactions_percentage])
plt.title('Відсоток успішних транзакцій')
plt.ylabel('Відсоток')
plt.show()

# 7. Процент повернень
plt.figure(figsize=(6, 4))
plt.bar(['Повернення', 'Без повернення'], [refund_percentage, 100 - refund_percentage])
plt.title('Відсоток повернень')
plt.ylabel('Відсоток')
plt.show()

# 8. Середній час онлайн до покупки
plt.figure(figsize=(6, 4))
plt.hist(df['player_seconds_online'], bins=20, color='blue')
plt.title('Середній час онлайн до покупки')
plt.xlabel('Час онлайн (секунди)')
plt.ylabel('Кількість користувачів')
plt.show()

# 9. Ефективність маркетингових каналів
plt.figure(figsize=(10, 6))
marketing_efficiency.plot(kind='bar')
plt.title('Ефективність маркетингових каналів')
plt.xlabel('Платіжний шлюз')
plt.ylabel('Сума продажів')
plt.show()

# 10. Рівень лояльності клієнтів
top_loyal_customers = loyalty_level.head(10)
plt.figure(figsize=(10, 6))
top_loyal_customers.plot(kind='bar')
plt.title('Топ-10 лояльних клієнтів')
plt.xlabel('ID клієнта')
plt.ylabel('Сума покупок')
plt.show()

# Додатково: Середній час від реєстрації до покупки
plt.figure(figsize=(6, 4))
plt.hist((df['date_start'] - df['player_registration']).dt.days, bins=20, color='green')
plt.title('Середній час від реєстрації до покупки')
plt.xlabel('Дні')
plt.ylabel('Кількість користувачів')
plt.show()

