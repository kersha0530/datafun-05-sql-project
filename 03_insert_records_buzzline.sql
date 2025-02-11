INSERT INTO users (name, email) VALUES
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com'),
('Charlie Brown', 'charlie@example.com'),
('Eve Adams', 'eve@example.com'),
('Kersha Broussard', 'kersha@example.com');

INSERT INTO messages (user_id, message, sentiment, category) VALUES
(1, 'I love Python!', 0.9, 'tech'),
(2, 'This new recipe is amazing!', 0.8, 'food'),
(3, 'JavaScript is hard but useful.', 0.4, 'tech'),
(4, 'I just watched a great movie.', 0.7, 'entertainment'),
(5, 'That meme was hilarious!', 0.9, 'humor');
