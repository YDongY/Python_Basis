--视图
    select gs.*, gc.name as cate_name,gb.name as brand_name from goods as gs
    left join goods_cates as gc on gs.cate_id=gc.id
    left join goods_brands as gb on gs.brand_id=gb.id;


--创建视图
    create view v_goods_info as
    select gs.*, gc.name as cate_name,gb.name as brand_name from goods as gs
    left join goods_cates as gc on gs.cate_id=gc.id
    left join goods_brands as gb on gs.brand_id=gb.id;