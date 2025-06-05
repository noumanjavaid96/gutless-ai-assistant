# src/bot.py
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.event("app_mention")
def handle_app_mention_events(body, say, logger):
    logger.info(body)
    user_query = body["event"]["text"].split('>', 1)[-1].strip() # Extract query after mention
    # TODO: Integrate with core_logic.py to get an answer
    # For now, just acknowledge
    response_text = f"Received your query: '{user_query}'. I'm working on it!"
    say(response_text)

@app.event("message")
def handle_message_events(body, logger):
    # This will capture all messages, including DMs and mentions if not handled by app_mention
    # For DMs, you might want specific logic
    # logger.info(body)
    pass

# Start your app
if __name__ == "__main__":
    # Ensure SLACK_APP_TOKEN is set for Socket Mode
    if not os.environ.get("SLACK_APP_TOKEN"):
        print("Error: SLACK_APP_TOKEN environment variable not set for Socket Mode.")
    else:
        print("Starting Gutless AI Assistant in Socket Mode...")
        SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
