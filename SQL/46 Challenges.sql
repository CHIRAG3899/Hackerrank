--Julia asked her students to create some coding challenges. Write a query to print the hacker_id, name, and the total number of challenges created by each student. Sort your results by the total number of challenges in descending order. If more than one student created the same number of challenges, then sort the result by hacker_id. If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.

--Input Format
--The following tables contain challenge data:
--Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker.

--Column	Type
--hacker_id	Integer
--name	    String

--Challenges: The challenge_id is the id of the challenge, and hacker_id is the id of the student who created the challenge.

--Column	    Type
--hacker_id	    Integer
--challenge_id	Integer

/*1st SELECTING THE VALUES requested to be printed*/
SELECT h.hacker_id, h.name, COUNT(c.challenge_id) AS challenge_counter
FROM hackers h
JOIN challenges c
    ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name

/*2nd applying the values found before*/

HAVING challenge_counter IN (
    SELECT aux_table.counter
    FROM(
        SELECT hacker_id, COUNT(challenge_id) AS counter 
        FROM challenges
        GROUP BY hacker_id
        ORDER BY counter DESC
    ) AS aux_table
    GROUP BY aux_table.counter 
    HAVING COUNT(aux_table.counter) = 1
)
OR
challenge_counter =(
    SELECT MAX(aux_table.counter)
    FROM(
        SELECT hacker_id, COUNT(challenge_id) AS counter
        FROM challenges
        GROUP BY hacker_id
        ORDER BY counter DESC
    ) AS aux_table)
/* Finally we order as requested (by counter and hacker_id)*/
ORDER BY challenge_counter DESC, h.hacker_id ASC;
