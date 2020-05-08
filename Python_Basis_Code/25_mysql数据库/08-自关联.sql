-- 查询出湖北省有哪些市
+--------+--------+------+--------+----------------------+--------+
| aid    | atitle | pid  | aid    | atitle               | pid    |
+--------+--------+------+--------+----------------------+--------+
| 420000 | 湖北省 | NULL | 420100 | 武汉市               | 420000 |
| 420000 | 湖北省 | NULL | 420200 | 黄石市               | 420000 |
| 420000 | 湖北省 | NULL | 420300 | 十堰市               | 420000 |
| 420000 | 湖北省 | NULL | 420500 | 宜昌市               | 420000 |
| 420000 | 湖北省 | NULL | 420600 | 襄阳市               | 420000 |
| 420000 | 湖北省 | NULL | 420700 | 鄂州市               | 420000 |
| 420000 | 湖北省 | NULL | 420800 | 荆门市               | 420000 |
| 420000 | 湖北省 | NULL | 420900 | 孝感市               | 420000 |
| 420000 | 湖北省 | NULL | 421000 | 荆州市               | 420000 |
| 420000 | 湖北省 | NULL | 421100 | 黄冈市               | 420000 |
| 420000 | 湖北省 | NULL | 421200 | 咸宁市               | 420000 |
| 420000 | 湖北省 | NULL | 421300 | 随州市               | 420000 |
| 420000 | 湖北省 | NULL | 422800 | 恩施土家族苗族自治州 | 420000 |
| 420000 | 湖北省 | NULL | 429000 | 省直辖行政单位       | 420000 |
+--------+--------+------+--------+----------------------+--------+
select * from areas as province inner join areas as city
              on city.pid=province.aid having province.atitle="湖北省";

select province.atitle,city.atitle from areas as province inner join areas as city
              on city.pid=province.aid having province.atitle="湖北省";


-- 查询襄阳市有哪些县城
+--------+----------+
| atitle | atitle   |
+--------+----------+
| 襄阳市 | 襄城区   |
| 襄阳市 | 樊城区   |
| 襄阳市 | 襄州区   |
| 襄阳市 | 南漳县   |
| 襄阳市 | 谷城县   |
| 襄阳市 | 保康县   |
| 襄阳市 | 老河口市 |
| 襄阳市 | 枣阳市   |
| 襄阳市 | 宜城市   |
+--------+----------+
select province.atitle,city.atitle from areas as province inner join areas as city
              on city.pid=province.aid having province.atitle="襄阳市";