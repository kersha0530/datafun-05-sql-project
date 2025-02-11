SELECT users.name, messages.message, messages.sentiment
FROM users
INNER JOIN messages ON users.user_id = messages.user_id;
