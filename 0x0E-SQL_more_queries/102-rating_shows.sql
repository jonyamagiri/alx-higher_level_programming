-- Import the database dump from hbtn_0d_tvshows_rate
-- lists all shows by their rating, from hbtn_0d_tvshows_rate
-- display: tv_shows.title - rating sum
-- sorted in descending order by the rating; use only one SELECT statement

SELECT
    tv_shows.title,
    SUM(tv_show_ratings.rate) AS 'rating'
FROM
    tv_shows
INNER JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY
    title
ORDER BY
    rating DESC;
