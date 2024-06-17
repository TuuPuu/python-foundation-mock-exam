'''

PART 1 MULTIPLE CHOICE

QUESTION 01: A

QUESTION 02: C

QUESTION 03: A

QUESTION 04: D

QUESTION 05: B

QUESTION 06: C

QUESTION 07: D

QUESTION 08: A

QUESTION 09: A

QUESTION 10: B

________________________________________________________

PART 2 EVALUATION


1)

Firstly, here is a syntax error after the department id declaration. A comma is missing. It should instead be:

SELECT
    department_id,
    COUNT(*) AS total_admissions
    
    
Secondly, the columns will be mismatched as the group by is using the declaration department_name. Instead it should use department_id, like this:

GROUP BY
    department_id;









'''