import urlparse, random, string
import unittest

URLPrefix = "t.co/"
MAX_TWEET = 140
MAX_Retries = 10

URL_hashes = {}

class HashError(Exception):
    def __init__(self, value, errmsg):
        self.value = value
        self.errmsg = errmsg
    def __str__(self):
        return repr(self.value, self.errmsg)


def isValidURL(url):
    result = urlparse.urlparse(url)
    if not result.netloc and not result.path:
        return False
    return True

def getPossibleHashLength(tweet):
    hashLength = MAX_TWEET - len(tweet) - len(URLPrefix) - 1
    if hashLength < 0:
        return 0
    return hashLength


def generateHash(hashLength):
    retries = MAX_Retries
    present = False
    while not present and retries:
        potentialHash = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(hashLength))
        retries -= 1
        if potentialHash not in URL_hashes:
            return potentialHash
        #hopefully we don't end up here forever

    return generateHash(hashLength-1)



def generateURL(tweet, longURL):
    if not isValidURL(longURL):
        raise HashError(2, "URL is not valid")

    hashLength = getPossibleHashLength(tweet)
    if hashLength <= 4:
        raise HashError(1, "Tweet is too long")

    generatedHash = generateHash(hashLength)
    URL_hashes[generatedHash] = longURL

    return URLPrefix + generatedHash

def generateNewTweet(tweet, longURL):
    return tweet + ' ' + generateURL(tweet, longURL)




class TestURLGenerationMethods(unittest.TestCase):

    def test_normal_tweet(self):
        tweet = "The food smells nice"
        longURL = "www.foodpanda.com"
        generatedTweet = generateNewTweet(tweet, longURL)

        self.assertEqual(len(generatedTweet), MAX_TWEET)
        self.assertTrue(generatedTweet.startswith(tweet))
        self.assertEqual(generatedTweet[len(tweet)], ' ')
        self.assertNotEqual(generatedTweet.find(URLPrefix), -1)

        


'''
newTweet = generateNewTweet("The food smells nice", "www.+123.com")
print newTweet, len(newTweet)
'''
if __name__ == '__main__':
    unittest.main()