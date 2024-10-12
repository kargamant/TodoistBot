from fastapi import APIRouter
from .todoist_oauth import OAuthController

router = APIRouter()

router.include_router(OAuthController.create_router())
