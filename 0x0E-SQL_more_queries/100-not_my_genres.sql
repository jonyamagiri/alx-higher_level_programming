-- Import the database dump from hbtn_0d_tvshows
-- list all genres not linked to the show Dexter, from the database hbtn_0d_tvshows
-- display: tv_genres.name
-- sorted in ascending order by the genre name; use only two SELECT statements

SELECT
    tv_genres.name
FROM
    tv_genres
WHERE
    tv_genres.name NOT IN(
    SELECT
        tv_genres.name
    FROM
        tv_genres
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE
        tv_shows.title = "Dexter")
ORDER BY
    tv_genres.name ASC;
