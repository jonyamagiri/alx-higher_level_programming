-- Import the database dump from hbtn_0d_tvshows
-- lists all shows without the genre Comedy, from the database hbtn_0d_tvshows
-- display: tv_shows.title
-- sorted in ascending order by the show title; use only two SELECT statements

SELECT
    tv_shows.title
FROM
    tv_shows
WHERE
    tv_shows.title NOT IN(
    SELECT
        tv_shows.title
    FROM
        tv_shows
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE
        tv_genres.name = "Comedy")
ORDER BY
    tv_shows.title ASC;
