use imdb;
select full_name from actors where full_name like 'Dan%';
select count(*) from actors where full_name like 'ben%';
select salary from cast order by salary asc limit 5;
