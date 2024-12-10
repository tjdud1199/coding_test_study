SELECT SUM(G.SCORE) AS SCORE, G.EMP_NO AS EMP_NO, E.EMP_NAME AS EMP_NAME, E.POSITION AS POSITION, E.EMAIL AS EMAIL
FROM HR_GRADE AS G
JOIN HR_EMPLOYEES AS E
ON G.EMP_NO = E.EMP_NO
GROUP BY EMP_NO
HAVING MAX(SCORE)
ORDER BY SCORE DESC
LIMIT 1;