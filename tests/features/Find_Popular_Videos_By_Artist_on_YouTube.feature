Feature: Find Popular Videos By Artist on YouTube
  As a music lover
  I want a list of YouTube video URLs for the top songs by an artist
  So that I can download those videos

  Scenario: Popular Videos By Artist
    Given YouTube and pyTube
    When I provide an artist
    Then I get a list of URLs of YouTube videos by that artist
