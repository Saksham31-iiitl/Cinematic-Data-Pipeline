
SELECT genres, COUNT(*) AS movie_count
FROM movies
GROUP BY genres
ORDER BY movie_count DESC
LIMIT 5;


SELECT genres, AVG(averageRating) AS avg_rating
FROM movies
GROUP BY genres
ORDER BY avg_rating DESC;


SELECT decade, genres, COUNT(*) AS movie_count
FROM movies
GROUP BY decade, genres
ORDER BY decade, movie_count DESC;


SELECT title, genres, numVotes
FROM movies
ORDER BY numVotes DESC
LIMIT 10;
