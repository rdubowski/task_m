import hashlib
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeAlias

DEFAULT_URL_START = "http://short.est/"
DEFAULT_HASH_LENGTH = 6

BaseUrl: TypeAlias = str
ShortenedUrl: TypeAlias = str


class ShortenerStrategy(ABC):
    @abstractmethod
    def encode(self, base_url: BaseUrl, hash_length: int) -> ShortenedUrl:
        pass


class Md5Strategy(ShortenerStrategy):
    def encode(self, base_url: BaseUrl, hash_length: int) -> ShortenedUrl:
        hash_value = hashlib.md5(base_url.encode()).hexdigest()[:hash_length]
        return hash_value


@dataclass
class ShortenContext:
    strategy: ShortenerStrategy
    url_start: str = DEFAULT_URL_START
    hash_length: int = DEFAULT_HASH_LENGTH

    def shorten_url(self, base_url: BaseUrl) -> ShortenedUrl:
        """
        Shortens the given base URL by
        encoding it and appending it to the url_start parameter.
        """
        if not base_url:
            raise ValueError("Empty base_url")
        encoded_part = self.strategy.encode(
            base_url=base_url, hash_length=self.hash_length
        )
        return f"{self.url_start}{encoded_part}"


md5_shortener_context = ShortenContext(strategy=Md5Strategy())
