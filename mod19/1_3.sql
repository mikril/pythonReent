SELECT students.full_name
FROM students
INNER JOIN students_groups ON students.group_id = students_groups.group_id
INNER JOIN ( SELECT teachers.teacher_id,avg(assignments_grades.grade) avgrade
FROM  teachers,assignments_grades
WHERE teachers.teacher_id=(
    SELECT teacher_id
    FROM assignments
    WHERE assignments.assisgnment_id = assignments_grades.assisgnment_id)
GROUP BY teachers.teacher_id
ORDER BY avgrade DESC
LIMIT 1) as easy
ON students_groups.teacher_id=easy.teacher_id