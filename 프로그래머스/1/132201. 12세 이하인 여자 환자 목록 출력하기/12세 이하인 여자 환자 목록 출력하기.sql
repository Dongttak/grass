select pt_name, pt_no, gend_cd, age, IFNULL(TLNO, 'NONE') as TLNO from patient where gend_cd='W' and AGE<=12
order by age desc, pt_name;