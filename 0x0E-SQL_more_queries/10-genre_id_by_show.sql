-- Import the database dump from hbtn_0d_tvshows
-- URL: https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- to import: (create database then use 'curl' to download)
-- 1. $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- 2. $ curl "URL" -s | mysql -uroot -p hbtn_0d_tvshows
-- lists all shows in hbtn_0d_tvshows that have at least one genre linked
-- display: tv_shows.title - tv_show_genres.genre_id
-- sorted in ascending order by tv_shows.title and tv_show_genres.genre_id; use only one SELECT statement

SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY
    tv_shows.title,
    tv_show_genres.genre_id ASC;
