from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend
from config import SECRET_0

cookie_transport = CookieTransport(cookie_max_age=3600, cookie_name="bonds")

SECRET = SECRET_0


def gett_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(name='jwt', transport=cookie_transport, get_strategy=gett_jwt_strategy)
