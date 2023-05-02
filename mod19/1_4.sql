SELECT avg(overdue_tasks_count), max(overdue_tasks_count), min(overdue_tasks_count)
FROM (
    SELECT sum(assignments_grades.date > assignments.due_date) as overdue_tasks_count
    FROM assignments
    INNER JOIN assignments_grades
    ON assignments.assisgnment_id = assignments_grades.assisgnment_id
    GROUP BY assignments.group_id
    );