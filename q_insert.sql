--TRUNCATE TABLE player_answers, high_scores, questions, players RESTART IDENTITY CASCADE;

-- Art Questions
--INSERT INTO questions (question_text, answer_a, answer_b, answer_c, answer_d, correct_answer)
--VALUES
--('Who painted the Mona Lisa?', 'Leonardo da Vinci', 'Vincent van Gogh', 'Pablo Picasso', 'Claude Monet', 'a'),
--('The Starry Night is a famous painting by which artist?', 'Claude Monet', 'Pablo Picasso', 'Vincent van Gogh', 'Leonardo da Vinci', 'c'),
--('What material did Michelangelo use to create his sculpture David?', 'Marble', 'Bronze', 'Wood', 'Clay', 'a'),
--('Which artist is known for the painting "Guernica"?', 'Pablo Picasso', 'Salvador Dali', 'Henri Matisse', 'Edvard Munch', 'a');

-- History Questions
--INSERT INTO questions (question_text, answer_a, answer_b, answer_c, answer_d, correct_answer)
--VALUES
--('Who was the first president of the United States?', 'George Washington', 'Abraham Lincoln', 'Thomas Jefferson', 'John Adams', 'a'),
--('In which year did World War I begin?', '1912', '1914', '1916', '1918', 'b'),
--('Who was the ancient Egyptian queen known for her relationship with Julius Caesar and Mark Antony?', 'Cleopatra', 'Nefertiti', 'Hatshepsut', 'Merneith', 'a'),
--('Which empire was ruled by the Caesars?', 'Roman Empire', 'Ottoman Empire', 'Byzantine Empire', 'Holy Roman Empire', 'a');

-- Music Questions
--INSERT INTO questions (question_text, answer_a, answer_b, answer_c, answer_d, correct_answer)
--VALUES
--('Who composed the opera "The Magic Flute"?', 'Ludwig van Beethoven', 'Wolfgang Amadeus Mozart', 'Johann Sebastian Bach', 'Franz Schubert', 'b'),
--('Which band released the album "Abbey Road"?', 'The Rolling Stones', 'The Beatles', 'Led Zeppelin', 'Pink Floyd', 'b'),
--('Who is known as the "King of Pop"?', 'Elvis Presley', 'Michael Jackson', 'Freddie Mercury', 'Prince', 'b'),
--('What instrument does a cellist play?', 'Violin', 'Cello', 'Piano', 'Flute', 'b');

-- Cinema Questions
--INSERT INTO questions (question_text, answer_a, answer_b, answer_c, answer_d, correct_answer)
--VALUES
--('Which movie won the Academy Award for Best Picture in 1994?', 'Forrest Gump', 'The Shawshank Redemption', 'Pulp Fiction', 'Braveheart', 'a'),
--('Who directed "Inception"?', 'Martin Scorsese', 'Quentin Tarantino', 'Christopher Nolan', 'Steven Spielberg', 'c'),
--('Which actor played the character of Tony Stark in the Marvel movies?', 'Chris Evans', 'Robert Downey Jr.', 'Chris Hemsworth', 'Mark Ruffalo', 'b'),
--('What was the first feature-length animated movie ever released?', 'Snow White and the Seven Dwarfs', 'Fantasia', 'Cinderella', 'The Jungle Book', 'a');


-- Geography Questions
--INSERT INTO questions (question_text, answer_a, answer_b, answer_c, answer_d, correct_answer)
--VALUES
--('What is the capital of France?', 'Berlin', 'Madrid', 'Paris', 'Rome', 'c'),
--('Which river flows through Egypt?', 'Amazon', 'Nile', 'Danube', 'Mississippi', 'b'),
--('Mount Everest is located in which mountain range?', 'Alps', 'Andes', 'Himalayas', 'Rocky Mountains', 'c'),
--('Which country is the largest by land area?', 'USA', 'China', 'Russia', 'Canada', 'c');

-- History Questions (More Difficult)
--INSERT INTO questions (question_text, answer_a, answer_b, answer_c, answer_d, correct_answer)
--VALUES
--('Which treaty ended the Thirty Years'' War in 1648?', 
-- 'Treaty of Westphalia', 'Treaty of Versailles', 'Treaty of Utrecht', 'Treaty of Vienna', 'a'),
--('Who led the Haitian Revolution that resulted in the abolition of slavery and the founding of Haiti?', 
-- 'Toussaint Louverture', 'Jean-Jacques Dessalines', 'François-Dominique Toussaint', 'Henri Christophe', 'a'),
--('What year did the Byzantine Empire fall with the conquest of Constantinople by the Ottomans?', 
-- '1453', '1521', '1492', '1415', 'a'),
--('Who was the British Prime Minister during the signing of the Munich Agreement in 1938?', 
-- 'Winston Churchill', 'Neville Chamberlain', 'Clement Attlee', 'Stanley Baldwin', 'b');

-- Greek Mythology Questions
--INSERT INTO questions (question_text, answer_a, answer_b, answer_c, answer_d, correct_answer)
--VALUES
--('Who was the wife of Hades and queen of the underworld?', 'Persephone', 'Aphrodite', 'Hera', 'Athena', 'a'),
--('What was the name of the Titan who was condemned to hold up the sky for eternity?', 'Atlas', 'Prometheus', 'Cronus', 'Oceanus', 'a'),
--('Which Greek hero killed the Minotaur?', 'Theseus', 'Heracles', 'Achilles', 'Odysseus', 'a'),
--('Which goddess was born from the foam of the sea?', 'Aphrodite', 'Hera', 'Artemis', 'Demeter', 'a');

-- Basic Computer Knowledge Questions
--INSERT INTO questions (question_text, answer_a, answer_b, answer_c, answer_d, correct_answer)
--VALUES
--('What does "CPU" stand for in computing?', 'Central Processing Unit', 'Control Processing Unit', 'Computer Processing Unit', 'Central Program Unit', 'a'),
--('Which programming language is known for its snake logo and readability?', 'Python', 'Java', 'C++', 'Ruby', 'a'),
--('Which file extension is used for Microsoft Excel documents?', '.xlsx', '.docx', '.pptx', '.txt', 'a'),
--('What does "HTML" stand for?', 'HyperText Markup Language', 'HyperText Machine Language', 'HighText Markup Language', 'HyperText Multiple Language', 'a');

-- Classic Literature Questions
--INSERT INTO questions (question_text, answer_a, answer_b, answer_c, answer_d, correct_answer)
--VALUES
--('Who is the author of "The Odyssey"?', 'Homer', 'Sophocles', 'Virgil', 'Aeschylus', 'a'),
--('In which Shakespearean play does the character Iago appear?', 'Othello', 'Hamlet', 'Macbeth', 'King Lear', 'a'),
--('What is the name of the novel by Mary Shelley that tells the story of a scientist who creates life?', 'Frankenstein', 'Dracula', 'The Invisible Man', 'The Strange Case of Dr Jekyll and Mr Hyde', 'a'),
--('Which novel, written by Jane Austen, features the characters Elizabeth Bennet and Mr. Darcy?', 'Pride and Prejudice', 'Emma', 'Sense and Sensibility', 'Mansfield Park', 'a');

--INSERT INTO questions (question_text, answer_a, answer_b, answer_c, answer_d, correct_answer)
--VALUES
--('Which leader initiated the Cultural Revolution in China?', 'Mao Zedong', 'Deng Xiaoping', 'Zhou Enlai', 'Chiang Kai-shek', 'a'),
--('The Battle of Stalingrad during World War II was fought between which two major forces?', 'Soviet Union and Nazi Germany', 'United States and Japan', 'Soviet Union and Italy', 'Nazi Germany and the United Kingdom', 'a'),
--('Who was the first Emperor of unified Germany in 1871?', 'Wilhelm I', 'Frederick the Great', 'Otto von Bismarck', 'Franz Joseph I', 'a'),
--('Which event directly led to the United States entering World War I in 1917?', 'The Zimmerman Telegram', 'Sinking of the Lusitania', 'Assassination of Archduke Ferdinand', 'Treaty of Brest-Litovsk', 'a');

-- 20th-Century Classic Literature Questions
--INSERT INTO questions (question_text, answer_a, answer_b, answer_c, answer_d, correct_answer)
--VALUES
--('Who wrote the novel "1984", which explores a dystopian future under a totalitarian regime?', 'George Orwell', 'Aldous Huxley', 'Ray Bradbury', 'Philip K. Dick', 'a'),
--('Which American author wrote "The Great Gatsby," a novel about the American Dream and disillusionment in the 1920s?', 'F. Scott Fitzgerald', 'Ernest Hemingway', 'William Faulkner', 'John Steinbeck', 'a'),
--('Who is the author of "One Hundred Years of Solitude," a landmark in magical realism?', 'Gabriel García Márquez', 'Jorge Luis Borges', 'Isabel Allende', 'Mario Vargas Llosa', 'a'),
--('Which Nobel Prize-winning author wrote "The Old Man and the Sea"?', 'Ernest Hemingway', 'William Faulkner', 'Toni Morrison', 'John Steinbeck', 'a');

INSERT INTO questions (question_text, answer_a, answer_b, answer_c, answer_d, correct_answer)
VALUES
('Which existentialist author wrote "The Stranger" and won the Nobel Prize in Literature in 1957?', 'Albert Camus', 'Jean-Paul Sartre', 'Franz Kafka', 'Simone de Beauvoir', 'a'),
('Which powerful Japanese daimyo played a key role in unifying Japan in the late 16th century before his death in 1582?', 'Oda Nobunaga', 'Tokugawa Ieyasu', 'Toyotomi Hideyoshi', 'Uesugi Kenshin', 'a'),
('Which band released the album "Ride the Lightning" in 1984, featuring iconic songs such as "Creeping Death" and "Fade to Black"?', 'Metallica', 'Megadeth', 'Slayer', 'Anthrax', 'a'),
('Which French military commander is considered one of the greatest tacticians of his time and served under Louis XIV?', 'Henri de Turenne', 'Maurice de Saxe', 'Louis de Bourbon', 'Jean-Baptiste Colbert', 'a'),
('Which Apache leader led resistance against Mexico and the United States during the Apache Wars in the late 19th century?', 'Geronimo', 'Cochise', 'Sitting Bull', 'Crazy Horse', 'a'),
('Who is the captain of the USS Enterprise-D in the television series "Star Trek: The Next Generation"?', 'Captain Picard', 'Captain Kirk', 'Commander Riker', 'Captain Sisko', 'a');
