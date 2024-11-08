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
--CREATE VIEW player_wrong_count AS
--SELECT player_id, COUNT(*) AS pwr_cnt
--FROM player_answers
--where is_correct = false 
--GROUP BY player_id
--ORDER BY pwr_cnt DESC;
--
--CREATE VIEW player_stats_correct AS
--select p.username, cr.cnt as correct
--from players p
--join (select player_id, count(*) cnt
--    from player_answers
--    where is_correct = True
--    group by player_id) as cr using(player_id)
--    order by correct desc
--
--CREATE VIEW question_stats AS
--select q.question_text, so.so_cnt answered, cor.cor_cnt correct_answers, wr.wr_cnt wrong_answers
--from questions q 
--join question_answer_count so using(question_id)
--join question_correct_count cor using(question_id)
--join question_wrong_count wr using(question_id)

CREATE VIEW player_stats_id AS
select p.player_id, p.username, pl_so.pso_cnt answered, pl_cor.pcor_cnt correct_answers, pl_wr.pwr_cnt wrong_answers
from players p 
join player_answer_count pl_so using(player_id)
join player_correct_count pl_cor using(player_id)
join player_wrong_count pl_wr using(player_id)
