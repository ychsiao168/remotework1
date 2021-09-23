import requests
import json
from bs4 import BeautifulSoup

class AaplHistory:
  '''
  curr_id: 6408
  smlID: 1159963
  header: AAPL历史数据
  st_date: 2021/08/01
  end_date: 2021/08/02
  interval_sec: Daily
  sort_col: date
  sort_ord: DESC
  action: historical_data
  '''
  _API_URL = 'https://cn.investing.com/instruments/HistoricalDataAjax'

  def __init__(self, dateStart, dateEnd):
    self.dateStart = dateStart
    self.dateEnd = dateEnd

  def _html_to_json_arr(self, html):
    col_index = 0
    json_arr = []
    col_string= ['Date', 'Price', 'Open', 'High', 'Low', 'Vol.', 'Change%',]

    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('table')[0]
    for row in table.find_all('tr'):
      col_index = 0
      one_day_data = {}
      columns = row.find_all('td')
      for column in columns:
        one_day_data[col_string[col_index]] = column.get_text()
        col_index += 1
        #print(column.get_text())

      if(len(one_day_data) > 0) :
        json_arr.append(json.dumps(one_day_data))

    return json_arr

  def get_json(self):
    r = requests.post('https://cn.investing.com/instruments/HistoricalDataAjax',
        data = {
            'curr_id': '6408',
            'smlID': '1159963',
            'header': 'AAPL历史数据',
            'st_date': self.dateStart,
            'end_date': self.dateEnd,
            'interval_sec': "Daily",
            'sort_col': 'date',
            'sort_ord': 'DESC',
            'action': 'historical_data',
        },
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
            'X-Requested-With': 'XMLHttpRequest',
        },
    )

    if r.status_code == 200:
      return self._html_to_json_arr(r.text)
    else:
      return []

if __name__ == '__main__':
  # test code
  apple = AaplHistory('2021/08/05', '2021/08/09')
  json_arr = apple.get_json()
  print(f'json_arr={json_arr}')
