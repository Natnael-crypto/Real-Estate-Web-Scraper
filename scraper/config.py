import os
from dotenv import load_dotenv

load_dotenv()

CUSTOM_USER_AGENT = os.getenv("CUSTOM_USER_AGENT")
BROWSERS = ["chromium", "firefox", "webkit"]
