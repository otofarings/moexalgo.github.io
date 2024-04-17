# Кастомизация запросов к API

## Формат данных
Данные можно получать в **json**, **csv** и **xml** форматах

```
# json
https://iss.moex.com/iss/engines/stock/markets/shares/boards/tqbr/securities.json

# csv
https://iss.moex.com/iss/engines/stock/markets/shares/boards/tqbr/securities.csv

# xml
https://iss.moex.com/iss/engines/stock/markets/shares/boards/tqbr/securities.xml
```


## Meta данные
Можно включить/отключить получение метаданных (тип и размер данных)

> *iss.meta=on|off*

```
# Включить метаданные
https://iss.moex.com/iss/engines/stock/markets/shares/boards/tqbr/securities.json?
iss.meta=on

# Отключить метаданные
https://iss.moex.com/iss/engines/stock/markets/shares/boards/tqbr/securities.json?
iss.meta=off
```

## Блоки данных
Ответ может сождержать несколько блоков данных. Чтобы выбрать конкретный блок данных, нужно использовать

> *iss.only=&lt;data_block&gt;*

```
# Блок данных securiries - справочник инструментов
https://iss.moex.com/iss/engines/stock/markets/shares/boards/tqbr/securities.json?
iss.only=securities

# Блок данных marketdata - торговая статистика
https://iss.moex.com/iss/engines/stock/markets/shares/boards/tqbr/securities.json?
iss.only=marketdata
```

## Наборы полей
По умолчанию, данные приходят со всеми полями. Если нужно только несколько полей, то в запросе можно указать список необходимых полей

> *&lt;data_block&gt;.columns=&lt;column1&gt;,&lt;column2&gt;,&lt;column3&gt;*

```
# Получить несколько конкретных полей
https://iss.moex.com/iss/engines/stock/markets/shares/boards/tqbr/securities.json?
iss.only=marketdata&
marketdata.columns=SECID,LAST,LASTCHANGEPRCNT
```

## Курсор
Количество возвращаемых данных в запросе может быть ограничена лимитом, например 100 или 500 строк. Чтобы получить все данные, предусмотрен курсор 

> *start=&lt;number&gt;*

```
# Получить данные с 1000-ой строки
https://iss.moex.com/iss/datashop/algopack/eq/tradestats.json?
date=2024-04-15&
start=1000
```
