CREATE OR REPLACE FUNCTION update_answered_after_insert()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE players
    SET questions_solved = questions_solved + 1
    WHERE player_id = NEW.player_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_answered_after_insert_trigger
AFTER INSERT ON player_answers
FOR EACH ROW
EXECUTE FUNCTION update_answered_after_insert();