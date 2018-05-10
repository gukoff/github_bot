import asyncio
import aiohttp
from gidgethub.aiohttp import GitHubAPI

import settings


async def create_issue(gh, repo='github_bot'):
    return (
        await gh.post(
            f'/repos/{gh.requester}/{repo}/issues',
            data={
                'title': 'We got a problem',
                'body': 'Use. More. Emoji.',
            }
        )
    )


async def comment_issue(gh, issue_id, repo='github_bot'):
    return (
        await gh.post(
            f'/repos/{gh.requester}/{repo}/issues/{issue_id}/comments',
            data={
                'body': 'BUMP',
            }
        )
    )


async def close_issue(gh, issue_id, repo='github_bot'):
    return (
        await gh.patch(
            f'/repos/{gh.requester}/{repo}/issues/{issue_id}',
            data={
                'state': 'closed',
            }
        )
    )


async def react_on_issue(gh, issue_id, repo='github_bot'):
    return (
        await gh.post(
            f'/repos/{gh.requester}/{repo}/issues/{issue_id}/reactions',
            data={
                'content': 'heart',
            },
            accept='application/vnd.github.squirrel-girl-preview+json'
        )
    )


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, requester='gukoff', oauth_token=settings.TOKEN)
        issue_id = (await create_issue(gh))['number']
        await comment_issue(gh, issue_id)
        await react_on_issue(gh, issue_id)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
