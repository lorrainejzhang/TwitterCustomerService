import csv
import string


def read_file(path):
	with open(path, 'rb') as csvfile:
		headers = None
		tweets = []
		fileRows = [row for row in csv.reader(csvfile.read().splitlines())]
		headers = fileRows[0]
		tweets = fileRows[1:]
		return headers, tweets

def find_tweet_responses(tweets):
	has_response = []
	doesnt_have_response = []
	for tweet in tweets:
		if tweet[-2] == '':
			doesnt_have_response.append(tweet)
		else:
			has_response.append(tweet)
	return has_response, doesnt_have_response

def create_response_csv(has_response):
	with open('responses.csv', 'wb') as csvfile:
	    spamwriter = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    for tweet in has_response:
	    	spamwriter.writerow(tweet)

def create_no_response_csv(doesnt_have_response):
	with open('no_responses.csv', 'wb') as csvfile:
	    spamwriter = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    for tweet in doesnt_have_response:
	    	spamwriter.writerow(tweet)

def get_punctuation(path):
	d = dict()
	with open(path, 'rb') as csvfile:
		fileRows = [row for row in csv.reader(csvfile.read().splitlines())]
		for row in fileRows:
			tweetContent = row[4]
			for c in tweetContent:
				if c in string.punctuation:
					if c in d:
						d[c] += 1
					else:
						d[c] = 1
		return d



def main():
	headers, tweets = read_file('../Downloads/twcs.csv')
	has_response, doesnt_have_response = find_tweet_responses(tweets)
	# create_response_csv(has_response)
	# create_no_response_csv(doesnt_have_response)
	responses_punctuation = get_punctuation('responses.csv')
	no_responses_punctuation = get_punctuation('responses.csv')
	overall = get_punctuation('../Downloads/twcs.csv')
	print(overall)


if __name__ == "__main__":
    main()
