# Space Explorer

[![Run on Repl.it](https://repl.it/badge/github/space-explorer/bfarahdel)](https://replit.com/@BritnyFarahdel/space-explorer#.replit)
[![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)](https://spaceexplorerweb-c2a157af97f1.herokuapp.com/)

A website where users can explore and gain insight to information about asteroids, mars, and more. The website is hosted on [Replit](https://replit.com/) and developed with the Python [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework, and utilizes the [NASA API](https://api.nasa.gov/) from the [National Aeronautics and Space Administration (NASA)](https://www.nasa.gov/).

**Website URL:** https://replit.com/@BritnyFarahdel/space-explorer (Please also read the **Warning** section below for information regarding the Mars webpage)

The navbar consists of 4 pages the user can visit:

1. "Home": the main page of the website. The [Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html) from the NASA will be displayed along with the title of the image and a brief description of the image.
2. "Asteroids": lists information regarding the number of asteroids currently near earth based on the current date of the website visit as well as each asteroid's name, estimated diameter (kilometers), relative velocity (m/s), distance to Earth (kilometers), and whether or not the asteroid is considered a threat to Earth.
3. "Space Weather": Provides defintions for Coronal Mass Ejections and Solar Flares within the past 30 days of the current UTC date.
   - Coronal Mass Ejections: Speed data (km/s) from NASA is displayed and each date contains a link to the [Space Weather Database Of Notifications, Knowledge, Information (DONKI)](https://kauai.ccmc.gsfc.nasa.gov/DONKI/) for the corresponding coronal mass ejection.
   - Solar Flares: Class information from NASA is displayed and each date contains a link to the [Space Weather Database Of Notifications, Knowledge, Information (DONKI)](https://kauai.ccmc.gsfc.nasa.gov/DONKI/) for the corresponding solar flare. The query is for high-speed solar flares (above 500 km/s).
4. "Mars": Contains NASA data regarding the weather in mars and the latest photos taken by mars rover.
   - Weather: includes NASA data for the last datum of the Sol for when the weather data was obtained, the atmospheric temperature (Fahrenheit), average wind speed (m/s), average atmospheric pressure (Pa), and the season. :exclamation:**Warning: Mars weather data may not be available from NASA and a message will appear on the screen to indicate this. This occurs because there can be issues with the sensors on Mars that result in missing data. When the data is available, it will be displayed on the webpage.**:exclamation:
   - Rover images: when the webpage loads, 3 randomly selected rover images are displayed along with the sol, earth date, and the name of the rover that took the image. **Note: Sometimes duplicate images may be displayed. This is a known issue from NASA and occurs because the database sometimes contains multiple copies of the image, even though unique indices are being used to extract information from the database.**

# Warning

:exclamation:**Mars weather data may not be available from NASA and a message will appear on the screen to indicate this. This is a known issue from NASA and occurs because there can be issues with the sensors on Mars that result in missing data. When the data is available, it will be displayed on the webpage.**:exclamation:
