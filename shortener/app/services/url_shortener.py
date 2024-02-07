from abc import ABC, abstractmethod
from dataclasses import dataclass
import hashlib
from typing import NewType, Sequence

DEFAULT_URL_START = "http://short.est/"

BaseUrl = NewType('BaseUrl', str)
ShortenedUrl = NewType('ShortenedUrl', str)


class ShortenerStrategy(ABC):
    @abstractmethod
    def encode(self, base_url: BaseUrl) -> ShortenedUrl:
        pass
    
class Md5Strategy(ShortenerStrategy):
    def encode(self, base_url: BaseUrl) -> ShortenedUrl:
        hash_value = hashlib.md5(base_url.encode()).hexdigest()[:6]
        return hash_value
    

@dataclass
class ShortenContext:
    strategy: ShortenerStrategy
    url_start: str = DEFAULT_URL_START


    def shorten_url(self, base_url: BaseUrl) -> ShortenedUrl:
        if not base_url:
            raise ValueError("Empty base_url")
        encoded_part = self.strategy.encode(base_url=base_url)
        return f"{self.url_start}{encoded_part}"
    

md5_shortener_context = ShortenContext(strategy=Md5Strategy())