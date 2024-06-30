# fantastic-umbrella

Goal:
* Service that continously loads and stores your spotify history in a database
  * Skips any songs played <30 seconds
 
Implementation:
* Built in Python
* Hits Spotify API once a minute
  * Stores API key?
* Upserts into database (PostgreSQL?), skipping any duplicate listens already there
  * Including username + listening metadata (listen_id, time, song, album, artist, genre, ...)
* Uses python thread to execute polling (I/O constrained)

Future plan:
* Exposes an API that allows returning listen history over a time period
* Starts clustering listens
  * Avoids clustering if listens correspond to liked list order, or same album(?)
  * Require getting liked list
* Supports multiple users
* Identifying patterns across users
