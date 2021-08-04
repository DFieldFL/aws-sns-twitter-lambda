import configparser
import logging
import twitter

def lambda_handler(event, context):
  config = configparser.ConfigParser()
  config.read('config.ini');
  consumer_key = ''
  consumer_secret = ''
  access_token_key = ''
  access_token_secret = ''
  if 'TwitterApi' in config:
    twitterConfig = config['TwitterApi']
    consumer_key = twitterConfig['consumer_key']
    consumer_secret = twitterConfig['consumer_secret']
    access_token_key = twitterConfig['access_token_key']
    access_token_secret = twitterConfig['access_token_secret']
  else:
    logging.warning('no twitter configuration in config.ini')

  twitterApi = None
  if consumer_key and consumer_secret and access_token_key and access_token_secret:
    twitterApi = twitter.Api(consumer_key=consumer_key,
                              consumer_secret=consumer_secret,
                              access_token_key=access_token_key,
                              access_token_secret=access_token_secret)
  for record in event['Records']:
    message = record['Sns']['Message']
    if message:
      logging.info('message: ' + message)
      if twitterApi:
        logging.info('sending to twitter')
        twitterApi.PostUpdate(message)
    else:
      logging.info('no message provided')
