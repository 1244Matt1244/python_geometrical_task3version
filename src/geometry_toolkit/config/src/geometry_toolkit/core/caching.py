# src/geometry_toolkit/core/caching.py
import functools
from redis import asyncio as aioredis
from contextlib import asynccontextmanager

class CacheManager:
    def __init__(self, redis_url: str):
        self.redis_url = redis_url

    @asynccontextmanager
    async def get_client(self):
        async with aioredis.from_url(self.redis_url) as client:
            yield client

    def lru_cache_async(self, maxsize=128):
        def decorator(func):
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                # Hybrid caching logic
                return await func(*args, **kwargs)
            return wrapper
        return decorator
