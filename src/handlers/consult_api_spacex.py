from aiohttp import ClientSession


async def handler_consult_api_spacex():
    async with ClientSession() as session:
        async with session.get('https://api.spacexdata.com/v3/launches/latest?pretty=true') as req:
            resp = req
            if resp.status == 200:
                return await resp.json()
            else:
                return resp.status
