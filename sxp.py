import requests
import time
import random

url = "https://www.youtube.com/youtubei/v1/live_chat/send_message?prettyPrint=false"

headers = {
  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
  'Content-Type': "application/json",
  'x-origin': "https://www.youtube.com",
  'x-youtube-bootstrap-logged-in': "true",
  'authorization': "SAPISIDHASH 1756118703_a7bbbbcc1ef8df7146bfdc826536cad4331a34f9_u SAPISID1PHASH 1756118703_a7bbbbcc1ef8df7146bfdc826536cad4331a34f9_u SAPISID3PHASH 1756118703_a7bbbbcc1ef8df7146bfdc826536cad4331a34f9_u",
  'x-youtube-client-name': "1",
  'x-youtube-client-version': "2.20250821.07.00",
  'x-goog-authuser': "0",
  'x-goog-visitor-id': "CgtMZGdyUmM2NkxTTSjy_LDFBjIKCgJJThIEGgAgSw%3D%3D",
  'origin': "https://www.youtube.com",
  'x-client-data': "CIS2yQEIo7bJAQipncoBCIa1ygEIjrrKARiFnMsB",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "same-origin",
  'sec-fetch-dest': "empty",
  'referer': "https://www.youtube.com/live_chat?continuation=0ofMyAOAARpeQ2lrcUp3b1lWVU5yUm1WdlRsTnhXVlJoTjNSeWJqYzFWMDA1ZEhObkVndDBUbXRhYzFKWE4yZ3lZeG9UNnFqZHVRRU5DZ3QwVG10YWMxSlhOMmd5WXlBQk1BQSUzRDABggEICAQYAiAAKACIAQGgAfTqwdTjpY8DqAEAsgEA&dark_theme=true&authuser=0",
  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
  'Cookie': "VISITOR_INFO1_LIVE=LdgrRc66LSM; VISITOR_PRIVACY_METADATA=CgJJThIEGgAgSw%3D%3D; PREF=f6=40000000&tz=Asia.Calcutta&f4=4000000&f5=30000; HSID=ACt-2HeLxiWJKhtXo; SSID=AOGmuF0-y7LvmWSg9; APISID=wd5w-HcOlelUwxBk/AFvnxZ2zv3CARPzsn; SAPISID=U5eljb9C8e0xWM_t/AOWRAd7x4FbZeSQt3; __Secure-1PAPISID=U5eljb9C8e0xWM_t/AOWRAd7x4FbZeSQt3; __Secure-3PAPISID=U5eljb9C8e0xWM_t/AOWRAd7x4FbZeSQt3; SID=g.a0000gg-FQJUONgnLNXB7oJ2mz8niKDwAMjAhgHfGTMc6yCCSMuoX8I0n4UzBQZzJMNDx4OaTAACgYKASgSARUSFQHGX2MivMhzKkZuGq4y2XVyb2zqpxoVAUF8yKqx4il277PnBef8lhE49YVd0076; __Secure-1PSID=g.a0000gg-FQJUONgnLNXB7oJ2mz8niKDwAMjAhgHfGTMc6yCCSMuoo36NeQm-5x_aLFH2X9RkQQACgYKATwSARUSFQHGX2Mi-HvceTe6TXROCUYygJcK6BoVAUF8yKr1HDFRU98ugaIJ53kEH1Hg0076; __Secure-3PSID=g.a0000gg-FQJUONgnLNXB7oJ2mz8niKDwAMjAhgHfGTMc6yCCSMuoFAz7a3oOHH6HfmytudnX1wACgYKAScSARUSFQHGX2MiLcQt6Y9GT5OL1Mh82KvxuxoVAUF8yKolIH1CA4uW6TDoUEVcfplB0076; YSC=85OOsHD76Uk; __Secure-ROLLOUT_TOKEN=CKzfwrb9oJCw8AEQpKD3qLGhjwMYi5L6peOljwM%3D; __Secure-1PSIDTS=sidts-CjUB5H03P0dXa8ucnA47FlcnJgsrOAuxMcLbRROkTqLwX18jkR76oqrSuqs60Y-rFXOapaw-xRAA; __Secure-3PSIDTS=sidts-CjUB5H03P0dXa8ucnA47FlcnJgsrOAuxMcLbRROkTqLwX18jkR76oqrSuqs60Y-rFXOapaw-xRAA; LOGIN_INFO=AFmmF2swRQIhAIR2Se3hg3uXnyll8RIFlh74_uMGUrTAGXycdHs4-Zm6AiBEoPudPsOQSdYZBAj7-WIVVNNcjoMORMB_kVtXMogcfA:QUQ3MjNmeFNjWVJRZXZQSU5ZQ2QwbTMycjFyOURXV1ZDM25tQWZ4Zlo3ek41MmtmTktKNlplWDBXVFN3bUFYQVN4eTdLQklOZFg1OERBdHRndHBMQW9UMXB0aHFzQXN3TS1sWjZCbnN0Z3RzYVlWaVJnOTNOdldDNVVua09pUUU3UGp1WF8xV3lIaklZd29DeW1iYmdKRW5CbkZFNXFxSWxR; ST-sbra4i=session_logininfo=AFmmF2swRQIgb0dMkE3Dmn96IE2yCK0GL9LsbspJv4y_Y4_e_2aMzsMCIQDJmt4Eib9vGeGPSVRoEG0sII_s0TzM2OMZdzIRrLpqOQ%3AQUQ3MjNmd0N3Mnk5Vl9HdWZaNzV0VXU0SDN1bEk5dXZVdDh6cHRjSXFYNWUwbkVNdWcyRVE0RmJFczdVZm9reVhKeFNvQ3ZoT0hYVk83aU84WjZ1N0tGdzEtQzJXRE5CRmVfNmotdlN0a1AwZS1HT3NfS1pySUZlY0xZQVA1TnV6RjZ1RTFleVpvdWJsNXlsQlQyc1lzYk9vN1lndkF1Q1pR; SIDCC=AKEyXzXfw281XyPazLdhjTj82a9475F-5fFzrMuVMAURyjwwcEHc5-V8En-EJrtXpjLu2SU4qg; __Secure-1PSIDCC=AKEyXzUfAhX8pa5Q8rDn3yD8GPFmEWr_r34SgnVlJ8eiF55Jns2ZD4CzzfYemugBWiy9V6aWheE; __Secure-3PSIDCC=AKEyXzXwHLlmDFupHILPzGjedLHMObWdYtPyplVO3OBibPfKKjnm7rPPwdpGyVZrGv9FxarW3A; ST-6m7wh8=session_logininfo=AFmmF2swRQIgb0dMkE3Dmn96IE2yCK0GL9LsbspJv4y_Y4_e_2aMzsMCIQDJmt4Eib9vGeGPSVRoEG0sII_s0TzM2OMZdzIRrLpqOQ%3AQUQ3MjNmd0N3Mnk5Vl9HdWZaNzV0VXU0SDN1bEk5dXZVdDh6cHRjSXFYNWUwbkVNdWcyRVE0RmJFczdVZm9reVhKeFNvQ3ZoT0hYVk83aU84WjZ1N0tGdzEtQzJXRE5CRmVfNmotdlN0a1AwZS1HT3NfS1pySUZlY0xZQVA1TnV6RjZ1RTFleVpvdWJsNXlsQlQyc1lzYk9vN1lndkF1Q1pR"
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
