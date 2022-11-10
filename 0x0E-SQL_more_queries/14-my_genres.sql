-- Import the database dump from hbtn_0d_tvshows
-- lists all genres of the show Dexter
-- display: tv_genres.name
-- sorted in ascending order by the genre name; use only one SELECT statement

SELECT
    tv_genres.name
FROM
    tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE
    tv_shows.title = "Dexter"
ORDER BY
    tv_genres.name ASC;
