Data Cleaning & Preprocessing – Netflix Dataset

Objective:
The goal of this project is to clean and preprocess a raw Netflix dataset by handling missing values, removing duplicates, and standardizing data formats.

Tools Used
* Python
* Pandas

Steps Performed
* Loaded dataset using Pandas
* Identified missing values using `.isnull()`
* Filled missing values in columns like director, cast, and country
* Removed rows with critical missing data (date_added, rating)
* Removed duplicate records
* Standardized column names (lowercase, no spaces)
* Converted date format to datetime

Key Insights
* Majority of the content on Netflix is Movies
* Content addition increased significantly after 2015

Files Included
* netflix_titles.csv (raw dataset)
* cleaned_netflix.csv (cleaned dataset)
* netflix_data_cleaning.py (code)

Outcome:
A clean and structured dataset ready for further data analysis and visualization.

