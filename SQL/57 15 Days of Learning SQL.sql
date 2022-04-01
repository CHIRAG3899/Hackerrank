--Julia conducted a 15 days of learning SQL contest. The start date of the contest was March 01, 2016 and the end date was March 15, 2016.
--Write a query to print total number of unique hackers who made at least 1 submission each day (starting on the first day of the contest), and find the hacker_id and name of the hacker who made maximum number of submissions each day. If more than one such hacker has a maximum number of submissions, print the lowest hacker_id. The query should print this information for each day of the contest, sorted by the date.

--Input Format
--The following tables hold contest data:
--Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker.

--Column	Type
--hacker_id	Integer
--name	    String

--Submissions: The submission_date is the date of the submission, submission_id is the id of the submission, hacker_id is the id of the hacker who made the submission, and score is the score of the submission.

--Column	        Type
--hacker_id	        Integer
--submission_date	Integer
--score	            Integer
--submission_id	    Integer

SELECT s4.submission_date, b.num_in_comp, s4.hacker_id, h1.name
FROM Submissions s4

/* join the hackers table to access name field */
JOIN Hackers h1 ON h1.hacker_id = s4.hacker_id

/* join subquery to retrieve the number of hackers still in the competition
   in subquery select submission date and distinct hacker_ids */
JOIN (SELECT s2.submission_date, COUNT(DISTINCT s2.hacker_id) as num_in_comp
    FROM Submissions s2
      
    /* join subquery that tracks day_num of competition i.e. 1, 2, 3, ... */
    JOIN (SELECT s1.submission_date, DATEDIFF(s1.submission_date, '2016-03-01') + 1 AS day_num
        FROM Submissions s1
        GROUP BY s1.submission_date) a 
    ON a.submission_date = s2.submission_date
      
    /* only count hacker_id if hacker has made a submission on number of days = day_num */
    WHERE (
        SELECT COUNT(DISTINCT s3.submission_date)
        FROM Submissions s3
        WHERE DATEDIFF(s2.submission_date, s3.submission_date) >= 0
        GROUP BY s3.hacker_id
        HAVING s3.hacker_id = s2.hacker_id
    ) = a.day_num
      
    /* group by date to count number of hackers in competition on given day */
    GROUP BY submission_date
    ) b ON s4.submission_date = b.submission_date
    
/* only show hacker who made the most submissions on any given day */
WHERE s4.hacker_id = (
    SELECT s6.hacker_id
    FROM Submissions s6
    GROUP BY s6.submission_date, s6.hacker_id
    HAVING s6.submission_date = s4.submission_date
    ORDER BY COUNT(s6.hacker_id) DESC, s6.hacker_id ASC
    LIMIT 1
    )
/* final group by needed to eliminate dubplicate outputs */
GROUP BY s4.submission_date, b.num_in_comp, s4.hacker_id, h1.name;
