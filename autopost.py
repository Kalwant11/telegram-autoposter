import time
import telegram

# Telegram Bot Token और चैनल username
BOT_TOKEN = '7019280866:AAGBq5ODM9eyW4aPhTXwE7e0Z1vB_XfaQFc'
CHANNEL_USERNAME = '@sapnalottery'

bot = telegram.Bot(token=BOT_TOKEN)

# पोस्ट्स की लिस्ट - लूप के लिए
posts = [
    {"type": "text", "content": "🙏 नमस्कार! यह Auto Post है जो हर 15 मिनट में आता है।"},
    {"type": "video", "content": "video1.mp4"},
    {"type": "video", "content": "video2.mp4"},
    {"type": "video", "content": "video3.mp4"},
    {"type": "document", "content": "appfile.apk"}
]

while True:
    for item in posts:
        try:
            if item["type"] == "text":
                bot.send_message(chat_id=CHANNEL_USERNAME, text=item["content"])
            elif item["type"] == "video":
                bot.send_video(chat_id=CHANNEL_USERNAME, video=open(item["content"], 'rb'))
            elif item["type"] == "document":
                bot.send_document(chat_id=CHANNEL_USERNAME, document=open(item["content'], 'rb'))
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print(f"✅ Posted: {item['type']} - Waiting 15 mins...")
        time.sleep(15 * 60)  # 15 minutes
