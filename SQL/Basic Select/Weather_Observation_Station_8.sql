SELECT DISTINCT CITY FROM STATION WHERE REGEXP_LIKE(LOWER(CITY), '^[aeiou]') and  REGEXP_LIKE(LOWER(CITY), '[aeiou]$');