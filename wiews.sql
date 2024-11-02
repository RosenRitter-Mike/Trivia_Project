--CREATE VIEW question_answer_count AS
--SELECT question_id, COUNT(*) AS so_cnt
--FROM player_answers
--GROUP BY question_id
--ORDER BY so_cnt DESC;

--CREATE VIEW question_correct_count AS
--SELECT question_id, COUNT(*) AS cor_cnt
--FROM player_answers
--where is_correct = True
--GROUP BY question_id
--ORDER BY cor_cnt DESC;

--CREATE VIEW question_wrong_count AS
--SELECT question_id, COUNT(*) AS wr_cnt
--FROM player_answers
--where is_correct = false 
--GROUP BY question_id
--ORDER BY wr_cnt DESC;

--CREATE VIEW player_answer_count AS
--SELECT player_id, COUNT(*) AS pso_cnt
--FROM player_answers
--GROUP BY player_id
--ORDER BY pso_cnt DESC;
--
--CREATE VIEW player_correct_count AS
--SELECT player_id, COUNT(*) AS pcor_cnt
--FROM player_answers
--where is_correct = True
--GROUP BY player_id
--ORDER BY pcor_cnt DESC;
--
CREATE VIEW player_wrong_count AS
SELECT player_id, COUNT(*) AS pwr_cnt
FROM player_answers
where is_correct = false 
GROUP BY player_id
ORDER BY pwr_cnt DESC;
--
