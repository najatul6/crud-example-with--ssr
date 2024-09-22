from pweb import PWebAppConfig


class Config(PWebAppConfig):
    APP_NAME = "Hello App"
    PORT: int = 1212
    
    CONNECT_MESSAGE: str = "Hello App is an Open Source Python based Web Framework for Rapid Development."
    DEVELOPED_BY: str = "Najatul islam engineer"
    DEVELOPED_BY_LINK: str = "https://najatul-islam.vercel.app"
    APP_VERSION: str = "v2.0.0"
    ENABLE_REGISTRATION: bool = True