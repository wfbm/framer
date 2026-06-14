import logging
from fastapi import Request, APIRouter

router = APIRouter(
  prefix = "/webhook",
  tags = ["waha", "webhook", "whatsapp"]
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/ping")
async def ping() -> str:
  return "pong"
