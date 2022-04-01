--You did such a great job helping Julia with her last coding contest challenge that she wants you to work on this one, too!
--The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of 0 from your result.

--Input Format
--The following tables contain contest data:
--Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker.

--Column	Type
--hacker_id	Integer
--name	    String

--Submissions: The submission_id is the id of the submission, hacker_id is the id of the hacker who made the submission, challenge_id is the id of the challenge for which the submission belongs to, and score is the score of the submission.

--Column	    Type
--hacker_id	    Integer
--challenge_id	Integer
--submission_id	Integer
--score 	    Integer

SELECT
    t2.hid,
    h.name,
    t2.score
FROM
    (SELECT
        SUM(t1.maxscore) AS score,
        t1.hid as hid
    FROM
        (SELECT
            MAX(score) AS maxscore,
            challenge_id AS cid,
            hacker_id AS hid
        FROM
            submissions
    WHERE
        score > 0
        GROUP BY
            hacker_id,
            challenge_id) t1
    GROUP BY
        hid) t2
JOIN
    hackers h
ON h.hacker_id = t2.hid
ORDER BY
    t2.score DESC,
    t2.hid ASC;