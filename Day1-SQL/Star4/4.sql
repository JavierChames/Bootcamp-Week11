use imdb;
select full_name from actors order by full_name asc;
select count(*) from movies;
select count(*) from movies where genre='action';
select count(*) from movies where genre <>'action';
select year,count(*)  from movies  group by year order by year;
select count(*) from movies  where (title like 'the%' or title like '%the' or title like '%the%');
select count(*) from movies  where title like 'the%';



select * from movies order by year;