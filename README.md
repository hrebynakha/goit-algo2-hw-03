# goit-algo2-hw-03



### Description
Home work 3 for second algorithm course.

### Files

- `task1.py` - main script for task1, where we load data and draw graph, and calculate maximum flow
- `task2.py` - main script for task2, where we load data from csv and create two calases SimpleOOBTree and SimpleDict, and compare their performance
- `data/` - data files with connections between nodes, and positions of nodes (for task1) and items data (for task2)
- `helpers.py` - helper functions, like loading data from CSV and JSON files
- `graph.py` - graph module for drawing graph using networkx and matplotlib (for task1)
- `algorithms.py` - algorithms module for finding maximum flow (for task1)

## Task 1

#### How to run

```bash
python task1.py
```

#### Results


It output graph and maximum flow for each source and sink as table in console.

Final table for task 1 looks like:


|source|sink|max_flow|
|---|---|---|
|Термінал 1|Магазин 1|15|
|Термінал 1|Магазин 2|10|
|Термінал 1|Магазин 3|20|
|Термінал 1|Магазин 4|15|
|Термінал 1|Магазин 5|10|
|Термінал 1|Магазин 6|20|
|Термінал 1|Магазин 7|15|
|Термінал 1|Магазин 8|15|
|Термінал 1|Магазин 9|10|
|Термінал 1|Магазин 10|0|
|Термінал 1|Магазин 11|0|
|Термінал 1|Магазин 12|0|
|Термінал 1|Магазин 13|0|
|Термінал 1|Магазин 14|0|
|Термінал 2|Магазин 1|0|
|Термінал 2|Магазин 2|0|
|Термінал 2|Магазин 3|0|
|Термінал 2|Магазин 4|10|
|Термінал 2|Магазин 5|10|
|Термінал 2|Магазин 6|10|
|Термінал 2|Магазин 7|15|
|Термінал 2|Магазин 8|15|
|Термінал 2|Магазин 9|10|
|Термінал 2|Магазин 10|20|
|Термінал 2|Магазин 11|10|
|Термінал 2|Магазин 12|15|
|Термінал 2|Магазин 13|5|
|Термінал 2|Магазин 14|10|




#### Questions

1. Які термінали забезпечують найбільший потік товарів до магазинів?
> `Термінал 2` забезпечує найбільший потік товарів до магазинів(загалом охоплює 11 магазинів `4-14`), в свою чергу Термінал 1 відстає лише на 2 магазини та охоплює мереежу магазинів `1-9` при цьому загальний потік товарів на відповідні мережі магазинів рівний(**130**)

2. Які маршрути мають найменшу пропускну здатність і як це впливає на загальний потік?
> При потоці товарів з `Терміналу 2` через `Склад 2` пропускна здатність відчутно зменшується, це помітно на мережі магазинів `4-6`, які отримують меншу кількість товарів з даного терміналу (максимально **10**), використовуючи маршрут з `Терміналу 1` через `Склад 2` дані магазини отримують **15**,**10**,**20** товарів відповідно.

3. Які магазини отримали найменше товарів і чи можна збільшити їх постачання, збільшивши пропускну здатність певних маршрутів?
> `Магазин 13` отримав найменше товарів(5), але це обмеження обумовлене суто логістикою складу - магазин. Для збільшення постачання товарів до `магазину 13`, необхідно збільшити пропускну здатність маршруту зі `Складу 4` до `Магазину 13`
4. Чи є вузькі місця, які можна усунути для покращення ефективності логістичної мережі?
    
    
> Згідно отриманої таблиці, бачимо що Магазини `10-14` не можуть отримувати товари з `Терміналу 1`, а також в свою чергу Магазини `1-3`не можуть отримувати товарів з `Терміналу 2`. Тому, в разі проблеми чи виведення з ладу одного із терміналів, можна припустити що дані магазини не отримають товари. Для поліпшення ситуації, необхідно робити додаткові маршрути з `Терміналу 1` до `Складу 4` а також з `Терміналу 2` до `Складу 1` 

## Task 2

#### How to run

```bash
python task2.py
```

#### Results
Output for test 1 (range from **0** to **100**):
```
Total range_query time for OOBTree: 0.13662397899997814 seconds
Total range_query time for Dict: 0.5923984920000294 seconds
```

Output for test 2 (range from **123.45** to **223.45**):
```
Total range_query time for OOBTree: 0.2059548689999815 seconds
Total range_query time for Dict: 0.5674667820000536 seconds
```



#### Conclusions


OOBTree is faster than Dict because it can use serch price range, not iterating over all items. OOBTree save key as tuple (price, id) and use it to find items in tree faster.