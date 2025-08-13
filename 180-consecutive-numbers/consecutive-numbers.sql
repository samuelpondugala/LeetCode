# Write your MySQL query statement below
with cte as (
    select num, lead(num,1) over() num1, lag(num, 1) over() num2 from logs
)
select distinct num ConsecutiveNums from cte where (num=num1) and (num=num2);