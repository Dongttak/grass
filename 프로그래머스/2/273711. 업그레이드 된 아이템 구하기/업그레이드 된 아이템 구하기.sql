select item_id, item_name, rarity
from item_info
where item_id in (
    select item_id
    from item_tree
    where parent_item_id in 
        (
            SELECT ITEM_ID 
            FROM ITEM_INFO 
            WHERE RARITY = 'RARE'
        ) 
)
order by item_id desc