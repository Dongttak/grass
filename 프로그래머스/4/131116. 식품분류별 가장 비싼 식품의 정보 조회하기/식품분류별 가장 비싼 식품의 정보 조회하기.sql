select category, price as max_price, product_name
from food_product p1
WHERE (CATEGORY, PRICE) IN (
                            SELECT CATEGORY, MAX(PRICE)
                            FROM FOOD_PRODUCT
                            GROUP BY CATEGORY
                            HAVING CATEGORY IN ('국', '김치', '식용유', '과자')
)
ORDER BY MAX_PRICE DESC