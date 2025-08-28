# Weather-App
- This App Predict City Weather

## How it works?
1. Clone the repo:
    `git clone https://github.com/Ziad-kh99/learn-DevOps.git`
    - Then you should change working dir to the project dir
        `cd learn-DevOps/weather_app/source`

2. Build the image based on Dockerfile:
    `docker build -t weather_app:v1 .`

3. Run the the container:
    `docker run -i --name weather-app -p 8000:8000 weather-app`
    - Note that the first time you need to run the container, just use command `docker start` instead of creating new container.
    `docker start -i weather-app`
