insert into Professors (name, SSN) values
        ('Jarek Gryz', '111111111'),
        ('Paul Skoufranis', '222222222');

insert into Students (name, SSN) values
        ('John Malkovich', '333333333'),
        ('Steven Chen', '444444444'),
        ('Oscar Whiley', '555555555'),
        ('Emma Whyte', '666666666');

insert into gtas (name, SSN, salary) values
        ('Oscar Whiley', '555555555', 38.81),
        ('Emma Whyte', '666666666', 27.00);

insert into team (teamid) values
        (1),
        (2),
        (3),
        (4);

insert into class (department, coursenumber) values
        ('EECS', 3421),
        ('EECS', 3101),
        ('MATH', 1300),
        ('MATH', 1310);

insert into section (sectionid, department, coursenumber) values
        ('A', 'EECS', 3421 ),
        ('B', 'EECS', 3101),
        ('C', 'MATH', 1300),
        ('D', 'MATH', 1310);

insert into on_team1 (SSN, TeamID) values
        ('111111111', 1),
        ('111111111', 2),
        ('222222222', 3),
        ('222222222', 4);

insert into on_team2 (SSN, TeamID) values
        ('555555555', 1),
        ('555555555', 2),
        ('666666666', 3),
        ('666666666', 4);

insert into admin (rating, teamid, sectionid, department, coursenumber) values
        (9, 1, 'A', 'EECS', 3421),
        (7, 2, 'B', 'EECS', 3101),
        (7, 3, 'C', 'MATH', 1300),
        (10, 4, 'D', 'MATH', 1310);

insert into wait_for (waitlist_rank, sectionid, department, coursenumber, ssn) values
        (1, 'A', 'EECS', 3421, '444444444'),
        (9, 'D', 'MATH', 1310, '444444444');

insert into take (grade, sectionid, department, coursenumber, ssn) values
        ('A+', 'A', 'EECS', 3421, '333333333'),
        ('A+', 'B', 'EECS', 3101, '333333333'),
        ('B+', 'C', 'MATH', 1300, '333333333'),
        ('B+', 'D', 'MATH', 1310, '333333333'),
        ('A+', 'A', 'EECS', 3421, '444444444'),
        ('B+', 'B', 'EECS', 3101, '444444444');

insert into req_of (pr_department, pr_coursenumber, r_department, r_coursenumber) values
        ('MATH', 1300, 'MATH', 1310);
