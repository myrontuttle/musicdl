from musicdl import download_youtube


# Test that the video can be downloaded successfully
def test_download_youtube_video():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    yt = download_youtube.url_to_youtube(url)
    mp3_path = download_youtube.download_video(yt)
    assert (
        mp3_path == "C:\\Users\\myron\\Downloads\\Never Gonna Give You "
        "Up.mp3"
    )


# Test that the user is notified of any errors during the download process.
def test_download_error_notification():
    url = "https://www.youtube.com/watch?v=invalid_url"
    yt = download_youtube.url_to_youtube(url)
    assert download_youtube.download_video(yt) is None


def test_input_artist_name():
    artist_name = "The Beach Boys"
    urls = download_youtube.find_videos(artist_name)
    assert urls is not None


def test_download_all():
    download_youtube.download_all()
    assert True
