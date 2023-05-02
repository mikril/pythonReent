SELECT teachers.full_name,avg(assignments_grades.grade) avgrade
FROM  teachers
INNER JOIN assignments on teachers.teacher_id = assignments.teacher_id
INNER JOIN assignments_grades on assignments.assisgnment_id = assignments_grades.assisgnment_id
GROUP BY teachers.teacher_id
ORDER BY avgrade
LIMIT 1