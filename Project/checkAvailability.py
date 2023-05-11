import pandas as pd
import requests
from bs4 import BeautifulSoup


"""
A simple script to check the availability for each product.
- By selecting the excel sheet name, Sheet name and the column that is having product links
"""

# Read the Excel file
df = pd.read_excel("proNew.xlsx", sheet_name="Sheet1")

# Specify the column containing the product links
column_with_links = "Product link"

# Create a new column to store availability status
df["Current Availability"] = ""

for index, row in df.iterrows():
    link = str(row[column_with_links])
    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")
        button = soup.find("li", class_="active")

        if button:
            availability = "Available"
        else:
            availability = "Not Available"

        df.at[index, "Current Availability"] = availability
    except Exception as e:
        print(f"Error processing link: {link}")
        print(e)


# Save the updated Excel file
df.to_excel("proNew.xlsx", index=False)

