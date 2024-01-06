# This is used to display graphics at the same notebook (Jupiter Notebook) instead of opening them in a separate file.
%matplotlib inline 

# Import the libraries which are used in these project: Pandas, Seaborn and matplotlib.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setting font for the document.
plt.rcParams["font.family"] = "arial"

# The first step - getting the data from our file (table) which contains all the information we need.
# Reading a file with the data - this file can be found in the root directory.
data = pd.read_csv('Userbase.csv')
# Displaying the data read from a file in the form of a table with the first 10 rows visible.
data.head(10)

# Data preparation and preprocessing - the second step, where the data is tranformed in the form which is essential for the task faced.
# Let's see what type of data are we dealing with (columins, data types, number of indexes).
data.info()
# The description of the table can be achieved by this method:
data.describe()

# Data transform - rename columns by removing capital letters and inserting underscore instead of space.
data.rename(
    columns={
        'User ID': 'user_id',
        'Subscription Type': 'sub_type',
        'Monthly Revenue': 'monthly_revenue',
        'Join Date': 'first_sub_date',
        'Last Payment Date': 'last_sub_date',
        'Plan Duration': 'plan_duration',
        'Country': 'country',
        'Age': 'age',
        'Gender': 'gender',
        'Device': 'device',
    },
    inplace=True
)

# Adding a column into our table for a better understanding of one very important feature - the duration of a subscription period of any viewer (in days).
# sub_period is calculated as substraction: last_sub_date - first_sub_date.
data['first_sub_date'] = pd.to_datetime(data['first_sub_date'], format='%d-%m-%y')
data['last_sub_date'] = pd.to_datetime(data['last_sub_date'], format='%d-%m-%y')
data['sub_period'] = (data['last_sub_date'] - data['first_sub_date'])
data['sub_period'] = data['sub_period'].dt.days

# Let's view our table again (in a form suitable for analysis)
data.head(10)
