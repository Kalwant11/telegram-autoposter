import os
import time
import telegram

BOT_TOKEN = '7019280866:AAGBq5ODM9eyW4aPhTXwE7e0Z1vB_XfaQFc'
CHANNEL_USERNAME = '@sapnalottery'
bot = telegram.Bot(token=BOT_TOKEN)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# पोस्ट्स की लिस्ट
posts = [
    {"type": "text", "content": "🙏 नमस्कार! यह Auto Post है जो हर 15 मिनट में आता है।"},
    {"type": "video", "content": os.path.join(BASE_DIR, "video1.mp4")},
    {"type": "video", "content": os.path.join(BASE_DIR, "video2.mp4")},
    {"type": "video", "content": os.path.join(BASE_DIR, "video3.mp4")},
    {"type": "document", "content": os.path.join(BASE_DIR, "appfile.apk")},
]

while True:
    for item in posts:
        try:
            if item["type"] == "text":
                bot.send_message(chat_id=CHANNEL_USERNAME, text=item["content"])
            elif item["type"] == "video":
                with open(item["content"], 'rb') as vid:
                    bot.send_video(chat_id=CHANNEL_USERNAME, video=vid)
            elif item["type"] == "document":
                with open(item["content"], 'rb') as doc:
                    bot.send_document(chat_id=CHANNEL_USERNAME, document=doc)

            print(f"✅ Posted: {item['type']} - Waiting 15 mins...")
        except Exception as e:
            print(f"❌ Error: {e}")

        time.sleep(15 * 60)
