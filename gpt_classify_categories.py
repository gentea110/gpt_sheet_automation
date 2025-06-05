import gspread
from google.oauth2.service_account import Credentials
import time

# Google Sheets API 認証
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("your-service-account.json", scopes=scope)
gc = gspread.authorize(creds)

# スプレッドシートとシートの読み込み
spreadsheet = gc.open_by_url("spreadssheets-url-here")
sheet = spreadsheet.worksheet("回答結果")

#　カテゴリ判定ルール
category_rules = {
     "ファッション・生活用品": ["バッグ", "収納", "ネックレス", "長靴", "鏡", "持ち運び"],
    "ヘルスケア・家電": ["電動歯ブラシ", "清潔", "効率", "健康", "ケア"],
    "科学・テクノロジー": ["ロケット", "宇宙", "科学", "推進", "探査"],
    "食品・飲料": ["バナナ", "果物", "栄養", "エネルギー", "食べる"],
    "その他": []
}

#ヘッダー追加(F列)
header = sheet.row_values(1)
if len(header) < 6:
    sheet.update(range_name="F1",values=[["category"]])

keywords_list = sheet.col_values(5)

#自動分類実行
for i, keywords in enumerate(keywords_list[1:],start=2):
    found = False
    for category, words in category_rules.items():
        if any(word in keywords for word in words):
            sheet.update(f"F{i}",[[category]])
            found = True
            break
    if not found :
        sheet.update(f"F{i}",[["その他"]])
    
    time.sleep(1)