--Samantha interviews many candidates from different colleges using coding challenges and contests. Write a query to print the contest_id, hacker_id, name, and the sums of total_submissions, total_accepted_submissions, total_views, and total_unique_views for each contest sorted by contest_id. Exclude the contest from the result if all four sums are .
--Note: A specific contest can be used to screen candidates at more than one college, but each college only holds  screening contest.

--Input Format
--The following tables hold interview data:
--Contests: The contest_id is the id of the contest, hacker_id is the id of the hacker who created the contest, and name is the name of the hacker.

--Column	  Type
--hacker_id	  Integer
--name	      String
--contest_id  Integer

--Colleges: The college_id is the id of the college, and contest_id is the id of the contest that Samantha used to screen the candidates.

--Column	    Type
--contest_id	Integer
--college_id	Integer

--Challenges: The challenge_id is the id of the challenge that belongs to one of the contests whose contest_id Samantha forgot, and college_id is the id of the college where the challenge was given to candidates.

--Column	    Type
--challenge_id	Integer
--college_id	Integer

--View_Stats: The challenge_id is the id of the challenge, total_views is the number of times the challenge was viewed by candidates, and total_unique_views is the number of times the challenge was viewed by unique candidates.

--Column	          Type
--challenge_id	      Integer
--total_views	      Integer
--total_unique_views  Integer

--Submission_Stats: The challenge_id is the id of the challenge, total_submissions is the number of submissions for the challenge, and total_accepted_submission is the number of submissions that achieved full scores.

--Column	                  Type
--challenge_id	              Integer
--total_submissions	          Integer
--total_accepted_submissions  Integer

SELECT A.contest_id, A.hacker_id, A.Name, 
        ifnull(SUM(total_submissions),0) As total_submissions, 
        ifnull(SUM(total_accepted_submissions),0) AS total_accepted_submissions,
        ifnull(SUM(total_views),0) AS total_views,
        ifnull(SUM(total_unique_views),0) AS total_unique_views
FROM Contests AS A

LEFT JOIN Colleges AS B
    ON A.contest_id = B.contest_id 

LEFT JOIN Challenges AS C
    ON B.college_id = C.college_id 

LEFT JOIN (SELECT challenge_id, SUM(total_views) AS total_views, 
                  SUM(total_unique_views) AS total_unique_views
           FROM View_Stats
           GROUP BY challenge_id) AS D 
    ON C.challenge_id = D.challenge_id 
    
LEFT JOIN (SELECT challenge_id, SUM(total_submissions) AS total_submissions, 
                  SUM(total_accepted_submissions) AS total_accepted_submissions
           FROM Submission_Stats
           GROUP BY challenge_id) AS E
    ON C.challenge_id = E.challenge_id 
    
GROUP BY A.contest_id, A.hacker_id, A.Name
HAVING (total_submissions + total_accepted_submissions + total_views + total_unique_views) > 0

ORDER BY A.contest_id
;



