from aiohttp import web

import settings


async def main(request):
    return web.Response(status=200, text="Hello world!")


if __name__ == "__main__":
    app = web.Application()
    app.router.add_get("/", main)
    web.run_app(app, port=settings.APP_PORT)
