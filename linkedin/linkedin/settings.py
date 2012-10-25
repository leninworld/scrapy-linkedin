# Scrapy settings for linkedin project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'linkedin'

SPIDER_MODULES = ['linkedin.spiders']
NEWSPIDER_MODULE = 'linkedin.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'linkedin (+http://www.yourdomain.com)'

# Enable auto throttle
AUTOTHROTTLE_ENABLED = True

# Set your own download folder
DOWNLOAD_FILE_FOLDER = '/Users/ChenWei/Documents/internet/com/github/scrapy-linkedin/linkedin/download_file'


