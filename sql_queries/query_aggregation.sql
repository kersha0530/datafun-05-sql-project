SELECT category, COUNT(*) AS message_count, AVG(sentiment) AS avg_sentiment
FROM messages
GROUP BY category;
