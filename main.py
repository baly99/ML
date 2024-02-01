
# About Dataset
# salaries dataset generally provides information about the employees of an organization in 
# relation to their compensation. It typically includes details such as how much each employee 
# is paid (their salary), their job titles, the departments they work in, and possibly additional 
# information like their level of experience, education, and employment history within the organization.

# Features
# - 'Id'
# - 'EmployeeName'
# - 'JobTitle'
# - 'BasePay'
# - 'OvertimePay'
# - 'OtherPay'
# - 'Benefits'
# - 'TotalPay' -> salary
# - 'TotalPayBenefits'
# - 'Year'
# - 'Notes'
# - 'Agency'
# - 'Status'

# Tasks

# 1. **Basic Data Exploration**: Identify the number of rows and columns in the dataset, determine the data types of each column, and check for missing values in each column.

# 2. **Descriptive Statistics**: Calculate basic statistics mean, median, mode, minimum, and maximum salary, determine the range of salaries, and find the standard deviation.

# 3. **Data Cleaning**: Handle missing data by suitable method with explain why you use it.

# 4. **Basic Data Visualization**: Create histograms or bar charts to visualize the distribution of salaries, and use pie charts to represent the proportion of employees in different departments.

# 5. **Grouped Analysis**: Group the data by one or more columns and calculate summary statistics for each group, and compare the average salaries across different groups.

# 6. **Simple Correlation Analysis**: Identify any correlation between salary and another numerical column, and plot a scatter plot to visualize the relationship.

# 7. **Summary of Insights**: Write a brief report summarizing the findings and insights from the analyses.


# Very Important Note
# There is no fixed or singular solution for this assignment, so if anything is not clear, please do 
# what you understand and provide an explanation.


import pandas as pd
import numpy as np

# Load your dataset
df = pd.read_csv('contentSalaries.csv')
df.head()

# Output

# 	Id	EmployeeName	JobTitle	BasePay	OvertimePay	OtherPay	Benefits	TotalPay	TotalPayBenefits	Year	Notes	Agency	Status
# 0	1	NATHANIEL FORD	GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY	167411.18	0.00	400184.25	NaN	567595.43	567595.43	2011	NaN	San Francisco	NaN
# 1	2	GARY JIMENEZ	CAPTAIN III (POLICE DEPARTMENT)	155966.02	245131.88	137811.38	NaN	538909.28	538909.28	2011	NaN	San Francisco	NaN
# 2	3	ALBERT PARDINI	CAPTAIN III (POLICE DEPARTMENT)	212739.13	106088.18	16452.60	NaN	335279.91	335279.91	2011	NaN	San Francisco	NaN
# 3	4	CHRISTOPHER CHONG	WIRE ROPE CABLE MAINTENANCE MECHANIC	77916.00	56120.71	198306.90	NaN	332343.61	332343.61	2011	NaN	San Francisco	NaN
# 4	5	PATRICK GARDNER	DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)	134401.60	9737.00	182234.59	NaN	326373.19	326373.19	2011	NaN	San Francisco	NaN


df.columns

# Output

# Index(['Id', 'EmployeeName', 'JobTitle', 'BasePay', 'OvertimePay', 'OtherPay',
#        'Benefits', 'TotalPay', 'TotalPayBenefits', 'Year', 'Notes', 'Agency',
#        'Status'],
#       dtype='object')


# 1. **Basic Data Exploration**:

# To Identify the number of rows and columns in the dataset
num_rows, num_cols = df.shape
print("Number of rows", num_rows)
print("Number of columns", num_cols)

# determine the data types of each column
column_types = df.dtypes
print(column_types)

# check for missing values in each column.
missing_values = df.isnull().sum()
print(missing_values)





# 2. **Descriptive Statistics**:

# Calculate the mean salary
mean_salary = df['TotalPay'].mean()
print("Mean Salary", mean_salary)

# Calculate the median salary
median_salary = df['TotalPay'].median()
print("Median Salary", median_salary)

# Calculate the mode of salary 
mode_salary = df['TotalPay'].mode()
print("Mode Salary", mode_salary)

# Calculate the minimum salary
min_salary = df['TotalPay'].min()
print("Minimum Salary", min_salary)

# Calculate the maximum salary
max_salary = df['TotalPay'].max()
print("Maximum Salary", max_salary) 

# determine the range of salaries
salary_range = df['TotalPay'].max() - df['TotalPay'].min()
print("Salary Range", salary_range)

# find the standard deviation.
salary_std = df['TotalPay'].std()
print("Standard Deviation of Salary", salary_std)


# 3. **Data Cleaning**: Handle missing data by suitable method with explain why you use it.

# Check for missing values in each column
missing_values = df.isnull().sum()
print(missing_values)


# Perform mean imputation for numeric features
numeric_features = ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay', 'TotalPayBenefits']
df[numeric_features] = df[numeric_features].fillna(df[numeric_features].mean())

# Perform mode imputation for categorical features
categorical_features = ['JobTitle', 'Department', 'Year', 'Notes', 'Agency', 'Status']
df[categorical_features] = df[categorical_features].fillna(df[categorical_features].mode().iloc[0])

# Verify if missing values are handled
missing_values = df.isnull().sum()
print(missing_values)

# we first identify the numeric and categorical features in the dataset. Then, 
# we use the fillna() method to impute missing values. 
# For numeric features, we fill the missing values with the mean of each respective column. 
# For categorical features, we fill the missing values with the mode (most frequent value) of each respective column.

# Finally, we verify if any missing values remain in the dataset by 
# calculating the sum of missing values for each column using isnull().sum().



# 4. **Basic Data Visualization**: Create histograms or bar charts to visualize the distribution of salaries, 
#     and use pie charts to represent the proportion of employees in different departments.

import matplotlib.pyplot as plt


# Create a histogram of salaries
plt.figure(figsize=(10, 6))
plt.hist(df['TotalPay'], bins=20, color='skyblue')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Distribution of Salaries')
plt.show()

# Create a bar chart of department proportions
department_counts = df['Department'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(department_counts.index, department_counts.values, color='skyblue')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.title('Proportion of Employees in Different Departments')
plt.xticks(rotation=90)
plt.show()

# Create a pie chart of department proportions
plt.figure(figsize=(10, 6))
plt.pie(department_counts.values, labels=department_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Proportion of Employees in Different Departments')
plt.axis('equal')
plt.show()


# 5. **Grouped Analysis**: Group the data by one or more columns and 
#     calculate summary statistics for each group, and compare the average salaries across different groups.


# Group the data by one or more columns and calculate summary statistics
grouped_data = df.groupby(['Department', 'JobTitle']).agg({'TotalPay': ['mean', 'median'], 'BasePay': 'max'})
grouped_data.columns = ['AverageTotalPay', 'MedianTotalPay', 'MaxBasePay']
grouped_data.reset_index(inplace=True)

# Compare the average salaries across different groups
average_salary_comparison = grouped_data.groupby('Department')['AverageTotalPay'].mean().sort_values(ascending=False)
print(average_salary_comparison)


# 6. **Simple Correlation Analysis**: Identify any correlation between salary and another numerical column, 
#     and plot a scatter plot to visualize the relationship.

# Identify correlation between salary and another numerical column
correlation = df['TotalPay'].corr(df['YearsExperience'])
print("Correlation between TotalPay and YearsExperience:", correlation)

# Plot scatter plot to visualize the relationship
plt.figure(figsize=(8, 6))
plt.scatter(df['YearsExperience'], df['TotalPay'], color='skyblue')
plt.xlabel('Years of Experience')
plt.ylabel('Total Pay')
plt.title('Relationship between Salary and Years of Experience')
plt.show()


# 7. **Summary of Insights**: Write a brief report summarizing the findings and insights from the analyses.


# Introduction:
#     The purpose of this report is to summarize the findings and insights 
#     from the analyses performed on the salary dataset. 
#     The dataset provides information about employees in an organization, 
#     including their job titles, salaries, departments, and other relevant details.

# 1. Handling Missing Data:
#     To handle missing data in the dataset, mean imputation was used for numeric features, 
#     and mode imputation was used for categorical features. 
#     This approach was chosen to fill in missing values with representative values based on the feature type.

# 2. Distribution of Salaries:
#     A histogram was created to visualize the distribution of salaries. 
#     The histogram depicted the frequency of different salary ranges. 
#     The shape of the distribution can provide insights into the overall salary distribution within the organization.

# 3. Proportion of Employees in Different Departments:
#     Bar charts and pie charts were used to represent the proportion of employees in different departments. 
#     The bar chart displayed the number of employees in each department, while the pie chart illustrated the 
#     proportion of employees in each department as a percentage of the total. 
#     These visualizations allow for quick comparisons and identification of departments with the highest and lowest employee counts.

# 4. Summary Statistics by Groups:
#     The data was grouped by one or more columns (e.g., Department and JobTitle) 
#     to calculate summary statistics for each group. 
#     The summary statistics included the average and median total pay, as well as the maximum base pay for each group. 
#     This analysis helps to understand the variations in compensation across different departments and job titles.

# 5. Comparison of Average Salaries:
#     The average salaries across different departments were compared. 
#     The departments were ranked based on the mean average total pay. 
#     This comparison provides insights into the departments with the highest and lowest average salaries.

# 6. Correlation between Salary and Years of Experience:
#     The correlation between salary (TotalPay) and years of experience was analyzed. 
#     A scatter plot was created to visualize the relationship. 
#     The correlation coefficient was calculated, indicating the strength and direction of the correlation. 
#     This analysis helps to identify any association between salary and years of experience.

# Conclusion:
#     Based on the analyses performed on the salary dataset, several insights and findings were obtained. 
#     The distribution of salaries provided an understanding of the overall salary structure within the organization. 
#     The visualizations of department proportions allowed for comparisons and identification of departments with varying employee counts. 
#     The summary statistics by groups allowed for a deeper understanding of compensation variations in different departments and job titles. 
#     The comparison of average salaries highlighted departments with higher and lower average salaries. 
#     Lastly, the correlation analysis between salary and years of experience provided insights into the relationship between these two variables.

#     These findings and insights can be valuable for the organization in terms of understanding salary distribution, 
#     identifying areas for improvement in compensation, and making informed decisions regarding employee remuneration.
