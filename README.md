# Lendico Challenge Data Engineering

### Considerations
- Python 3 (3.6) as main language 
- Save API data as raw data (in this case JSON). Because if i will convert to another format i will broken the data like a example, evolution schema. For don't loss any data I saved always in raw data, but I flexibility the project to add others formats in the future
- All environment context encapsulated in Docker containers
- Exercise 2, I saved the visualization as file, and this file will exists in output path (Dest variable)

## Running the project

#### Generate new api token
The Riot API TOKEN has a short life time value, and expire quickly. Because that you will need generate a new key to execute this project.

##### To generate
- Access https://developer.riotgames.com/ if you don't have a account in riot platform you will need create a new account
- Access menu (your account), and in this page you can generate your personal token


This project running on Docker container and you need build and run the container to get results

#### Docker build (building docker image)

Run this command:

```
docker build -t python-lendico .
```

#### Docker run (building docker image)

To run this container you need put some arguments to docker run.

- DEST (destination on file system to save the output)
- ACCESS_KEY (RIOT API Token Access Key)
- master_leagues_endpoint (RIOT master leagues endpoint)
- champion_mastery_endpoint (RIOT champion mastery endpoint)
- champion_mastery_summoner_id (Summoner id to filter by id)

In my mind I putted variable to flexibility the project.

Defaults arguments:
- DEST (You can put any path, but this path must be valid, and created before running, the path `\tmp` always exists in linux distributions)
- ACCESS_KEY you need generate API TOKEN
- master_leagues_endpoint = https://br1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5
- champion_mastery_endpoint = https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/
- champion_mastery_summoner_id = any summonerID (38qXY5lYF21b3TYLcF8j8lw0DlVrfdc8e8rCF55vdH1YlA)

Example to running project in docker
```
docker run -e "DEST=/tmp" -e "ACCESS_KEY=RGAPI-f29f0484-1c1a-4ff2-965d-d7d5a9901fb9" -e "master_leagues_endpoint=https://br1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5" -e "champion_mastery_endpoint=https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" -e "champion_mastery_summoner_id=38qXY5lYF21b3TYLcF8j8lw0DlVrfdc8e8rCF55vdH1YlA" python-lendico
```

In this example you can change DEST, ACCESS_KEY and champion_mastery_summoner_id and you will get the same result

##### How to check output Files

You will need use docker volumes and mapping your local file system with docker file system

Example:
```
    docker run -v your_local_system_path:container_path
```