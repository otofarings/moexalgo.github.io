# Welcome to ALGOPACK
Самый богатый набор online и исторических данных Московской Биржи через API

## Состав данных

<table>
  <tr>
    <th></th>
	<th></th>
    <th>Обновление</th>
    <th>История</th>
    <th>Python lib</th>
  </tr>
  <tr>
    <td>
      <span><b><a href="modules/realtime">Real-time market data</a></b></span></br>
      Свечи, стаканы и сделки
    </td>
    <td>
      акции</br>
	  фьючерсы
    </td>
    <td>10 сек</td>
    <td>-</td>
    <td>+</td>
  </tr>
  <tr>
    <td>
      <span><b><a href="modules/supercandles">Super Candles</a></b></span></br>
      50+ фич на потоке сделок, заявок и стакана котировок
    </td>
	<td>
      акции</br>
	  фьючерсы</br>
	  валюта
    </td>
    <td>5 мин</td>
    <td>c 2020 года</td>
    <td>+</td>
  </tr>
  <tr>
    <td>
      <span><b><a href="modules/futoi">Futures Open Interest (FUTOI)</a></b></span></br>
      Открытые позиции по фьючерсным контрактам в разрезе физ. и юр. лиц
    </td>
	<td>
      фьючерсы
    </td>
    <td>5 мин</td>
    <td>c 2020 года</td>
    <td>+</td>
  </tr>
  <tr>
    <td>
      <span><b><a href="modules/hi2">Market Concentration (HI2)</a></b></span></br>
      Индекс рыночной концентрации
    </td>
	<td>
      акции</br>
	  фьючерсы</br>
	  валюта
    </td>
    <td>Ежедневно, 19:00</td>
    <td>c 2020 года</td>
    <td>+</td>
  </tr>
  <tr>
    <td>
      <span><b><a href="modules/megaalerts">Mega Alerts</a></b></span></br>
      Сигналы о существенных отклонениях (аномалиях)
    </td>
	<td>
      акции</br>
	  фьючерсы</br>
	  валюта
    </td>
    <td>1 мин</td>
    <td>c 2024 года</td>
    <td>-</td>
  </tr>
  
  <!-- More rows follow -->
</table>




## С ALGOPACK вы сможете:
* Загружать исторические данные для тестирования торговых стратегий
* Получать online данные для алгоритмической торговли

> *Через ALGOPACK нельзя отправлять заявки на биржу.
Заявки отправляются через торговый API вашего брокера*


## Начать пользоваться

Зарегистрируйтесь на сайте moex.com

[:octicons-sign-in-16: Зарегистрироваться](https://www.moex.com/){ .md-button .md-button--primary }

и ALGOPACK готов к использованию: [Смотреть методы API](api.md)
