# Market Concentration (HI2)
Индекс рыночной концентрации
 

```
Акции    - https://iss.moex.com/iss/datashop/algopack/eq/hi2/
Фьючерсы - https://iss.moex.com/iss/datashop/algopack/fo/hi2/
Валюта   - https://iss.moex.com/iss/datashop/algopack/fx/hi2/
```

| Field        | Type         | Description                                  | Example value       |
|--------------|--------------|----------------------------------------------|---------------------|
| tradedate    | date:10      | Дата                                         | 2024-04-11          |
| tradetime    | time:10      | Время, на которое актуальны данные           | 18:40:00            |
| secid        | string:51    | Идентификатор инструмента                    | SBER                |
| metric       | string:96    | Метрика                                      | hhi_aggressive      |
| value        | double       | Значение метрики                             | 233                 |
| reference    | string:765   | Дополнительные справочные данные             | null                |
| SYSTIME      | datetime:19  | Время загрузки данных                        | 2024-04-11 18:45:35 |
