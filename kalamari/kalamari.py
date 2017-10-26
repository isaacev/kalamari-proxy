#! /usr/bin/env python3
import asyncio
import proxy


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    proxy_instance = proxy.ProxyServer(loop)
    coro = asyncio.start_server(proxy_instance.handler, '127.0.0.1', 3128,
                                loop=loop)
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
