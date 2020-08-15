from line_notify import send_text
from web_scraping import get_gold_price

gold_price = get_gold_price()
updating_time = gold_price['updating_time']
BLSell = gold_price['BLSell']
BLBuy = gold_price['BLBuy']
OMSell = gold_price['OMSell']
OMBuy = gold_price['OMBuy']
line_text = "ล่าสุด {}\nทองคำแท่ง \nขายออก: {} บาท\nรับซื้อ: {} บาท \nทองรูปพรรณ\nขายออก: {} บาท\nรับซื้อ: {} บาท".format(updating_time, BLSell, BLBuy, OMSell, OMBuy)

token = "your line token"
send_text(token, line_text)