import requests
import time

BOT_TOKEN = "8513786315:AAFNkNtWxWhHoe9c-x_4PecU7nCu7lc73IE"
CHAT_ID = "6109809618"

URL = "https://www.cartier.com/ko-kr/주얼리/네크리스/다이아몬드-컬렉션/까르띠에-다무르-펜던트-스몰%28small%29-모델-브릴리언트-컷-다이아몬드-CRB7215800.html"

def send_telegram(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

print("🚀 시작")

while True:
    try:
        res = requests.get(URL, headers={
            "User-Agent": "Mozilla/5.0"
        })

        text = res.text

        if "쇼핑백에 추가하기" in text:
            send_telegram("🔥 재고 있음!")
            break
        else:
            print("❌ 없음")

    except Exception as e:
        print("에러:", e)

    time.sleep(3600)
