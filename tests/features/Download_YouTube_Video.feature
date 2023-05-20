Feature: Download YouTube Video
  As a music listener
  I want to easily download youtube videos to .mp3 files
  So that I can listen to them when I'm not online

  Scenario: Download YouTube Video
    Given a video on YouTube
    When I provide the URL for the video
    Then the video is downloaded and saved as an .mp3 file
