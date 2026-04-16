import requests
import time
import random

BOT_TOKEN = "8513786315:AAFNkNtWxWhHoe9c-x_4PecU7nCu7lc73IE"
CHAT_ID = "6109809618"

URL = "https://www.cartier.com/ko-kr/주얼리/네크리스/다이아몬드-컬렉션/까르띠에-다무르-펜던트-스몰%28small%29-모델-브릴리언트-컷-다이아몬드-CRB7215800.html"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8"
}

def send_telegram(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

print("🚀 Cartier 재고 감시 시작 (안정 버전)")

def check_stock(text):
    text_lower = text.lower()

    # ❌ 확실한 품절 신호들
    out_signals = [
        "outofstock",
        "soldout",
        "unavailable"
    ]

    for signal in out_signals:
        if signal in text_lower:
            return False

    # ✅ 재고 있음 신호 (가격 + 구매 관련 구조)
    if '"price"' in text_lower and '"product"' in text_lower:
        return True

    return None  # 판단 불가

while True:
    try:
        res = requests.get(URL, headers=headers, timeout=10)
        text = res.text

        result = check_stock(text)

        if result is True:
            send_telegram("🔥 재고 있음!!! 지금 바로 확인!!!\n" + URL)
            print("🔥 감지 성공")
            break

        elif result is False:
            print("❌ 품절 상태 유지")

        else:
            print("⚠️ 판단 불가 (구조 변화 가능)")

    except Exception as e:
        print("에러:", e)

    time.sleep(300 + random.randint(121, 234))
