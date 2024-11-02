
--CREATE TABLE questions (
--    question_id SERIAL PRIMARY KEY,
--    question_text TEXT NOT NULL,
--    answer_a TEXT NOT NULL,
--    answer_b TEXT NOT NULL,
--    answer_c TEXT NOT NULL,
--    answer_d TEXT NOT NULL,
--    correct_answer CHAR(1) CHECK (correct_answer IN ('a', 'b', 'c', 'd')) NOT NULL
--);

--CREATE TABLE players (
--    player_id SERIAL PRIMARY KEY,
--    username VARCHAR(50) UNIQUE NOT NULL,
--    password VARCHAR(100) NOT NULL,  -- better to encrypt
--    email VARCHAR(100) UNIQUE NOT NULL,
--    age INTEGER NOT NULL,
--    questions_solved INTEGER DEFAULT 0
--);

--CREATE TABLE player_answers (
--    player_id INTEGER REFERENCES players(player_id) ON DELETE CASCADE,
--    question_id INTEGER REFERENCES questions(question_id) ON DELETE CASCADE,
--    selected_answer CHAR(1) CHECK (selected_answer IN ('a', 'b', 'c', 'd')) NOT NULL,
--    is_correct BOOLEAN NOT NULL,
--    PRIMARY KEY (player_id, question_id) -- Composite primary key
--);


--CREATE TABLE high_scores (
--    score_id INTEGER PRIMARY KEY CHECK (score_id >= 1 AND score_id <= 20), -- representing scores from 1 to 20
--    player_id INTEGER REFERENCES players(player_id) ON DELETE CASCADE,
--    achieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
--);