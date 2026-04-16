from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests

BOT_TOKEN = "8513786315:AAFNkNtWxWhHoe9c-x_4PecU7nCu7lc73IE"
CHAT_ID = "6109809618"

URL = "https://www.cartier.com/ko-kr/주얼리/네크리스/다이아몬드-컬렉션/까르띠에-다무르-펜던트-스몰%28small%29-모델-브릴리언트-컷-다이아몬드-CRB7215800.html"

def send_telegram(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

print("🚀 Selenium 재고 감시 시작")

while True:
    try:
        driver.get(URL)
        time.sleep(5)

        html = driver.page_source

        if "쇼핑백에 추가하기" in html:
            send_telegram("🔥 재고 있음!!!\n" + URL)
            print("🔥 감지 성공")
            break

        elif "상담원 연결" in html:
            print("❌ 품절 상태")

        else:
            print("⚠️ 구조 확인 필요")

    except Exception as e:
        print("에러:", e)

    time.sleep(60)
