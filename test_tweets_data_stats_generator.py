"""
Note that this file cannot be modified.
If you would like to add your own unit tests, please put these in a separate test file.
"""

import pytest
from tweets.tweets_api_service import TweetsAPIService
from tweets.tweets_data_stats_generator import TweetsDataStatsGenerator

JOE_SMITH_USER = "joe_smith"

_generator = TweetsDataStatsGenerator(TweetsAPIService())
res = TweetsAPIService().get_tweets(JOE_SMITH_USER)
TweetsDataStatsGenerator(res).get_most_tweets_for_any_day(JOE_SMITH_USER)
TweetsDataStatsGenerator(res).get_longest_tweet(JOE_SMITH_USER)
TweetsDataStatsGenerator(res).find_most_days_between_tweets(JOE_SMITH_USER)
TweetsDataStatsGenerator(res).get_most_popular_hash_tag(JOE_SMITH_USER)
@pytest.fixture
def stats_generator_setup():
    return _generator

def test_most_tweets(stats_generator_setup):
    assert stats_generator_setup.get_most_tweets_for_any_day(JOE_SMITH_USER) == 10

def test_longest_tweet(stats_generator_setup):
    assert stats_generator_setup.get_longest_tweet(JOE_SMITH_USER) == "0c2dc961-a0ae-470e-81a6-8320504dae14"

def test_most_days_between_tweets(stats_generator_setup):
    assert stats_generator_setup.find_most_days_between_tweets(JOE_SMITH_USER) == 120

def test_most_popular_hash_tag(stats_generator_setup):
    assert stats_generator_setup.get_most_popular_hash_tag(JOE_SMITH_USER) == "#WorldCup2018"
