select year(DIFFERENTIATION_DATE) as year,
(
    select max(size_of_colony) from ecoli_data e2
    where year(e2.DIFFERENTIATION_DATE) = year(e1.DIFFERENTIATION_DATE)
)- size_of_colony as year_dev,
ID from ecoli_data e1 order by year, year_dev;