from bs4 import BeautifulSoup as bs
import requests

def get_gold_price():
    url = "https://www.goldtraders.or.th/default.aspx"
    r = requests.get(url)
    c = r.content
    soup = bs(c,"html.parser")
    goldPrice = soup.find_all("td",{"style":"text-align:right;vertical-align:middle;"})
    updating_time = soup.find("span",{"id":"DetailPlace_uc_goldprices1_lblAsTime"})
    BLSell = soup.find("span",{"id":"DetailPlace_uc_goldprices1_lblBLSell"})
    BLBuy = soup.find("span",{"id":"DetailPlace_uc_goldprices1_lblBLBuy"})
    OMSell = soup.find("span",{"id":"DetailPlace_uc_goldprices1_lblOMSell"})
    OMBuy = soup.find("span",{"id":"DetailPlace_uc_goldprices1_lblOMBuy"})
    goldPrice_dict = {}
    goldPrice_dict['updating_time'] = updating_time.text.replace(" เวลา", "").split(" น.")[0]
    BLSell_price = BLSell.text.strip()
    BLBuy_price = BLBuy.text.strip()
    OMSell_price = OMSell.text.strip()
    OMBuy_price = OMBuy.text.strip()
    goldPrice_dict['BLSell'] = float(BLSell_price.replace(",", ""))
    goldPrice_dict['BLBuy'] = float(BLBuy_price.replace(",", ""))
    goldPrice_dict['OMSell'] = float(OMSell_price.replace(",", ""))
    goldPrice_dict['OMBuy'] = float(OMBuy_price.replace(",", ""))
    return goldPrice_dict

if __name__ == '__main__':
    gold_price = get_gold_price()
    print(gold_price)