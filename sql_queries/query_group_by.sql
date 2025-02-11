SELECT user_id, COUNT(*) AS message_count
FROM messages
GROUP BY user_id
ORDER BY message_count DESC;
