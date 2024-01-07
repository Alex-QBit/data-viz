# Setting (describing) a color palette which we are using in this study.
sns.palplot(['#0784BC','#6F7E88','#7DB9DB','#E0C29D','#062641'])
palette = ['#0784BC','#6F7E88','#7DB9DB','#E0C29D','#062641']

# How many new users do subscribe each month?
# A lineplot is the choice for this graph.
fig, ax = plt.subplots(figsize=(10,5))
user_counts = data['first_sub_date'].value_counts().sort_index()
user_counts = user_counts[user_counts.index > '2022-11-01']
sns.lineplot(x = user_counts.index, y = user_counts.values, ax = ax)
sns.despine()
ax.grid(axis = 'x', linestyle = '--', alpha = 0.5)
ax.grid(axis = 'y', linestyle = '--', alpha = 0.5)
ax.set_ylim(0)
ax.set_ylabel('Количество пользователей')
plt.show()

# What is the most favorite (popular) type of subscription among the viewers?
# This time countplot is a method to describe different categories and their quantitative values.
fig, ax = plt.subplots()
sns.countplot(x = 'sub_type', data = data, color = '#062641')
sns.despine()
ax.grid(axis = 'y', linestyle = '--', alpha = 0.1)
for s in ['top', 'left', 'right']:
    ax.spines[s].set_visible(False)
ax.tick_params(axis = 'both', which = 'both', length = 0)
ax.set_ylabel('Количество пользователей')
ax.set_xlabel('Тип подписки')
plt.show()

# How many viewers (users) are there in each country where our service is positioned?
fig, ax = plt.subplots()
sns.countplot(y = 'country', data = data, color = '#E0C29D', alpha = 0.95)
sns.despine()
ax.grid(axis = 'x', linestyle = '--', alpha = 0.8)
for s in ['top', 'bottom', 'right']:
    ax.spines[s].set_visible(False)
ax.tick_params(axis = 'both', which = 'both', length = 0)
ax.set_xlabel('Количество пользователей')
ax.set_ylabel('Страна')
plt.show()

# What age distribution does each country has in our service?
# The choice for this graph is histogram.
fig, ax = plt.subplots()
sns.histplot(x = 'age', data = data, color = '#0784BC', binwidth = 10)
sns.despine()
ax.grid(axis = 'y', linestyle = '--', alpha = 0.6)
for s in ['top', 'left', 'right']:
    ax.spines[s].set_visible(False)
ax.tick_params(axis = 'both', which = 'both', length = 0)
ax.set_ylabel('Количество пользователей')
ax.set_xlabel('Возраст')
plt.show()

# Where are the viewers located who have been subscribed for the service the longest?
# Barplot as a method allows us to determine both categories for each country and uncertainty around satistical estimate values.
fig, ax = plt.subplots()
sns.barplot(x = 'sub_period', y = 'country', data = data, color = '#6F7E88', width = 0.75)
ax.set_xlabel('Период подписки, дни')
ax.set_ylabel('Страна')
plt.show()

# What is the correlation between type of subscription and user's country?
# This graph counts the number of users in each country and of each type (basic, standart, premium).
fig, ax = plt.subplots(figsize=(10,6))
sns.countplot(y= 'country', hue= 'sub_type', data=data, palette=palette, width=0.8)
ax.set_xlabel('Количество пользователей')
ax.set_ylabel('Страна')
plt.show()

# What platform is the most popular among our viewers?
# By each country
fig, ax = plt.subplots(figsize=(15,12))
sns.countplot(y= 'country', hue= 'device', data=data, palette=palette, width=0.8)
ax.set_xlabel('Количество пользователей')
ax.set_ylabel('Страна')
plt.show()

# Worldwide
fig, ax = plt.subplots(figsize=(10,6))
sns.countplot(y = 'device', data = data, palette = palette, width = 0.65)
ax.set_xlabel('Количество пользователей')
ax.set_ylabel('Платформа')
plt.show()

# What is the correlation between: revenue, type of subscription, country and platform?
# This boxplot (box-and-whisker) shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution (0%, 25%, 50%, 75%, 100%).
# The following graph vizualizes revenue from each subscription.
fig, ax = plt.subplots(figsize=(12,10))
sns.boxplot(x = 'sub_type', y = 'monthly_revenue', data = data, palette = palette)
ax.set_xlabel('Тип подписки')
ax.set_ylabel('Месячная выручка')
plt.show()

# By each country
fig, ax = plt.subplots(figsize=(20,12))
sns.boxplot(x = 'country', y = 'monthly_revenue', data = data, palette = palette)
ax.set_xlabel('Страна')
ax.set_ylabel('Месячная выручка')
plt.show()

# By each platform
fig, ax = plt.subplots(figsize=(12,10))
sns.boxplot(x = 'device', y = 'monthly_revenue', data = data, palette = palette)
ax.set_xlabel('Платформа')
ax.set_ylabel('Месячная выручка')
plt.show()
