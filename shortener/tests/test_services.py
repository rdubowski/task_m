import pytest

from app.services.url_shortener import (
    DEFAULT_HASH_LENGTH,
    DEFAULT_URL_START,
    md5_shortener_context,
)


class Testmd5ShortenContext:
    @pytest.fixture(autouse=True)
    def _setup(self) -> None:
        self.shorten_context = md5_shortener_context
        self.base_url = "https://en.wikipedia.org/wiki/Computer"

    @pytest.mark.parametrize(
        "base_url",
        (
            "https://en.wikipedia.org/wiki/Computer",
            "https://www.example.com/" + "a" * 200,
            "https://www.example.com/?q=1&param=test",
        ),
        ids=["normal", "long", "special_chars"],
    )
    def test_shorten_url(self, base_url) -> None:
        shortened_url = self.shorten_context.shorten_url(base_url)
        assert shortened_url.startswith(DEFAULT_URL_START)
        assert len(shortened_url) == len(DEFAULT_URL_START) + DEFAULT_HASH_LENGTH

    def test_empty_url(self) -> None:
        with pytest.raises(ValueError):
            self.shorten_context.shorten_url("")

    def test_hash_length(self) -> None:
        self.shorten_context.hash_length = 10

        shortened_url = self.shorten_context.shorten_url(self.base_url)

        assert (
            len(shortened_url)
            == len(DEFAULT_URL_START) + self.shorten_context.hash_length
        )

    def test_url_start(self) -> None:
        self.shorten_context.url_start = "http://shorter.com/"

        shortened_url = self.shorten_context.shorten_url(self.base_url)

        assert shortened_url.startswith(self.shorten_context.url_start)
