from typing import Optional

import logging
import os

from pytube import YouTube
from pytube.exceptions import VideoUnavailable

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


def download_video(url: str) -> Optional[str]:
    """
    Downloads a YouTube video from the given URL and saves it to media
    directory.

    Args:
        url: The URL of the YouTube video to download.

    Returns:
        File path of the downloaded video.
    """
    try:
        yt = YouTube(url)

        # Get the first audio stream of the video
        stream = yt.streams.filter(only_audio=True).first()

        # Get the default output directory for downloads
        output_path = os.path.join(os.path.expanduser("~"), "Downloads")

        # Download the video
        print("Downloading video...")
        stream.download(output_path=output_path)

        # Convert the downloaded video to an .mp3 file
        print("Converting to mp3...")
        video_file = stream.default_filename
        mp3_file = os.path.splitext(video_file)[0] + ".mp3"
        video_path = os.path.join(output_path, video_file)
        mp3_path = os.path.join(output_path, mp3_file)
        os.system(f'ffmpeg -y -i "{video_path}" "{mp3_path}"')

        # Get path to media folder
        logger.info(f"Downloaded {mp3_path}")
        return mp3_path
    except VideoUnavailable:
        logger.error(f"Video {url} is unavailable.")
        return None
