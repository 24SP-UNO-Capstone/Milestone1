import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('..\\data\\2023-Survey.csv')
# Since we're interested in orgSize and intSecStaff, we'll focus on these columns
# It's important to handle missing values. We'll drop rows where either of these columns is missing.
data_filtered = data[['orgSize', 'intSecStaff']].dropna()

org_size_order_desc = [
    'Fewer than 100',
    '101 to 500', 
    '501 to 1,000', 
    '1,001 to 2,000',
    '2,001 to 5,000',
    '5,001 to 10,000', 
    '10,001 to 15,000', 
    '15,001 to 50,000',
    '50,001 to 100,000',
    'More than 100,000'
]

int_sec_staff_order = [
    'Less than 1 (part-time)', '1', '2 to 10', '11 to 25', '26 to 100', '101 to 1,000', 'Greater than 1000' # Assuming a logical progression; adjust as needed
]

# Ensure 'intSecStaff' in the original DataFrame is treated as a categorical variable with the defined order
data_filtered['intSecStaff'] = pd.Categorical(data_filtered['intSecStaff'], categories=int_sec_staff_order, ordered=True)

# Now, let's create the plot again with the y-axis values ordered as per the manually defined list
plt.figure(figsize=(12, 8))
sns.countplot(data=data_filtered, y='orgSize', hue='intSecStaff', palette='magma', order=org_size_order_desc)
plt.title('Organization Size by Internal Security Staff (Descending Order)')
plt.xlabel('Count')
plt.ylabel('Organization Size')
plt.legend(title='Internal Security Staff', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()