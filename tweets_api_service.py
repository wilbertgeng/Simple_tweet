import requests
class TweetsAPIService(object):

    tweets_endpoint_url = 'https://app.codescreen.dev/accessments/tweets?userName=joe_smith'

    # Your API token. Needed to successfully authenticate when calling the tweets endpoint.
    # This needs to be included in the Authorization header (using the Bearer authentication scheme) in the request you send to the tweets endpoint.
    api_token = "8c5996d5-fb89-46c9-8821-7063cfbc18b1"

    # Retrieves all tweets for the given user by calling the https://app.codescreen.dev/api/assessments/tweets endpoint.
    # The username should be passed in the request as a query parameter called userName.
    def get_tweets(self, user_name):
        """TODO Implement
        """
        headers = {'authorization': "Bearer " + self.api_token}
        response = requests.get('https://app.codescreen.dev/api/assessments/tweets?userName=joe_smith', headers=headers)
        r = response.json()
        # print(type(r))
        return r
