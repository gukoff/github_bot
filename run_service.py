import aiohttp
from aiohttp import web
from gidgethub import routing, sansio
from gidgethub.aiohttp import GitHubAPI

import settings

router = routing.Router()


@router.register("issues", action="opened")
async def issue_opened_event(event, gh, *args, **kwargs):
    """ Whenever an issue is opened, greet the author and say thanks."""
    author = event.data["issue"]["user"]["login"]
    await gh.post(
        event.data["issue"]["comments_url"],
        data={
            'body': f'Thanks for the report, @{author}! But I am just a :robot:...'
        }
    )


async def main(request):
    event = sansio.Event.from_http(
        body=await request.read(),
        headers=request.headers,
        secret=settings.WEBHOOK_SECRET,
    )

    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(
            session, 'gukoff', oauth_token=settings.TOKEN
        )
        await router.dispatch(event, gh)

    return web.Response(status=200)


if __name__ == "__main__":
    app = web.Application()
    app.router.add_post("/", main)
    web.run_app(app, port=settings.APP_PORT)
