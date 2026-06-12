# E-Commerce Data Cleaning

This repository contains my solution for the Week 5 assignment of the SWID Data Analytics Programme. The project focuses on data cleaning, specifically identifying and handling missing data in a mock e-commerce dataset using Python and Pandas.

##  Project Overview

Real-world data is rarely perfectly clean. In this project, I stepped into the role of a data analyst to clean an e-commerce order dataset before it could be used for downstream analysis or pipeline integration. 

The raw dataset contained missing values across multiple data types (strings, categories, and numerical values), requiring different imputation strategies for each.

##  Tools & Technologies

* **Language:** Python
* **Libraries:** Pandas, NumPy
* **Environment:** Jupyter Notebook / Local Python Environment

##  Key Tasks Completed

1. **Data Exploration:** Used `info()`, `describe()`, and `isnull().sum()` to profile the dataset and identify the scope of missing data.
2. **Handling Missing Names:** Imputed missing customer names with the constant string `"Unknown"` to retain the financial value of the order without fabricating identities.
3. **Handling Missing Prices & Quantities:** Applied median imputation to numerical columns (`Price` and `Quantity`) to ensure robustness against potential future outliers.
4. **Handling Missing Delivery Days:** Checked for outliers and filled gaps with the median, as delivery days represent discrete, whole numbers where fractional means would not make sense.
5. **Handling Missing Categories:** Used mode (most frequent value) imputation for the `Country` and `Product` categorical columns to preserve the overall distribution of the dataset without dropping valuable rows.

## How to Run

1. Clone this repository to your local machine.
2. Ensure you have Python installed along with the required libraries (`pandas`, `numpy`).
3. Open the Jupyter Notebook or Python script.
4. Run the code sequentially to see the dataset transformation from raw to fully cleaned (zero missing values).

---
*Built by Bethel (@bethel.builds) as part of the Solavise Tech Women in Data cohort.*