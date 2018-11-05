use test
set names utf8;

-- 1. Выбрать все товары (все поля)
SELECT * FROM product

-- 2. Выбрать названия всех автоматизированных складов
SELECT store.name FROM store WHERE is_automated

-- 3. Посчитать общую сумму в деньгах всех продаж
SELECT SUM(total) FROM sale total

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
SELECT DISTINCT store_id FROM sale

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
SELECT DISTINCT store_id FROM store WHERE store_id NOT IN (SELECT DISTINCT store_id FROM sale)

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
SELECT p.name, avg(s.total/s.quantity) from sale as s left join product as p ON s.product_id = p.product_id GROUP BY p.name ORDER BY avg(s.total/s.quantity)

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
SELECT p.name from sale as s left join product as p ON s.product_id = p.product_id group by s.product_id having count(distinct s.store_id) = 1

-- 8. Получить названия всех складов, с которых продавался только один продукт
select store.name from sale as sale left join store as store on sale.store_id = store.store_id group by sale.store_id having count(distinct sale.product_id) = 1

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select * from sale where total = (select max(sale.total) from sale as sale)

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select date from sale group by date order by sum(total) desc, date asc limit 1
