# Stake Holder Analysis

**Analysis**:

In order to properly scope the challenges our CTI guide will address and the recommendations we will provide, we must first identify who our audience is and the resources available to them. To do this, we have identified a good source for a cybersecurity "census," the SANs SOC Survey. While this data does not entirely represent all businesses, it provides a good look into the size, resources, and capabilities of businesses that at least contain some security maturity level. 

We collected the data from the SANs SOC Survey from 2022 and 2023 to create our graphs for our analysis. The data points we addressed were organization size, security team size, and annual budgets. Our analysis lacks an accurate positional breakdown of the security team and a breakdown of annual budgets between software licenses, hardware, training, and people. This also does not consider the difference between new license and renewal budgets. 

Below are four graphs that break down organization size vs. annual security budgets and organization size vs. security team size—the data from 2022 and 2023. 

**SANs Data Graphs**:
<div class="align-center">
	<img src="./images/2022-OrgbyBudget.png" alt="what am I doing here?">
<div>

**Table 1**: This table shows the annual security budget by the size of organizations based on data collected in the SANs 2022 SOC Survey.

<div class="align-center">
	<img src="./images/2022-OrgbySecSize.png" alt="what am I doing here?">
<div>

**Table 2**: This table shows the security team size by the size of organizations based on data collected in the SANs 2022 SOC Survey.

<div class="align-center">
	<img src="./images/2023-OrgbyBudget.png" alt="what am I doing here?">
<div>

**Table 3**: This table shows the annual security budget by the size of organizations based on data collected in the SANs 2023 SOC Survey.

<div class="align-center">
	<img src="./images/2023-OrgbySecSize.png" alt="what am I doing here?">
<div>

**Table 4**: This table shows the security team size by the size of organizations based on data collected in the SANs 2023 SOC Survey.

Report and data available [here.](https://soc-survey.com/)

In order to correlate the vast difference in spending between the different sized organizations, we will take the available data points and identify the average spend per user. In order to do this, given the limitations of the available data, we will calculate the average number of users per company and the average security budget. We used this formula to calculate the average of each range:

```
Average = (Minimum + Maximum) * 0.5
```

Next, we took the sum of the averages for each organization size and divided them by the number of data points and the average number of users.

```
Average Spend Per User = SUM(budget) / # of data points / Acerage Users
```

**2022 - Spend Per User**
| Organization Size | Average Users | Average Spend Per User | Companies |
| ----------------- | ------------- | ---------------------- | --------- |
| Fewer than 100 | 50.5 users | $3,800.71 | 31 |
| 101 to 500 | 300.5 users | $2,293.05 | 32 |
| 501 to 1,000 | 750.5 users | $2,146.01 | 26 |
| 1,001 to 2,000 | 1,500.5 users | $1,025.58 | 9 |
| 2,001 to 5,000 | 3,500.5 users | $473.74 | 12 |

**2023 - Spend Per User**
| Organization Size | Average Users | Average Spend Per User | Companies |
| ----------------- | ------------- | ---------------------- | --------- |
| Fewer than 100 | 50.5 users | $4,702.98 | 14 |
| 101 to 500 | 300.5 users | $3,944.32 | 56 |
| 501 to 1,000 | 750.5 users | $,2063.84 | 46 |
| 1,001 to 2,000 | 1,500.5 users | $1,348.63 | 18 |
| 2,001 to 5,000 | 3,500.5 users | $857.64 | 23 |

For this chart, we removed the "$48 million +" budgets as those appear to be excessive outliers compared to the rest of the data points that could skew the results.

**Findings**: 

This report is intended for IT staff with a focus on cybersecurity obligations in addition to personnel in a security analyst, security engineer, architect, or cybersecurity manager role. It has been designed specifically for organizations with little or zero financial budget designated for Cyber Threat Intelligence goals but still wants to improve their intelligence capabilities. 

This report's suggested development and operational tasks are designed to reduce hands-on responsibilities and recommend automation wherever possible. This CTI model assumes that most organizations need full-time equivalent staff available, and this model must be able to operate with limited maintenance or dedicated resources. 

This technical guide is written to benefit readers of all cybersecurity experience levels. Organizations may implement the entire framework as written or adopt individual pieces as needed to meet their needs. 

**Citations**: 

Crowley, C., Filkins, B., & Pescatore, J. (2024, March 13). SANS 2023 SOC Survey. SANS Institute. https://www.sans.org/white-papers/2023-sans-soc-survey/ 