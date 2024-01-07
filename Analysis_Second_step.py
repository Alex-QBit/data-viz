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
