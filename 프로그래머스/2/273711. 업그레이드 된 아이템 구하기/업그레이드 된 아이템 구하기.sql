SELECT it.ITEM_ID, ii.ITEM_NAME, ii.RARITY
FROM ITEM_TREE AS it
JOIN ITEM_INFO AS ii
ON
it.ITEM_ID = ii.ITEM_ID
WHERE it.PARENT_ITEM_ID IN (SELECT ii.ITEM_ID FROM ITEM_INFO AS ii WHERE ii.RARITY = 'RARE')
ORDER BY 1 DESC;