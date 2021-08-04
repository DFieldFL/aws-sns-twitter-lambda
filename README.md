# AWS SNS to Twitter
Publishes AWS SNS messages to the Twitter account of your choosing using AWS Lambda

## Requirements
- Python 3.8.x
- Twitter API Credentials

## Installation and Setup
1. Clone the repository
1. Install the dependencies `pip install -r requirements.txt`
1. Copy file `config.template.ini` and save it as `config.ini`
1. Modify the relevant information in `config.ini`
1. Test it out `python -c 'from BogoMain import *; lambda_handler("", "");'`
1. Zip the project files `zip -g ~/sns_twitter.zip lambda_function.py config.ini`
1. Add projects dependencies (`site-packages`). cd to `site-packages` and execute this command `zip -r9 ~/sns_twitter.zip .`

### Config
#### TwitterApi
If the section does not exist the output will only be to the logs. If you would like to post to twitter apply for a [developer account](https://developer.twitter.com/en/apply-for-access) and enter in required info in this section.
