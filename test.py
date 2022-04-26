import asyncio
from async_polygon import RestClient
from data import config

async def check():
    async with RestClient(config.POLY_API) as requestor:
        print(requestor)
        requestor: RestClient
        await requestor.aggregate_bars('AAPL', 1, 'hour', '2022-03-29', '2022-04-26')


loop = asyncio.get_event_loop()
loop.run_until_complete(check())