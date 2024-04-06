import pandas as pd
import matplotlib.pyplot as plt

dataCustomer = pd.read_csv("D:\\Python\\Sourse\\Customer.csv")
dataProduct = pd.read_csv("D:\\Python\\Sourse\\Product.csv")
dataSaleHistory = pd.read_csv("D:\\Python\\Sourse\\SaleHistory.csv")
dataWebAccessHistory = pd.read_csv("D:\\Python\\Sourse\\WebAccessHistory.csv")

# Print out all tables
print("=== Customer Table ===")
print(dataCustomer.head())

print("\n=== Product Table ===")
print(dataProduct.head())

print("\n=== Sale History Table ===")
print(dataSaleHistory.head())

print("\n=== Web Access History Table ===")
print(dataWebAccessHistory.head())

# Delete empty data from each table
dataCustomer.dropna(inplace=True)
dataProduct.dropna(inplace=True)
dataSaleHistory.dropna(inplace=True)
dataWebAccessHistory.dropna(inplace=True)

# Reprint tables after removing empty data
print("\n=== Customer Table after removing empty rows ===")
print(dataCustomer.head())

print("\n=== Product Table after removing empty rows ===")
print(dataProduct.head())

print("\n=== Sale History Table after removing empty rows ===")
print(dataSaleHistory.head())

print("\n=== Web Access History Table after removing empty rows ===")
print(dataWebAccessHistory.head())

# Customer

# Count the number of male and female customers
gender_counts = dataCustomer['Gender'].value_counts()
# Plot a pie chart
plt.pie(gender_counts.values, labels = gender_counts.index, autopct='%1.1f%%')
# Set the title
plt.title('Customer gender ratio')
# Display the plot
plt.show()

# Product
# Count the number of products by category
category_counts = dataProduct['Category'].value_counts()

# Draw a bar chart
plt.figure(figsize=(10, 6))  # Increase the size of the chart
bars = plt.bar(category_counts.index, category_counts.values)

# Set the title and axis labels
plt.title('Number of Products by Category')
plt.xlabel('Category')
plt.ylabel('Quantity')

# Rotate x-axis labels and adjust spacing
plt.xticks(rotation=45, ha='right')

# Check and adjust the font if needed
for bar in bars:
    height = bar.get_height()
    if height < 10:
        plt.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom', fontsize=8)
    else:
        plt.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom')

# Display the chart
plt.tight_layout()  # Ensure the content is not cut off
plt.show()

# Count the number of visits to each webpage
page_visits = dataWebAccessHistory['PageVisited'].value_counts()

# Get the top 10 visited pages
top_10_pages = page_visits.head(10)

# Create a bar chart to show the number of visits to each webpage
plt.bar(top_10_pages.index, top_10_pages.values)

# Set the title and axis labels
plt.title('Top 10 Visited Pages')
plt.xlabel('Page')
plt.ylabel('Number of Visits')

# Rotate the x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Display the chart
plt.show()