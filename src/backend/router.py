from fastapi import APIRouter
from src.backend.oauth.todoist_oauth import OAuthController

router = APIRouter()

router.include_router(OAuthController.create_router())
