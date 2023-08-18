INSERT INTO teacher (name, email, phone, password) VALUES
    ('Emily Johnson', 'emily.johnson@kindergartenschool.com', '12345678901', 'teacherpass1'),
    ('Michael Smith', 'michael.smith@kindergartenschool.com', '98765432102', 'teacherpass2'),
    ('Jessica Williams', 'jessica.williams@kindergartenschool.com', '55512345603', 'teacherpass3'),
    ('Daniel Brown', 'daniel.brown@kindergartenschool.com', '77788899904', 'teacherpass4'),
    ('Sophia Davis', 'sophia.davis@kindergartenschool.com', '22233344405', 'teacherpass5'),
    ('David Wilson', 'david.wilson@kindergartenschool.com', '11122233306', 'teacherpass6');


-- Teacher 1 (Emily Johnson) assigned to class 1
INSERT INTO class_teacher (teacher_id, class_id) VALUES (1, 1);

-- Teacher 2 (Michael Smith) assigned to class 2
INSERT INTO class_teacher (teacher_id, class_id) VALUES (2, 2);

-- Teacher 3 (Jessica Williams) assigned to class 3
INSERT INTO class_teacher (teacher_id, class_id) VALUES (3, 3);

-- Teacher 4 (Daniel Brown) assigned to class 4
INSERT INTO class_teacher (teacher_id, class_id) VALUES (4, 4);

-- Teacher 5 (Sophia Davis) assigned to class 5
INSERT INTO class_teacher (teacher_id, class_id) VALUES (5, 5);

-- Teacher 6 (David Wilson) assigned to class 1
INSERT INTO class_teacher (teacher_id, class_id) VALUES (6, 1);