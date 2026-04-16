import requests
import time

BOT_TOKEN = "8513786315:AAFNkNtWxWhHoe9c-x_4PecU7nCu7lc73IE"
CHAT_ID = "6109809618"

URL = "https://www.cartier.com/ko-kr/주얼리/네크리스/다이아몬드-컬렉션/까르띠에-다무르-펜던트-스몰%28small%29-모델-브릴리언트-컷-다이아몬드-CRB7215800.html"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def send_telegram(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

print("🚀 재고 모니터링 시작")

while True:
    try:
        res = requests.get(URL, headers=headers)
        text = res.text

        if "InStock" in text:
            send_telegram("🔥 재고 있음! 바로 구매 가능!\n" + URL)
            break
        elif "OutOfStock" in text:
            print("❌ 품절 상태 유지")
        else:
            print("⚠️ 상태 확인 필요 (패턴 없음)")

    except Exception as e:
        print("에러:", e)

    time.sleep(60)
