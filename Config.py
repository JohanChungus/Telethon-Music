import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "20154826"))
    API_HASH = os.environ.get("API_HASH", "42caa36ee14786314595514aade305ac")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5901294437:AAHIWcn7GYfAZ5FOkEpZ6wCycDBNsi2XPA0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzUBu3_-mTib_e7i75VgJOUjTEUewDGnlciYss9AZ23qMmqdZy1-FkkV0o_S6sdA57Pfu9tl4qTXmu_FN5bTopqwfASNVLNHg2t36l-O7j5asZECl2UqfyhHx0hurrHkMQ7UbHr2dzbxSXkyWDKkdfNNak-nXDaaolEOkWLMCaXTBn8rM-mlfPwafmoE9QJiDaa2zMOHE5dm4_V_9757rYBo9pLZNIsrvv33GSkLDQoUnTfyBm2U45-TLdFpdPx9_2zZNhwL830rggfGmFY8v9jDwFqaw8xFTrAkuo7YkPXjJHBb83buePWBQzf-yhXXnOkRn3JA1vpyWemlaWpsBjTZS5Y=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Musikqp1e7_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5722335529")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
