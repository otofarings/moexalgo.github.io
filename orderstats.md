# ORDER STATS

* ### put_orders, cancel_orders
Количество поставленных сделок

* ### put_orders_b, put_orders_s
Количество заявок на покупку/продажу, поставленных в стакан

* ### cancel_orders_b, cancel_orders_s
Количество снятых заявок на покупку/продажу

## vol

* ### put_vol, cancel_vol
Объем заявок, поставленных/снятых в стакан

* ### put_vol_b, put_vol_s
Объем заявок на покупку/продажу, поставленных в стакан

* ### cancel_vol_b, cancel_vol_s
Объем снятых заявок на покупку/продажу

### Пример
![image](https://github.com/kde2podfreebsd/MOEX-ALGOPACK-DOCS/assets/39852259/276a0edf-f87f-4d71-bf7e-67dfb4e28d09)

## val
* ### put_val, cancel_val
Объем заявок, поставленных/снятых в стакан (₽)
```
put_val = put_val_b + put_val_s
```
```
cancel_val = cancel_val_b + cancel_val_s
```

* ### put_val_b, put_val_s
Объем заявок на покупку/продажу, поставленных в стакан (₽)

* ### cancel_val_b, cancel_val_s
Объем снятых заявок на покупку/продажу выраженный в рублях

### Пример
![image](https://github.com/kde2podfreebsd/MOEX-ALGOPACK-DOCS/assets/39852259/1d8f607b-dc2a-4ce4-9335-9a9db8ecdfcb)

## vwap
### Средневзвешенная цена — это средняя цена заявок, весом которых является объем заявок

### Пример расчета: 
Было выставлено 3 заявки
![image](https://github.com/kde2podfreebsd/MOEX-ALGOPACK-DOCS/assets/39852259/4158e585-ced7-4659-b39e-9ba3e1c5cd72)

* ### put_vwap_b, put_vwap_s, cancel_vwap_b, cancel_vwap_s
**Средневзвешенная цена выставленных/отмененных заявок на покупку и продажу**, соответственно — это средняя цена заявки покупки или продажи, весом которых является объем соответствующих сделок.
```
put_vwap_b = put_val_b / put_vol_b
```

### Пример:

Есть 2 сделки на покупку: 100 акций по 10 рублей и 200 акций по 20 рублей, тогда:
```
put_vwap_b = (100*10 + 200*20) / (100 + 200) = 16.67 ₽
```
