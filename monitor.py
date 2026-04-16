import requests
import time
import random

BOT_TOKEN = "8513786315:AAFNkNtWxWhHoe9c-x_4PecU7nCu7lc73IE"
CHAT_ID = "6109809618"

URL = "https://www.cartier.com/ko-kr/주얼리/네크리스/다이아몬드-컬렉션/까르띠에-다무르-펜던트-스몰%28small%29-모델-브릴리언트-컷-다이아몬드-CRB7215800.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}

def send_telegram(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

print("🚀 1분 단위 재고 감시 시작")

while True:
    try:
        res = requests.get(URL, headers=headers, timeout=10)
        text = res.text
    
        if "재입고알림 신청하기" in text or "상담원 연결" in text:
            print("❌ 품절 상태 유지")
        else:
            send_telegram("🔥 재고 있음!!!\n" + URL)
            print("🔥 감지 성공")
            break
        
    except Exception as e:
        print("에러:", e)

    time.sleep(300 + random.randint(100, 200))
