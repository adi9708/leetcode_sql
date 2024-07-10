# Write your MySQL query statement below
Select q1.person_name 
From queue q1
Inner join queue q2
on q1.turn >= q2.turn
Group by q1.turn
Having sum(q2.weight) <= 1000
order by q1.turn desc limit 1


