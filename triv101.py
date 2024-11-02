import getpass
import re
# import datetime
from datetime import datetime
import psycopg2
import psycopg2.extras


# Helper Functions for Database Operations

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
            choice = input("Continue from previous game session? (Y/N): ").upper()

            if choice == 'Y':
                play_game(player_id)
            else:
                choice = input("Start a new game? (Y/N): ").upper()
                if choice == 'Y':
                    update_query_str = "UPDATE players SET questions_solved = 0 WHERE player_id = %s"
                    upsert_query(cursor, update_query_str, (player_id,))
                    play_game(player_id)
                else:
                    print(f"Goodbye, {user}!")
        else:
            print("Incorrect username/password.")
            retry_choice = input("Try again? (Y/N): ").upper()
            if retry_choice == 'Y':
                user1 = input("Enter username: ")
                pwd1 = getpass.getpass(f"User Name: {user1}\nEnter your password: ")
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
            get_question(answered, player_id)

        connection.commit()
        close_db(connection, cursor)


def get_question(answered: int, player_id: int) -> None:
    while answered < 20:
        connection, cursor = connect_db()
        if connection and cursor:
            select_query_str = "SELECT question_text, answer_a, answer_b, answer_c, answer_d FROM questions WHERE question_id = %s"
            question = select_query(cursor, select_query_str, (answered,))

            if question:
                question = question[0]
                print(f"Q: {question['question_text']}")
                print(
                    f"A: {question['answer_a']}, B: {question['answer_b']}, C: {question['answer_c']}, D: {question['answer_d']}")

                u_answer = input("What is your answer? ")

                select_answer = "SELECT correct_answer FROM questions WHERE question_id = %s"
                correct_answer = select_query(cursor, select_answer, (answered,))

                if correct_answer and u_answer == correct_answer[0]['correct_answer']:
                    is_correct = True
                else:
                    is_correct = False

                insert_str = """INSERT INTO player_answers (player_id, question_id, selected_answer, is_correct)
                                      VALUES (%s, %s, %s, %s);"""
                insert_values = (player_id, answered, u_answer, is_correct)
                upsert_query(cursor, insert_str, insert_values)

                answered += 1

            print("You have completed the game!")
            # Logic for updating high scores can go here.
            upsert_high_scores(player_id)

            connection.commit()
            close_db(connection, cursor)


def upsert_high_scores(player_id: int) -> None:
    connection, cursor = connect_db()

    try:
        if connection and cursor:
            # Check if the player already has a high score
            select_str = "SELECT * FROM high_scores WHERE player_id = %s"
            exists = select_query(cursor, select_str, (player_id,))

            achieved_at = datetime.now()

            # If the high score exists, update it
            if exists:
                update_str = "UPDATE high_scores SET achieved_at = %s WHERE player_id = %s"
                upsert_query(cursor, update_str, (achieved_at, player_id))
            # Otherwise, insert a new high score record
            else:
                insert_str = """INSERT INTO high_scores (player_id, achieved_at) 
                                VALUES (%s, %s);"""
                upsert_query(cursor, insert_str, (player_id, achieved_at))

            # Fetch and display the top 20 high scores
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
                ORDER BY score DESC, achieved_at DESC 
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

def stats_menu()->None:
    '''
    Opens the statistics manu of the trivia. Allows statistics menu actions
    :return:
    None
    '''
    print("work in progress...")
    # while True:
    #     print("===========Main Menu==============")
    #     print(
    #         "0 - number of players\n1 - question with most right answers\n2 - question with most wrong answers\n"
    #         "3 - players list ordered by right answers\n4 - players ordered by questions answered\n5 - player stats\n"
    #         "6 - question stats\n\n999 - exit");
    #     try:
    #         action: int = int(input("What data is required? "));
    #         match action:
    #             case 0:
    #
    #             case 1:
    #
    #             case 2:
    #
    #             case 3:
    #
    #             case 4:
    #
    #             case 5:
    #
    #             case 6:
    #
    #             case 999:
    #                 print("leaving the stats menu, have a nice day!")
    #                 break;
    #             case _:
    #                 print("invalid input");
    #                 continue;
    #
    #         print();
    #
    #     except TypeError as e:
    #         print(f"{str(e)} - is not a valid input");
    #
    #     except Exception as e:
    #         print(f"{e} - error has occurred");
    #     finally:
    #         print("Have a great day!")

def main_menu()->None:
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

