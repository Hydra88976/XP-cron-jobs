import requests
import time
import random

url = "https://www.youtube.com/youtubei/v1/live_chat/send_message?prettyPrint=false"

headers = {
  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
  'Content-Type': "application/json",
  'x-origin': "https://www.youtube.com",
  'x-youtube-bootstrap-logged-in': "true",
  'authorization': "SAPISIDHASH 1756121312_6f4b86faa1ec834bf77a17ec6092e44af06314fe_u SAPISID1PHASH 1756121312_6f4b86faa1ec834bf77a17ec6092e44af06314fe_u SAPISID3PHASH 1756121312_6f4b86faa1ec834bf77a17ec6092e44af06314fe_u",
  'x-youtube-client-name': "1",
  'x-youtube-client-version': "2.20250821.07.00",
  'x-goog-authuser': "1",
  'x-goog-visitor-id': "CgtMZGdyUmM2NkxTTSiqkbHFBjIKCgJJThIEGgAgSw%3D%3D",
  'origin': "https://www.youtube.com",
  'x-client-data': "CIS2yQEIo7bJAQipncoBCIa1ygEIjrrKARiFnMsB",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "same-origin",
  'sec-fetch-dest': "empty",
  'referer': "https://www.youtube.com/live_chat?continuation=0ofMyAOAARpeQ2lrcUp3b1lWVU5yUm1WdlRsTnhXVlJoTjNSeWJqYzFWMDA1ZEhObkVndDBUbXRhYzFKWE4yZ3lZeG9UNnFqZHVRRU5DZ3QwVG10YWMxSlhOMmd5WXlBQk1BQSUzRDABggEICAQYAiAAKACIAQGgAY6z2LPtpY8DqAEAsgEA&dark_theme=true&authuser=1",
  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
  'Cookie': "VISITOR_INFO1_LIVE=LdgrRc66LSM; VISITOR_PRIVACY_METADATA=CgJJThIEGgAgSw%3D%3D; PREF=f6=40000000&tz=Asia.Calcutta&f4=4000000&f5=30000; HSID=ACt-2HeLxiWJKhtXo; SSID=AOGmuF0-y7LvmWSg9; APISID=wd5w-HcOlelUwxBk/AFvnxZ2zv3CARPzsn; SAPISID=U5eljb9C8e0xWM_t/AOWRAd7x4FbZeSQt3; __Secure-1PAPISID=U5eljb9C8e0xWM_t/AOWRAd7x4FbZeSQt3; __Secure-3PAPISID=U5eljb9C8e0xWM_t/AOWRAd7x4FbZeSQt3; SID=g.a0000gg-FQJUONgnLNXB7oJ2mz8niKDwAMjAhgHfGTMc6yCCSMuoX8I0n4UzBQZzJMNDx4OaTAACgYKASgSARUSFQHGX2MivMhzKkZuGq4y2XVyb2zqpxoVAUF8yKqx4il277PnBef8lhE49YVd0076; __Secure-1PSID=g.a0000gg-FQJUONgnLNXB7oJ2mz8niKDwAMjAhgHfGTMc6yCCSMuoo36NeQm-5x_aLFH2X9RkQQACgYKATwSARUSFQHGX2Mi-HvceTe6TXROCUYygJcK6BoVAUF8yKr1HDFRU98ugaIJ53kEH1Hg0076; __Secure-3PSID=g.a0000gg-FQJUONgnLNXB7oJ2mz8niKDwAMjAhgHfGTMc6yCCSMuoFAz7a3oOHH6HfmytudnX1wACgYKAScSARUSFQHGX2MiLcQt6Y9GT5OL1Mh82KvxuxoVAUF8yKolIH1CA4uW6TDoUEVcfplB0076; __Secure-ROLLOUT_TOKEN=CKzfwrb9oJCw8AEQpKD3qLGhjwMYi5L6peOljwM%3D; YSC=rTWiIQwQFiI; __Secure-1PSIDTS=sidts-CjUB5H03P6jFTw-bfOB3-AGQkHvPdxTmc3K5ZSEbOmg78IuIvgxC99ij2FVim4iNyyfhBQS8GRAA; __Secure-3PSIDTS=sidts-CjUB5H03P6jFTw-bfOB3-AGQkHvPdxTmc3K5ZSEbOmg78IuIvgxC99ij2FVim4iNyyfhBQS8GRAA; LOGIN_INFO=AFmmF2swRAIgNweyhZHQUX9DGYgC7mk0_-Jq1gJf3K7W5_PBPQJ2aEECIE1sEmMrwUORYMTMbOkm1kvqREiwZ0QrHT_Gn1TExdu7:QUQ3MjNmejRMeHdjNWk5WjRtWHhpbzBMTVl2RklUSlRKMWRSR2JIQ0NwYW1qSDlTTFExcEZQUVdaZ1ZmaEhqS2k5RjZpd3B4Qi1VN0Fxc0ViOXZKa3M3aWZva2RXdlp2M2lfZTRZUm1fZ05rWFpWczk0TFMxWVZrdDFqd0ZQZWlEZmk0NUJtQTllcWVpZUtaUFdPTGZHd3Q1NjZHZHBzY25R; SIDCC=AKEyXzX4MSqprcc5yUWLy7I2Ca4Q00sUuuVPKTeZgMg28xueTcvcA26mS8c2vEYa7MvB8p1M1g; __Secure-1PSIDCC=AKEyXzUMgW8d6UC1lfnqdS-bKA-FHoOcaHGH_rygRQ40hvFihcY8gOdsbTuYEqm4L94jxXpfoqc; __Secure-3PSIDCC=AKEyXzVIhKMjb0rfFPEyEqxV12FKTlujmlz-lbPxKbNzeGUh_lM6qEo6jTO4xtfqDnX17i8S0w; ST-183jmdn=session_logininfo=AFmmF2swRAIgNweyhZHQUX9DGYgC7mk0_-Jq1gJf3K7W5_PBPQJ2aEECIE1sEmMrwUORYMTMbOkm1kvqREiwZ0QrHT_Gn1TExdu7%3AQUQ3MjNmejRMeHdjNWk5WjRtWHhpbzBMTVl2RklUSlRKMWRSR2JIQ0NwYW1qSDlTTFExcEZQUVdaZ1ZmaEhqS2k5RjZpd3B4Qi1VN0Fxc0ViOXZKa3M3aWZva2RXdlp2M2lfZTRZUm1fZ05rWFpWczk0TFMxWVZrdDFqd0ZQZWlEZmk0NUJtQTllcWVpZUtaUFdPTGZHd3Q1NjZHZHBzY25R; ST-6m7wh8=session_logininfo=AFmmF2swRQIgbzok02HgbUlmVynndn5uvyAEMyD7QFZR_0TPW2dAUF8CIQCDqP7YPft1td6gx0TiRpZVNpvT8lvKo7sZDz8mmVEDhw%3AQUQ3MjNmd3k4amd4TWYtLVJXeFVJNnFOcWNkWFdZamtaWG9aTmc3T2J1cUZqeVJNcERtQmNTaDF6R1pvQVVjcG9xQ3B6QXIyS09VejFvNEg0OVNYbHVZR21xQ0FSTm5JQ2pIenA3bjMxQVJweUJDOTZYQkZiR19zRW5YMV9jdnJYNHdPV21DQVBEMGxuX3JlYWlZNVlPQ182VklrOE00MW1B"
}
texts = [
    "🍓",
    "🍒️️",
    "🍎",
    "🍉",
    "🍊",
    "🥭️",
    "🍍",
    "🍋",
    "🍈",
    "🍏",
    "🍐",
    "🥝",
    "🍇",
    "🍅",
    "🥥",
    "🍄",
    "🥕",
    "🍞",
    "🥬",
    "🥦",
    "🍕",
    "🥞",
    "🥜",
    "🥨",
    "🌮",
    "🍔",
    "🥗",
    "🍛",
    "🍖",
    "🌭",
    "️🥣",
    "🧀",
    "🍗",
    "🍝"
    ]

repeat_count = 3
delay_between_batches = 60 * 60  # 60 minutes in hour

batch_number = 1

while True:
    print(f"=== Batch {batch_number} starting ===")
    for i in range(repeat_count):
        random_text = random.choice(texts)

        payload = {
  "context": {
    "client": {
      "hl": "en-GB",
      "gl": "IN",
      "remoteHost": "2405:201:4017:c9a5:10fb:9568:b4ca:db4a",
      "deviceMake": "",
      "deviceModel": "",
      "visitorData": "CgtMZGdyUmM2NkxTTSib5afFBjIKCgJJThIEGgAgSw%3D%3D",
      "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36,gzip(gfe)",
      "clientName": "WEB",
      "clientVersion": "2.20250821.07.00",
      "osName": "X11",
      "osVersion": "",
      "originalUrl": "https://www.youtube.com/live_chat?continuation=0ofMyAOAARpeQ2lrcUp3b1lWVU5vYWpNMmRrSTBPRXg0Unpsak9VOXVhWEp6UTJwQkVndDBVVUpIU0Y5ZlJuRmZNQm9UNnFqZHVRRU5DZ3QwVVVKSFNGOWZSbkZmTUNBQk1BQSUzRDABggEICAQYAiAAKACIAQGgAbTNqpCzoY8DqAEAsgEA&dark_theme=true&authuser=0",
      "screenPixelDensity": 2,
      "platform": "DESKTOP",
      "clientFormFactor": "UNKNOWN_FORM_FACTOR",
      "configInfo": {
        "appInstallData": "CJvlp8UGENfBsQUQ0-GvBRDQ1s8cEJT-sAUQ56_PHBD50M8cEOLozxwQudnOHBDN0bEFEOLUrgUQibDOHBCZjbEFEODNsQUQgo_PHBC45M4cELOQzxwQhefPHBDJ968FEMTWzxwQ3rzOHBC9irAFEI3MsAUQq53PHBCd0M8cEParsAUQ2vfOHBCRjP8SEKrozxwQgc3OHBDFw88cEL3QzxwQoq_PHBCIh7AFEPyyzhwQ8t_PHBDS5c8cEI24zxwQq_jOHBDw1M8cEOSVsAUQnNfPHBDbr68FEJ7QsAUQh6zOHBCT3c8cEK7WzxwQ8ZywBRD7tM8cEP7AzxwQzN-uBRCYuc8cEPDjzxwQt-r-EhCJ6K4FEMvRsQUQppqwBRC9tq4FEJOZgBMQu9nOHBD12c8cENHgzxwQkd3PHBCZmLEFEOLKzxwQvZmwBRCKgoATEOmIzxwQ_5bPHBDSpIATEPXbzxwqQENBTVNLaFVob0wyd0ROSGtCcmlVRXJQUTVndVA5QTd2LXdiVl9BQzF6QWFIVERMQWd3VFlJUU9EM1FVZEJ3PT0wAA%3D%3D"
      },
      "screenDensityFloat": 2,
      "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
      "timeZone": "Asia/Calcutta",
      "browserName": "Chrome",
      "browserVersion": "81.0.4044.138",
      "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "deviceExperimentId": "ChxOelUwTVRneU5UYzVPVEEzT1RVeU56STRPQT09EJvlp8UGGJvlp8UG",
      "rolloutToken": "CKzfwrb9oJCw8AEQpKD3qLGhjwMYmsCIqbGhjwM%3D",
      "screenWidthPoints": 930,
      "screenHeightPoints": 594,
      "utcOffsetMinutes": 330,
      "connectionType": "CONN_WIFI",
      "memoryTotalKbytes": "2000000",
      "mainAppWebInfo": {
        "graftUrl": "https://www.youtube.com/live_chat?continuation=0ofMyAOAARpeQ2lrcUp3b1lWVU5vYWpNMmRrSTBPRXg0Unpsak9VOXVhWEp6UTJwQkVndDBVVUpIU0Y5ZlJuRmZNQm9UNnFqZHVRRU5DZ3QwVVVKSFNGOWZSbkZmTUNBQk1BQSUzRDABggEICAQYAiAAKACIAQGgAbTNqpCzoY8DqAEAsgEA&dark_theme=true&authuser=0",
        "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
        "isWebNativeShareAvailable": True
      }
    },
    "user": {
      "lockedSafetyMode": False
    },
    "request": {
      "useSsl": True,
      "consistencyTokenJars": [
        {
          "encryptedTokenJarContents": "AKreu9vw-RSxW_rrHdJn4Sfz4Rm6coVGwthtZK2SwKMGDLZwlG13bUfgeAXrQSy4LOchET1omT9Shy7Aese9bOcFGQytLX9L8YUwoEf2B7zIyFIyDIY3-Fqt5ug"
        }
      ],
      "internalExperimentFlags": []
    },
    "clickTracking": {
      "clickTrackingParams": "CCYQ8FsiEwjC5KmRs6GPAxX1dfUFHWWQIG7KAQRaGyCk"
    },
    "adSignalsInfo": {
      "params": [
        {
          "key": "dt",
          "value": "1755968160236"
        },
        {
          "key": "flash",
          "value": "0"
        },
        {
          "key": "frm",
          "value": "1"
        },
        {
          "key": "u_tz",
          "value": "330"
        },
        {
          "key": "u_his",
          "value": "13"
        },
        {
          "key": "u_h",
          "value": "720"
        },
        {
          "key": "u_w",
          "value": "360"
        },
        {
          "key": "u_ah",
          "value": "720"
        },
        {
          "key": "u_aw",
          "value": "360"
        },
        {
          "key": "u_cd",
          "value": "24"
        },
        {
          "key": "bc",
          "value": "31"
        },
        {
          "key": "bih",
          "value": "1612"
        },
        {
          "key": "biw",
          "value": "980"
        },
        {
          "key": "brdim",
          "value": "0,0,0,0,360,0,360,592,930,594"
        },
        {
          "key": "vis",
          "value": "1"
        },
        {
          "key": "wgl",
          "value": "True"
        },
        {
          "key": "ca_type",
          "value": "image"
        }
      ]
    }
  },
  "params": "Q2lrcUp3b1lWVU5yUm1WdlRsTnhXVlJoTjNSeWJqYzFWMDA1ZEhObkVndDBUbXRhYzFKWE4yZ3lZeEFCR0FRJTNE",
  "clientMessageId": "null",
  "richMessage": {
    "textSegments": [
      {
        "text": random_text
      }
    ]
  }
}
        try:
            response = requests.post(url, headers=headers, json=payload)
            print(f"[Batch {batch_number}] [{i+1}/{repeat_count}] Sent: {response.status_code}")
            time.sleep(5)
        except requests.RequestException as e:
            print(f"Error sending request: {e}")
    print(f"=== Batch {batch_number} complete, waiting 60 minutes ===\n")
    time.sleep(delay_between_batches)
    batch_number += 1
