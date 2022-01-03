select coursenumber, department
from students, take
where students.name = 'John Malkovich' and students.ssn = take.ssn;
