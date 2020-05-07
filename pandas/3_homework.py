# kospi 체결가를 page별로 받아서 line chart 그리기
# https://finance.naver.com/sise/sise_index_day.nhn?code=KOSPI&page=1

from bs4 import BeautifulSoup
import requests as req
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

code = "KOSPI"

def get_data(page_num):
    uri = "https://finance.naver.com/sise/sise_index_day.nhn?code={}&page={}".format(code, page_num)
    response = req.get(uri)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # tr_tag = soup.find_all("tr")
        date_data = soup.find_all("td", class_ = "date")
        date_array = [date.get_text(strip = True) for date in date_data]
        number1_data = soup.find_all("td", class_ = "number_1")
        number1_array = [number1.get_text(strip = True) for number1 in number1_data]

        np_date_array = np.array(date_array)
        np_number1_array = np.array(number1_array).reshape(6, 4)
        data = pd.DataFrame(np_number1_array, columns = ["1", "2", "3", "4"], index = np_date_array)
        data["1"] = [float(item1.replace(",", "")) for item1 in data["1"]]
        data["3"] = [float(item1.replace(",", "")) for item1 in data["3"]]
        return data
    else:
        raise Exception('error')
        
def get_all_pages(page):
    result_pd = None
    for page in range(1, 3):
        res = get_data(page)
        if result_pd is None: result_pd = res
        else: result_pd = result_pd.append(res)
    return result_pd

data = get_all_pages(3)
data.sort_index(inplace=True)

plt.subplot(211)
plt.plot(data.index, data["1"])
plt.xticks(rotation=30)
plt.title("price")
plt.grid()

plt.subplot(212)
plt.bar(data.index, data["3"])
plt.xticks(rotation=30)
plt.title("mount")
plt.grid()

plt.show()




