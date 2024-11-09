import getpass
import re
# import datetime
from datetime import datetime
import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def connect_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="admin",
            password="admin",
            port="5556"
        )
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return connection, cursor
    except Exception as error:
        print(f"Error connecting to database: {error}")
        return None, None


def select_query(cursor, query, params=None):
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()
    except Exception as error:
        print(f"Error executing SELECT query: {error}")
        return None


def upsert_query(cursor, query, params):
    try:
        cursor.execute(query, params)
    except Exception as error:
        print(f"Error executing UPSERT query: {error}")


def close_db(connection, cursor):
    if cursor:
        cursor.close()
    if connection:
        connection.close()


# Main Functions

def create_new_player() -> None:
    while True:
        user = input("Enter username: ")
        print("Username input accepted")
        try:
            # pwd = getpass.getpass(f"User Name: {user}\nEnter your password: ")
            # pwd2 = getpass.getpass("Please enter the password again: ")
            pwd = input(f"User Name: {user}\nEnter your password: ")
            pwd2 = input("Please enter the password again: ")
        except Exception as e:
            print(f"Error with password input: {e}")
            return  # Exit if there’s an error in password entry

        if pwd == pwd2:
            email = input("Enter your email: ")
            valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
            if not valid:
                print("Invalid email address.")
                continue

            try:
                age = int(input("Enter your age: "))
                if age < 3 or age > 125:
                    print("Invalid age.")
                    continue
            except ValueError:
                print("Age must be a number.")
                continue

            print("Welcome!!!")
            break
        else:
            print("Passwords do not match. Try again.")
            continue

    connection, cursor = connect_db()
    if connection and cursor:
        insert_query = """INSERT INTO players (username, password, email, age, questions_solved)
                          VALUES (%s, %s, %s, %s, %s) RETURNING player_id;"""
        insert_values = (user, pwd, email, age, 0)
        try:
            cursor.execute(insert_query, insert_values)
            new_id = cursor.fetchone()[0]
            print(f'New player ID: {new_id}')
            connection.commit()
        except Exception as error:
            print(f"Error inserting new player: {error}")
        finally:
            close_db(connection, cursor)


def login_player(user: str, pwd: str) -> None:
    connection, cursor = connect_db()
    if connection and cursor:
        select_query_str = "SELECT player_id, password FROM players WHERE username = %s"
        result = select_query(cursor, select_query_str, (user,))

        if result and result[0]['password'] == pwd:
            player_id = result[0]['player_id']

            choice = input("Start a new game? (Y/N): ").upper()

            if choice == 'Y':
                delete_query_str = "DELETE FROM player_answers WHERE player_id = %s"
                upsert_query(cursor, delete_query_str, (player_id,))

                update_query_str = "UPDATE players SET questions_solved = 0 WHERE player_id = %s"
                upsert_query(cursor, update_query_str, (player_id,))

                play_game(player_id)

            else:
                choice = input("Continue from previous game session? (Y/N): ").upper()
                if choice == 'Y':
                    play_game(player_id)
                else:
                    print(f"Goodbye, {user}!")
        else:
            print("Incorrect username/password.")
            retry_choice = input("Try again? (Y/N): ").upper()
            if retry_choice == 'Y':
                user1 = input("Enter username: ")
                # pwd1 = getpass.getpass(f"User Name: {user1}\nEnter your password: ")
                pwd1 = input(f"User Name: {user1}\nEnter your password: ")
                login_player(user1, pwd1)
            else:
                return

        connection.commit()
        close_db(connection, cursor)


def play_game(player_id: int) -> None:
    connection, cursor = connect_db()
    if connection and cursor:

        select_query_str = "SELECT questions_solved FROM players WHERE player_id = %s"
        result = select_query(cursor, select_query_str, (player_id,))

        if result:
            answered = result[0]['questions_solved']
        else:
            answered = 0

        print(f"Starting game with {answered} questions answered so far.")
        get_question(answered + 1, player_id)

        connection.commit()
        close_db(connection, cursor)


def get_question(answered: int, player_id: int) -> None:
    connection, cursor = connect_db()
    if connection and cursor:
        try:
            while answered < 20:
                print(f"Fetching question ID: {answered}")
                select_query_str = "SELECT question_text, answer_a, answer_b, answer_c, answer_d, correct_answer FROM questions WHERE question_id = %s"
                question = select_query(cursor, select_query_str, (answered,))

                if not question:
                    print("No question found for the given question ID.")
                    break

                question = question[0]
                print(f"Q: {question['question_text']}")
                print(
                    f"A: {question['answer_a']}, B: {question['answer_b']}, C: {question['answer_c']}, D: {question['answer_d']}")

                p_answer = input("Your answer (or 'Q' to quit, 'S' for stats): ").strip()

                if p_answer.upper() == 'Q':
                    print("Exiting to main menu...")
                    main_menu()
                    return
                elif p_answer.upper() == 'S':
                    print("Fetching player stats...")
                    select_query_str = "SELECT COUNT(*) FROM player_answers WHERE player_id = %s AND is_correct = TRUE"
                    c_ans = select_query(cursor, select_query_str, (player_id,))[0]['count']
                    select_query_str = "SELECT COUNT(*) FROM player_answers WHERE player_id = %s AND is_correct = FALSE"
                    w_ans = select_query(cursor, select_query_str, (player_id,))[0]['count']
                    print(f"You answered {c_ans} questions correctly, and {w_ans} of your answers are wrong.")
                    continue

                correct_answer = question['correct_answer']

                is_correct = (p_answer.lower() == correct_answer.lower())
                if is_correct:
                    print("Correct answer!")
                else:
                    print("Wrong answer!")

                insert_str = """INSERT INTO player_answers (player_id, question_id, selected_answer, is_correct)
                                VALUES (%s, %s, %s, %s);"""
                insert_values = (player_id, answered, p_answer, is_correct)
                upsert_query(cursor, insert_str, insert_values)

                update_query_str = "UPDATE players SET questions_solved = %s WHERE player_id = %s"
                upsert_query(cursor, update_query_str, (answered, player_id))

                answered += 1
                # continue

            print("You have completed the game!")
            upsert_high_scores(player_id)
        finally:
            connection.commit()
            close_db(connection, cursor)


def upsert_high_scores(player_id: int) -> None:
    connection, cursor = connect_db()

    try:
        if connection and cursor:
            select_str = "SELECT * FROM high_scores WHERE player_id = %s"
            exists = select_query(cursor, select_str, (player_id,))

            achieved_at = datetime.now()

            if exists:
                update_str = "UPDATE high_scores SET achieved_at = %s WHERE player_id = %s"
                upsert_query(cursor, update_str, (achieved_at, player_id))
            else:
                select_max_id = "SELECT COALESCE(MAX(score_id), 0) + 1 FROM high_scores"
                cursor.execute(select_max_id)
                new_score_id = cursor.fetchone()[0]

                insert_str = """INSERT INTO high_scores (score_id, player_id, achieved_at) 
                                VALUES (%s, %s, %s);"""
                upsert_query(cursor, insert_str, (new_score_id, player_id, achieved_at))

            select_str = '''
                SELECT p.player_id, p.username, p.email, COUNT(sc.*) as score, hs.achieved_at
                FROM high_scores hs
                JOIN players p USING(player_id)
                JOIN (
                    SELECT player_id, COUNT(*) 
                    FROM player_answers
                    WHERE is_correct = True
                    GROUP BY player_id
                ) sc USING(player_id)
                GROUP BY p.player_id, hs.achieved_at
                ORDER BY score DESC, hs.achieved_at DESC 
                LIMIT 20;
            '''
            high_scores = select_query(cursor, select_str)

            print("_______________________High Scores Table____________________________")
            if high_scores:
                for score in high_scores:
                    scores_dict = dict(score)
                    print(scores_dict)

            connection.commit()
    finally:
        close_db(connection, cursor)


def create_pie(player_id: int) -> None:
    connection, cursor = connect_db()
    try:
        if connection and cursor:
            select_str = "SELECT username, correct_answers, wrong_answers FROM player_stats_id WHERE player_id = %s"
            result = select_query(cursor, select_str, (player_id,))

            if result:
                correct = result[0]['correct_answers']
                wrong = result[0]['wrong_answers']
                unanswered = 20 - correct - wrong
                username = result[0]['username']

                labels = ['Correct', 'Wrong', 'Unanswered']
                sizes = [correct, wrong, unanswered]
                colors = ['#50C878', '#DC143C', '#007FFF']

                explode = [0.1, 0, 0]

                plt.figure(figsize=(6, 6))
                plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                        startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})

                plt.title(f"Player {username} - Answer Distribution")
                plt.show()
            else:
                print(f"No stats found for player ID {player_id}.")

        connection.commit()
    finally:
        close_db(connection, cursor)


def create_bar() -> None:
    connection, cursor = connect_db()
    try:
        if connection and cursor:
            select_str = "SELECT question_text, answered, correct_answers, wrong_answers FROM question_stats"
            result = select_query(cursor, select_str)

            if result:
                df = pd.DataFrame(result)

                print("Column names in DataFrame:", df.columns)
                print(df.head())

                df.columns = ['question_text', 'answered', 'correct_answers', 'wrong_answers']

                df_melted = df.melt(id_vars='question_text',
                                    value_vars=['answered', 'correct_answers', 'wrong_answers'],
                                    var_name='Answer Type', value_name='Count')

                plt.figure(figsize=(12, 8))
                sns.barplot(x='question_text', y='Count', hue='Answer Type', data=df_melted, palette='bright')

                plt.title("Question Answer Statistics")
                plt.xlabel("Questions")
                plt.ylabel("Count")
                plt.xticks(rotation=45, ha='right')
                plt.legend(title='Answer Type')
                plt.tight_layout()

                plt.show()
            else:
                print("No data found in question_stats.")

        connection.commit()
    finally:
        close_db(connection, cursor)


def stats_menu() -> None:
    '''
    Opens the statistics manu of the trivia. Allows statistics menu actions
    :return:
    None
    '''
    print("work in progress...")
    while True:
        print("===========Stats Menu==============")
        print(
            "0 - number of players\n1 - question with most right answers\n2 - question with most wrong answers\n"
            "3 - players list ordered by right answers\n4 - players ordered by questions answered\n5 - player stats\n"
            "6 - question stats\n\n999 - exit");
        try:
            action: int = int(input("What data is required? "));
            match action:
                case 0:
                    connection, cursor = connect_db()

                    try:
                        if connection and cursor:
                            select_str = "select count(distinct player_id) from players"
                            result = select_query(cursor, select_str);
                            print(f"Number of players = {result[0][0]}");
                        connection.commit()
                    finally:
                        close_db(connection, cursor);
                case 1:
                    connection, cursor = connect_db()

                    try:
                        if connection and cursor:
                            select_str = ("select question_id from question_correct_count"
                                          " where cor_cnt = (select max(cor_cnt) from question_correct_count)"
                                          " group by question_id")
                            result = select_query(cursor, select_str);
                            print(f"Question with most correct answers = {result}");
                        connection.commit()
                    finally:
                        close_db(connection, cursor);
                case 2:
                    connection, cursor = connect_db()

                    try:
                        if connection and cursor:
                            select_str = ("select question_id from question_wrong_count"
                                          " where wr_cnt = (select max(wr_cnt) from question_wrong_count)"
                                          " group by question_id")

                            result = select_query(cursor, select_str);
                            print(f"Question with most wrong answers = {result}");
                        connection.commit()
                    finally:
                        close_db(connection, cursor);
                case 3:
                    connection, cursor = connect_db()

                    try:
                        if connection and cursor:
                            select_str = "select * from player_stats_correct"
                            result = select_query(cursor, select_str);
                            print("Player Stats", result);
                        connection.commit()
                    finally:
                        close_db(connection, cursor);
                case 4:
                    connection, cursor = connect_db()

                    try:
                        if connection and cursor:
                            select_str = ("select username, questions_solved "
                                          "from players "
                                          "order by questions_solved desc")
                            result = select_query(cursor, select_str);
                            print("players ordered by questions answered", result);
                        connection.commit()
                    finally:
                        close_db(connection, cursor);
                case 5:
                    connection, cursor = connect_db()
                    player_id = int(input("player id: "));
                    create_pie(player_id);
                    try:
                        if connection and cursor:
                            select_str = ("select * from player_stats_id psi "
                                          "where player_id = %s")
                            result = select_query(cursor, select_str, (player_id,))
                            print("player stats", result);
                        connection.commit()
                    finally:
                        close_db(connection, cursor);

                case 6:
                    connection, cursor = connect_db()
                    try:
                        if connection and cursor:
                            select_str = "select * from question_stats"
                            result = select_query(cursor, select_str);
                            print("Question statistics", result);
                        connection.commit()
                    finally:
                        close_db(connection, cursor);
                        create_bar();

                case 999:
                    print("leaving the stats menu, have a nice day!")
                    break;

                case _:
                    print("invalid input");
                    continue;

            print();

        except TypeError as e:
            print(f"{str(e)} - is not a valid input");

        except Exception as e:
            print(f"{e} - error has occurred");
        finally:
            print("Have a great day!")


def main_menu() -> None:
    '''
    Opens the main manu of the trivia. Allows main menu actions
    :return:
    None
    '''

    # action: int = None;
    while True:
        print("===========Main Menu==============")
        print(
            "0 - register new player\n1 - login existing\n2 - view statistics\n999 - exit");
        try:
            action: int = int(input("What is the purpose of your visit? "));
            match action:
                case 0:
                    create_new_player()
                case 1:
                    name = input("username: ")
                    pwd = input("password: ")
                    login_player(name, pwd);
                case 2:
                    stats_menu();

                case 999:
                    print("leaving the system, have a nice day!")
                    break;
                case _:
                    print("invalid input");
                    continue;

            print();

        except TypeError as e:
            print(f"{str(e)} - is not a valid input");

        except Exception as e:
            print(f"{e} - error has occurred");
        finally:
            print("Have a great day!")
