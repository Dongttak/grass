select p.member_name, r.REVIEW_TEXT, date_format(r.REVIEW_DATE, "%Y-%m-%d") as review_date from member_profile p
join rest_review r on p.member_id=r.member_id where p.member_id in(
    select member_id from REST_REVIEW group by member_id having count(*)=(
        select max(cnt) from
        (
            select count(*) as cnt from rest_review group by member_id
        ) cnt
    ))
order by r.review_date, r.REVIEW_DATE
