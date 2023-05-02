SELECT students.full_name,avg(assignments_grades.grade) avgrade
FROM  students
INNER JOIN assignments_grades on students.student_id = assignments_grades.student_id
GROUP BY students.student_id
ORDER BY avgrade DESC
LIMIT 10