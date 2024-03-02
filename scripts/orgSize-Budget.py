import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('..\\data\\2022-Survey.csv')
# Since we're interested in orgSize and intSecStaff, we'll focus on these columns
# It's important to handle missing values. We'll drop rows where either of these columns is missing.
data_filtered = data[['orgSize', 'budget']].dropna()

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

budget_order = [
    'Less than $100,000 USD',
    '$100,001 to 250,000 USD',
    '250,001 to $500,000 USD',
    '$500,001 to $750,000 USD',
    '$750,001 to $1,000,000 USD',
    '$1 million to $2 million USD',
    '$2 million to $4 million USD',
    '$4 million to $8 million USD',
    '$8 million to $16 million USD',
    '$16 million to $48 million USD',
    'Greater than $48M USD',
]

# Ensure 'intSecStaff' in the original DataFrame is treated as a categorical variable with the defined order
data_filtered['budget'] = pd.Categorical(data_filtered['budget'], categories=budget_order, ordered=True)

# Now, let's create the plot again with the y-axis values ordered as per the manually defined list
plt.figure(figsize=(12, 8))
sns.countplot(data=data_filtered, y='orgSize', hue='budget', palette='magma', order=org_size_order_desc)
plt.title('2022 Organization Size by Security Budget (Ascending Order)')
plt.xlabel('Count')
plt.ylabel('Organization Size')
plt.legend(title='Security Budget', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()