--INSERT INTO players (username, password, email, age)
--VALUES
--('john_doe', 'password123', 'john@example.com', 25),
--('jane_smith', 'mypassword', 'jane@example.com', 30),
--('alex_brown', 'securepass', 'alex@example.com', 22),
--('emma_white', 'emma1234', 'emma@example.com', 28),
--('michael_green', 'password789', 'michael@example.com', 35),
--('lucas_black', 'qwerty567', 'lucas@example.com', 40),
--('olivia_blue', 'abc123', 'olivia@example.com', 20),
--('sophia_red', 'password321', 'sophia@example.com', 27),
--('liam_yellow', 'letmein', 'liam@example.com', 33),
--('ava_purple', 'pass567', 'ava@example.com', 29);

INSERT INTO player_answers (player_id, question_id, selected_answer, is_correct)
VALUES
(1, 1, 'a', TRUE),   -- john_doe answered correctly on question 1
(1, 2, 'b', FALSE),  -- Incorrect answer for john_doe
(1, 3, 'a', TRUE),
(1, 4, 'a', TRUE),
(2, 5, 'a', TRUE),   -- jane_smith correct answer
(2, 6, 'b', TRUE),   -- Another correct answer for jane_smith
(2, 7, 'a', TRUE),
(2, 8, 'a', TRUE),
(3, 9, 'b', TRUE),   -- alex_brown correct answer
(3, 10, 'b', TRUE),
(3, 11, 'b', TRUE),
(3, 12, 'b', TRUE),
(4, 13, 'a', TRUE),  -- emma_white correct answer
(4, 14, 'c', TRUE),
(4, 15, 'b', TRUE),
(4, 16, 'a', TRUE),
(5, 17, 'c', TRUE),  -- michael_green correct answer
(5, 18, 'b', TRUE),
(5, 19, 'c', TRUE),
(5, 20, 'c', TRUE),
(6, 1, 'a', TRUE),
(6, 2, 'a', FALSE),
(6, 3, 'a', TRUE),
(6, 4, 'b', FALSE),
(7, 5, 'a', TRUE),
(7, 6, 'b', TRUE),
(7, 7, 'a', TRUE),
(7, 8, 'a', TRUE),
(8, 9, 'b', TRUE),
(8, 10, 'b', TRUE),
(8, 11, 'b', TRUE),
(8, 12, 'b', TRUE),
(9, 13, 'c', FALSE),
(9, 14, 'c', TRUE),
(9, 15, 'b', TRUE),
(9, 16, 'a', TRUE),
(10, 17, 'b', FALSE),
(10, 18, 'b', TRUE),
(10, 19, 'a', FALSE),
(10, 20, 'c', TRUE);
