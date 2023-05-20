"""Find Popular Videos By Artist on YouTube feature tests."""

from pytest_bdd import given, scenario, then, when


@scenario(
    "../features/Find_Popular_Videos_By_Artist_on_YouTube.feature",
    "Popular Videos By Artist",
)
def test_popular_videos_by_artist():
    """Popular Videos By Artist."""


@given("YouTube and pyTube")
def _():
    """YouTube and pyTube."""
    raise NotImplementedError


@when("I provide an artist")
def test_provide_artist():
    """I provide an artist."""
    raise NotImplementedError


@then("I get a list of URLs of YouTube videos by that artist")
def check_video_list():
    """I get a list of URLs of YouTube videos by that artist."""
    raise NotImplementedError
