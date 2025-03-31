## **Project Overview**  
This project focuses on analyzing IMDb’s top-rated movies dataset using **Python** and **SQL**. The objective is to perform **ETL (Extract, Transform, Load) operations**, clean and structure the dataset, and derive insights about **movie genres, ratings, and trends** over time. The final data is stored in a **PostgreSQL database** for further querying and analysis.

---

## **Technologies Used**  
- **Python** (`pandas`, `psycopg2`) for data extraction, transformation, and loading.
- **PostgreSQL** for storing and querying structured movie data.
- **SQL queries** for extracting insights from the dataset.

---

## **Project Workflow**  

**Step 1: Set Up Your Environment**
Make sure you have the necessary Python libraries installed to manipulate the dataset and interact with PostgreSQL.

**Step 2: Read the CSV File Using Pandas**
Load the dataset into a pandas DataFrame to start working with it.

**Step 3: Data Exploration and Cleaning**
Explore the data to understand its structure and identify any data quality issues (e.g., missing values, inconsistencies).

**Basic Data Cleaning Steps:**
1. **Check for Missing Values** and handle them (e.g., fill or drop).
2. **Convert Data Types** as necessary (e.g., convert `releaseYear` to integer).
3. **Clean the 'genres' Column** by removing leading or trailing spaces and commas.

**Step 4: Data Transformation**
Transform the dataset to make it more structured and insightful.

**1. Split the `genres` Column**
Since movies can have multiple genres, we will split the `genres` column into individual rows for each genre.
**2. Additional Transformations**

- **Standardize Column Names:** Make column names lowercase and replace spaces with underscores.
- **Convert `releaseYear` to DateTime Format:** This makes it easier to handle dates for analysis.
- **Calculate Decade:** Calculate the decade for each movie based on the `releaseYear`.


---
**Step 5: Connect to PostgreSQL and Load Data**

Now, we'll connect to a PostgreSQL database and insert the cleaned and transformed data.
  
**1. Connect to PostgreSQL:**
Use `psycopg2` to connect to your database.

**2. Insert Data into PostgreSQL:**
Loop through the DataFrame and insert each record into the `movies` table.

---

### **Step 6: Extract Insights**

With the data now in PostgreSQL, you can run SQL queries to extract meaningful insights from it.
**1. Top 5 Most Popular Genres by the Number of Movies:**
**2. Average Rating per Genre:**
**3. Genre Popularity by Decade:**
**4. Most Popular Movies by Votes:**
---

### **Conclusion**

By completing these steps, we will have:

1. Cleaned and transformed the IMDb dataset for analysis.
2. Loaded the data into a PostgreSQL database.
3. Created insightful SQL queries to extract trends and patterns from the data, such as:
    - Popular genres
    - Average ratings by genre
    - Movie popularity trends over the decades


