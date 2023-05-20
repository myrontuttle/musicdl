from musicdl import download_youtube


# Test that the video can be downloaded successfully
def test_download_youtube_video():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    mp3_path = download_youtube.download_video(url)
    assert (
        mp3_path == "C:\\Users\\myron\\Downloads\\Never Gonna Give You "
        "Up.mp3"
    )


# Test that the user is notified of any errors during the download process.
def test_download_error_notification():
    url = "https://www.youtube.com/watch?v=invalid_url"
    assert download_youtube.download_video(url) is None
