import pytest

from app.services.url_shortener import md5_shortener_context


class Testmd5ShortenContext:

    @pytest.fixture(autouse=True)
    def _setup(self):
        self.shorten_context = md5_shortener_context
        self.base_url = "https://en.wikipedia.org/wiki/Computer"

    def test_shorten_url(self):
        shortened_url = self.shorten_context.shorten_url(self.base_url)
        assert shortened_url.startswith(self.shorten_context.url_start)
        assert len(shortened_url) > len(self.shorten_context.url_start)

    def test_empty_url(self):
        with pytest.raises(ValueError):
            self.shorten_context.shorten_url("")

    def test_long_url(self):
        long_url = "https://www.example.com/" + "a" * 200
        shortened_long_url = self.shorten_context.shorten_url(long_url)
        assert shortened_long_url.startswith(self.shorten_context.url_start)
        assert len(shortened_long_url) > len(self.shorten_context.url_start)

    def test_contains_special_characters(self):
        special_chars_url = "https://www.example.com/?q=1&param=test"
        shortened_special_chars_url = self.shorten_context.shorten_url(
            special_chars_url
        )
        assert shortened_special_chars_url.startswith(self.shorten_context.url_start)
        assert len(shortened_special_chars_url) > len(self.shorten_context.url_start)

    def test_hash_length(self):
        self.shorten_context.hash_length = 10

        shortened_url = self.shorten_context.shorten_url(self.base_url)

        assert (
            len(shortened_url)
            == len(self.shorten_context.url_start) + self.shorten_context.hash_length
        )

    def test_url_start(self):
        self.shorten_context.url_start = "http://shorter.com/"

        shortened_url = self.shorten_context.shorten_url(self.base_url)

        assert shortened_url.startswith(self.shorten_context.url_start)
        assert len(shortened_url) > len(self.shorten_context.url_start)
