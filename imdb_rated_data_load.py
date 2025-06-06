import psycopg2


conn = psycopg2.connect(
    dbname="your_dbname",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS movies (
    id VARCHAR(10) PRIMARY KEY,
    title VARCHAR(255),
    genres VARCHAR(50),
    averageRating FLOAT,
    numVotes INT,
    releaseYear INT,
    decade INT
);
"""
cur.execute(create_table_query)
conn.commit()


for _, row in df_genres.iterrows():
    insert_query = """
    INSERT INTO movies (id, title, genres, averageRating, numVotes, releaseYear, decade)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING;
    """
    cur.execute(insert_query, tuple(row))
conn.commit()

cur.close()
conn.close()
