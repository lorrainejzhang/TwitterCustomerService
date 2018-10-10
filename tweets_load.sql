--TO LOAD DATABASE: run postgres and run: psql -d postgres -U isdb -f tweets_load.sql

DROP TABLE IF EXISTS TweetsRaw CASCADE;


CREATE TABLE TweetsRaw (
    tweet_id                  TEXT,
    author_id                 TEXT,
    inbound                   BOOLEAN,
    created_at                TIMESTAMP,
    tweet                     TEXT,
    response_tweet_id         TEXT,
    in_response_to_tweet_id   TEXT
               
);

\copy TweetsRaw FROM 'twcs.csv' csv encoding 'ISO8859-1' header;
