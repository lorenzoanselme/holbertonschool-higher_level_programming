-- Script that lists all records with a score >= 10 in the table second_table
-- Display score and name ordered by score (top first)
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
