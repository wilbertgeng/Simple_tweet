# Python-CodeScreen-Tweets-Test

The CodeScreen Tweets API is a service that contains one endpoint,<br>
`GET` https://app.codescreen.dev/api/assessments/tweets, which returns the details of all tweets for a given user. <br>The user name is passed in as a query parameter called `userName` in the endpoint URL.

For authentication, you need to send your API token in the `Authorization HTTP header` using the [Bearer authentication scheme](https://tools.ietf.org/html/draft-ietf-oauth-v2-bearer-20#section-2.1). Your API token is `8c5996d5-fb89-46c9-8821-7063cfbc18b1`.

Here is an example of how to send a request from `cURL`:

    curl -H "Authorization: Bearer 8c5996d5-fb89-46c9-8821-7063cfbc18b1" \
    https://app.codescreen.dev/api/assessments/tweets?userName=joe_smith

When you send an `HTTP GET` request to the endpoint, the response will be a `200 OK`, which includes a body containing a list of tweet data in `JSON` format. 
<br><br>
An example response is the following:

     [
       {
           "id": "52f83d7c-ad2c-4ca0-b742-b03bc27f0c96",
           "createdAt": "2017-12-01T11:12:42",
           "text": "Chrome or Firefox? #Browsers",
           "user": {
               "id": "75343078-b5dd-306f-a3f9-8203a3915144",
               "userName": "joe_smith"
           }
       },
       {
           "id": "5f52e882-36a5-4460-a33b-e834b406650e",
           "createdAt": "2017-12-02T12:17:52",
           "text": "Bought a real Christmas tree, smells a lot more christmassy! #Xmas",
           "user": {
               "id": "75343078-b5dd-306f-a3f9-8203a3915144",
               "userName": "joe_smith"
           }
       }
     ]


The `id` field represents the unique id for the tweet. The `createdAt` field contains the time at which the tweet was
published, in ISO-8601 extended offset date-time format. You can assume all date-times are in the same timezone. </br>
The `user` field contains a JSON object which is made up of the unique id and name of the user who published the tweet.

## Your Task

You are required to implement all the methods marked with `TODO Implement` in the [TweetsAPIService](tweets/tweets_api_service.py) and [TweetDataStatsGenerator](tweets/tweets_data_stats_generator.py) classes in such a way that
all the unit tests in the [test_tweets_data_stats_generator.py](test/test_tweets_data_stats_generator.py) file pass.

[TweetsAPIService](tweets/tweets_api_service.py) should be implemented in such a way that you only need to call out to the CodeScreen Tweets API
endpoint once per full run of the [test_tweets_data_stats_generator.py](test/test_tweets_data_stats_generator.py) test suite.

## Requirements

The [test_tweets_data_stats_generator.py](test/test_tweets_data_stats_generator.py) file should not be modified. If you would like to add your own unit tests, you
can add these in a separate file.

The [requirements.txt](requirements.txt) file should only be modified to add any third-party dependencies required for your solution. <br> Please note that all third-party depdencies required for your solution **MUST** be added to the [requirements.txt](requirements.txt) file.

You are free to use whichever libraries you want (Python or third-party) when implementing your solution. </br>
Note we recommend using the <a href="https://docs.python.org/3.7/library/datetime.html" target="_blank">`Python datetime`</a> library for working with dates & times, and the <a href="https://pypi.org/project/requests/" target="_blank">`Requests`</a> HTTP client library to interact with the CodeScreen Tweets API service.

Your solution also must use/be compatible with `Python version 3.7`.

##

This test should take no longer than 2 hours to complete successfully.

Good luck!

## Submitting your solution

Please push your changes to the `master branch` of this repository. You can push one or more commits. <br>

Once you are finished with the task, please click the `Complete task` link on <a href="https://app.codescreen.dev/#/codescreentest9f9fe6a8-f49d-4e0c-b066-5e71bb4a4d53" target="_blank">this screen</a>.