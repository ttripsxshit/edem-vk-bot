
import os

from dotenv import load_dotenv

load_dotenv()

VK_TOKEN = os.getenv("VK_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

if not VK_TOKEN:
    raise ValueError("VK_TOKEN не найден в .env")

if not ADMIN_ID:
    raise ValueError("ADMIN_ID не найден в .env")

ADMIN_ID = int(ADMIN_ID)
