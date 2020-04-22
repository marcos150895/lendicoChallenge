#!/bin/bash -x

echo Starting python app ...

export PYTHONPATH='.'

python main.py --dest $DEST \
            --access_key $ACCESS_KEY \
            --master_leagues_endpoint $master_leagues_endpoint \
            --champion_mastery_endpoint $champion_mastery_endpoint \
            --champion_mastery_summoner_id $champion_mastery_summoner_id
