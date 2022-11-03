-- Import the database dump from hbtn_0d_tvshows
-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- display: <TV Show genre> - <Number of shows linked to this genre>
-- first column name is genre; second column name is number_of_shows
-- don’t display a genre that doesn’t have any shows linked
-- sorted in descending order by the number of shows linked; use only one SELECT statement

SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_shows DESC;
