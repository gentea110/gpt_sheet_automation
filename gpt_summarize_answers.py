import gspread
from google.oauth2.service_account import Credentials
from openai import OpenAI
import time

# OpenAI APIキー
client = OpenAI(api_key="your-api-key-here")

# Google Sheets API認証
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("your-service-account.json", scopes=scope)
gc = gspread.authorize(creds)

# スプレッドシートの操作
spreadsheet = gc.open_by_url("spreadssheets-url-here")
sheet =spreadsheet.worksheet("回答結果")

#回答列の同じ行数分データ取得
answers = sheet.col_values(3)

#ヘッダーを追加(なければ)
header = sheet.row_values(1)
if len(header) < 4 :
    sheet.update(range_name="D1",values=[["summary"]])

#回答を要約して　D列に記入
for i, answer in enumerate(answers[1:], start=2): #2行目から処理
    if not answer or "エラー" in answer:
        continue # 空やエラーはスキップ
    
    prompt = f"次の文章を簡潔に1文で要約してください:{answer}"
    print(f"{i}行目要約中:{prompt}")

    try:
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages=[{"role": "user","content":prompt}]
        )
        summary = response.choices[0].message.content.strip()
        sheet.update(range_name=f"D{i}",values=[[summary]])

    except Exception as e:
        print(f"{i}行目で要約エラー: {e}")
    
    time.sleep(1)
