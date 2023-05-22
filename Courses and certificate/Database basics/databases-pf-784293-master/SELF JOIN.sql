/* This following query retrieve data by displaying which customers share the same city */
SELECT A.FirstName AS CustomerA, B.FirstName AS CustomerB, A.City
FROM customers A, customers B
WHERE A.CustomerID <> B.CustomerID 
AND A.City = B.City
ORDER BY A.FirstName
 