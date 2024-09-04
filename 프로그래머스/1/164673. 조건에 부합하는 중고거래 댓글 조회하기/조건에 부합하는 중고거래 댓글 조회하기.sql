-- 코드를 입력하세요
SELECT title, b.board_id as board_id, reply_id, r.writer_id as writer_id, r.contents as contents, date_format(r.created_date, '%Y-%m-%d') as created_date
from used_goods_board b, used_goods_reply r
where b.board_id = r.board_id
and year(b.created_date) = 2022 and month(b.created_date) = 10
order by r.created_date, title;