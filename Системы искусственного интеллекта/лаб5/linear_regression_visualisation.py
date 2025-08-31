import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('california_housing_train.csv')

stats = df.describe(include='all').T

with pd.option_context('display.max_columns', 8):
    print(stats)

sns.set_theme(style="whitegrid")

df.hist(bins=30, figsize=(15, 10), layout=(3, 3), color='skyblue', edgecolor='black')
plt.suptitle('Гистограммы признаков', fontsize=16)
plt.tight_layout(rect=(0, 0.03, 1, 0.95))
plt.show()

plt.figure(figsize=(15, 10))
for i, column in enumerate(df.columns, 1):
    plt.subplot(3, 3, i)
    sns.boxplot(y=df[column], color='lightgreen')
    plt.title(f'Boxplot {column}')
plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 10))
for i, column in enumerate(df.columns, 1):
    plt.subplot(3, 3, i)
    sns.violinplot(y=df[column], color='lightcoral')
    plt.title(f'Вайдиновая диаграмма {column}')
plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 10))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.xticks(rotation=45)
plt.title('Матрица корреляций')
plt.show()

mean_std = stats[['mean', 'std']].reset_index()
mean_std_melted = pd.melt(mean_std, id_vars='index', value_vars=['mean', 'std'], var_name='Статистика',
                          value_name='Значение')

plt.figure(figsize=(15, 10))
sns.barplot(x='index', y='Значение', hue='Статистика', data=mean_std_melted, palette='Set2')
plt.xticks(rotation=45)
plt.title('Среднее и стандартное отклонение признаков')
plt.xlabel('Признак')
plt.ylabel('Значение')
plt.legend()
plt.tight_layout()
plt.show()

quantiles = df.quantile([0.25, 0.5, 0.75]).T
quantiles['min'] = stats['min']
quantiles['max'] = stats['max']
quantiles = quantiles.reset_index().rename(columns={'index': 'Признак'})
quantiles_melted = pd.melt(quantiles, id_vars='Признак', var_name='Статистика', value_name='Значение')

plt.figure(figsize=(15, 10))
ax = sns.barplot(x='Признак', y='Значение', hue='Статистика', data=quantiles_melted, palette='Set3')
plt.xticks(rotation=45)
plt.title('Квантили, минимум и максимум признаков')
plt.xlabel('Признак')
plt.ylabel('Значение')
plt.legend()

for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height:.2f}', (p.get_x() + p.get_width() / 2., height), ha='center', va='bottom', fontsize=8,
                rotation=90)

plt.tight_layout()
plt.show()
