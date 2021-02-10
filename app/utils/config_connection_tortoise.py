import ssl
from app.utils.settings import Settings
from app.utils.logger import logger


def config_connection_tortoise():
    settings = Settings()

    if settings.ENVIRONMENT == "PROD":
        logger.info("Using POSTGRES PROD database")
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        return {
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "database": settings.DATABASE_NAME,
                        "host": settings.DATABASE_HOST,
                        "password": settings.DATABASE_PASS,
                        "port": settings.DATABASE_PORT,
                        "user": settings.DATABASE_USER,
                        "ssl": ctx
                    }
                }
            },
            "apps": {
                "models": {
                    "models": settings.MODELS_TORTOISE,
                    "default_connection": "default",
                }
            }
        }
    else:
        logger.info("Using SQLITE DEV database")
        return {
            "connections": {
                "default": settings.DATABASE_URL
            },
            "apps": {
                "models": {
                    "models": settings.MODELS_TORTOISE,
                    "default_connection": "default",
                }
            }
        }
