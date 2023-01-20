import json
import requests
import datetime
import pandas as pd
import sqlalchemy
import sqlite3
from refresh import refresh
from Verify import check_if_valid_data



def run_spoti_dag():


    DATABASE_LOCATION = "sqlite:///played_tracks.sqlite"
    TOKEN= refresh()
    headers={
        "Authorization":"Bearer {token}".format(token=TOKEN),
        "Content-Type": "application/json"
    }

    yesterday = datetime.datetime.now() - datetime.timedelta(3)
    unix_time= int(yesterday.timestamp())*1000


    r=requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=unix_time),headers=headers)
    data=r.json()

    artist_name,song_name,played_at,timestamps=[],[],[],[]
    for song in data['items']:
        artist_name.append(song['track']['artists'][0]['name'])
        song_name.append(song['track']['name'])
        played_at.append(song['played_at'])
        timestamps.append(song['played_at'][0:10])


    song_dict={
        "song_name":song_name,
        "artist_name":artist_name,
        "played_at":played_at,
        "timestamps":timestamps
    }

    p=pd.DataFrame(song_dict, columns = ["song_name", "artist_name", "played_at", "timestamps"])

    if check_if_valid_data(p):
        print('data valid')
    else:
        print('invalid data')

    engine=sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('played_tracks.sqlite')
    cursor=conn.cursor()

    sql_query = """
        CREATE TABLE IF NOT EXISTS played_tracks(
            song_name VARCHAR(200),
            artist_name VARCHAR(200),
            played_at VARCHAR(200),
            timestamp VARCHAR(200),
            CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
        )
        """

    cursor.execute(sql_query)
    print("Opened database successfully")

    try:
        p.to_sql("played_tracks", engine,index=False,if_exists='append')
    except:
        print("Data already exists in the database")

    conn.close()
    print("Close database successfully")

run_spoti_dag()
