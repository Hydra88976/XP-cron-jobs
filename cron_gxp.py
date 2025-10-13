import requests
import time
import random

url = "https://www.youtube.com/youtubei/v1/live_chat/send_message?prettyPrint=false"
headers = {
  'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/json",
  'x-goog-pageid': "115456890412822029709",
  'sec-ch-ua-platform': "\"Android\"",
  'authorization': "SAPISIDHASH 1752162109_fda9ea36e0370854e0a4ae4b56c10b931040eeb1_u SAPISID1PHASH 1752162109_fda9ea36e0370854e0a4ae4b56c10b931040eeb1_u SAPISID3PHASH 1752162109_fda9ea36e0370854e0a4ae4b56c10b931040eeb1_u",
  'sec-ch-ua-full-version-list': "",
  'sec-ch-ua': "\"Android WebView\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  'sec-ch-ua-bitness': "\"\"",
  'sec-ch-ua-model': "\"\"",
  'sec-ch-ua-mobile': "?1",
  'x-youtube-client-name': "1",
  'sec-ch-ua-wow64': "?0",
  'x-origin': "https://www.youtube.com",
  'x-youtube-client-version': "2.20250708.10.00",
  'sec-ch-ua-arch': "\"\"",
  'sec-ch-ua-full-version': "\"\"",
  'sec-ch-ua-form-factors': "",
  'x-youtube-bootstrap-logged-in': "true",
  'x-goog-visitor-id': "CgstVXYydkhNUWpOSSjivb_DBjIKCgJJThIEGgAgIA%3D%3D",
  'x-goog-authuser': "9",
  'sec-ch-ua-platform-version': "\"\"",
  'origin': "https://www.youtube.com",
  'x-requested-with': "mark.via.gp",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "same-origin",
  'sec-fetch-dest': "empty",
  'referer': "https://www.youtube.com/live_chat?continuation=0ofMyAOAARpeQ2lrcUp3b1lWVU5yUm1WdlRsTnhXVlJoTjNSeWJqYzFWMDA1ZEhObkVndDBUbXRhYzFKWE4yZ3lZeG9UNnFqZHVRRU5DZ3QwVG10YWMxSlhOMmd5WXlBQk1BQSUzRDABggEICAQYAiAAKACIAQGgAZq31JPQso4DqAEAsgEA&dark_theme=true&authuser=9&pageId=115456890412822029709",
  'accept-language': "en-IN,en-US;q=0.9,en;q=0.8",
  'priority': "u=1, i",
  'Cookie': "YSC=3v5j6B29oKw; VISITOR_INFO1_LIVE=-Uv2vHMQjNI; VISITOR_PRIVACY_METADATA=CgJJThIEGgAgIA%3D%3D; PREF=f6=40000000&tz=Asia.Calcutta&f4=4000000&f5=30000&f7=100; __Secure-ROLLOUT_TOKEN=CL_F9pC8s9r2OBD_5YGpjL6LAxjI7d66pbKOAw%3D%3D; __Secure-1PSIDTS=sidts-CjIB5H03P-yKxHhio5tyKDY1zTop1rc6K9EDwEEceL6Q4TugGZTUNJBcMlHKim6_Qr1xURAA; __Secure-3PSIDTS=sidts-CjIB5H03P-yKxHhio5tyKDY1zTop1rc6K9EDwEEceL6Q4TugGZTUNJBcMlHKim6_Qr1xURAA; HSID=Au2dy8UXXEqG-uO43; SSID=A53aMPt1BLC-Jqmlq; APISID=0YkCh9DTHOy9Ouw1/Ajt7gmxsFHxJOuV1G; SAPISID=6ubdrPZzf9kFH8IV/AoNETUNJ5GlaZxVU6; __Secure-1PAPISID=6ubdrPZzf9kFH8IV/AoNETUNJ5GlaZxVU6; __Secure-3PAPISID=6ubdrPZzf9kFH8IV/AoNETUNJ5GlaZxVU6; SID=g.a000ywhVlspJeb05iMqm2XZ4vm2e_oeVyAgz8Ym96eJuzuVSW2UL5fjs0OvlTzyx3-BI08TpuQACgYKAQkSARcSFQHGX2MiHecNvfMRz80rA2tQDCm0wxoVAUF8yKo2gVl9VN_6XoNNo7lWoiQR0076; __Secure-1PSID=g.a000ywhVlspJeb05iMqm2XZ4vm2e_oeVyAgz8Ym96eJuzuVSW2ULU8UEi6B2xe6YOBaeMd20RQACgYKAaoSARcSFQHGX2MiO4Q_EZoENO5cheVvrxW8MhoVAUF8yKoQMfvqdmOUBdzSHXL_abrT0076; __Secure-3PSID=g.a000ywhVlspJeb05iMqm2XZ4vm2e_oeVyAgz8Ym96eJuzuVSW2UL05IgJvt2kw-5EbyJdBC4bAACgYKAecSARcSFQHGX2MiIDfbFoN7KfyQ_liiY9i-dhoVAUF8yKqgE2EYSFE_Ky8zk_zI7ESf0076; LOGIN_INFO=AFmmF2swRAIgXXQ_9s6bk-14RQQ9EyzztjBcwoI5FUT_jKT6L_vwxXwCIDaBYlc9V1pGE8A3Dfw4j7Rg6i5_Ax0eEcHR92caTubF:QUQ3MjNmenFhTjRSYTFtUEdoVE01NG1DMXZtWkZSLVFBY3ZtTGRERExmQXR3U1lfcHY2SVRzdmhUZDNYelR0bVE4YVJ5akU5ejhSQUVJcHJvRVBMVmVrblZIMUZEMkk1Ynh6cXVFWGZ5MkFEYWM5Tkd1YXE3ZGFHemRtQlpMeXZHWlYzeGVVNDRkdnBLNmhtS0szd0lqaGQ1TWw2NF92T2R2MVR6TkJtcjNIcjBDU3JCTTM2MktISWJjVVBkeFJCZDkxbm04NHlNSnByWmV6c0h2b0Zkc24xeGl5RE1SN0Q2Zw==; SIDCC=AKEyXzWGgobgsfQV1c7g-FZLHXZ91MdcxkywhjmO4PkYpGzj7kx6SyWu2S8E0B17Z7tviLQG-A; __Secure-1PSIDCC=AKEyXzUP3Qfkmk2PTm2wDsDCKsj0g4hZHqUWRqe3UeiUXNztTqXVVyqsVXZ7wXIBP6TGT_yr0w; __Secure-3PSIDCC=AKEyXzXynJ3ujhnF8s-7dJ2YvaOEdrEsSPyFjihZW-oUYSk2hSzAiZUMDKkGYXbCM_w3CG0T0oU; ST-183jmdn=session_logininfo=AFmmF2swRAIgXXQ_9s6bk-14RQQ9EyzztjBcwoI5FUT_jKT6L_vwxXwCIDaBYlc9V1pGE8A3Dfw4j7Rg6i5_Ax0eEcHR92caTubF%3AQUQ3MjNmenFhTjRSYTFtUEdoVE01NG1DMXZtWkZSLVFBY3ZtTGRERExmQXR3U1lfcHY2SVRzdmhUZDNYelR0bVE4YVJ5akU5ejhSQUVJcHJvRVBMVmVrblZIMUZEMkk1Ynh6cXVFWGZ5MkFEYWM5Tkd1YXE3ZGFHemRtQlpMeXZHWlYzeGVVNDRkdnBLNmhtS0szd0lqaGQ1TWw2NF92T2R2MVR6TkJtcjNIcjBDU3JCTTM2MktISWJjVVBkeFJCZDkxbm04NHlNSnByWmV6c0h2b0Zkc24xeGl5RE1SN0Q2Zw%3D%3D; ST-6m7wh8=session_logininfo=AFmmF2swRQIhAPRIo99-F8ONWuoTxWQtGNubESspJJUzJyhsm8ba5TaRAiAEBhe_XHlZhuu8X9wwlB6AEhj5bTNZNzo9bXZ8CUek_A%3AQUQ3MjNmeGxPbE1IQVBqNzlqc0hmSVpXaHUxOUVaRmpaa1pDY0ZRLUZiN0k3RVNHZVJCbmkwT3F4SlpLaXczWTBKc00yUjV0YnVGbVlia3BDWTRSZHZsT09QU2VpSDNfMDVLVEw3Tjk3TXNRZko5d3REa0s2ZWJsZVEtTXJmOFdEQTJYRjZrSVZHSy1ELW9HRk4yRkxjTkJTTXJTY2l1WXFxZG1zUXZJRGlycElBWUxDWFFPV21mTEVQMERTSFc2V2VDa1VOcTlFcHNrN1BYdWJ2NVAwb2gxRE5qOEc5aUhrUQ%3D%3D"
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

#while True:
print(f"=== Batch {batch_number} starting ===")
for i in range(repeat_count):
   random_text = random.choice(texts)

   payload = {
      "context": {
        "client": {
          "hl": "en-GB",
          "gl": "IN",
          "remoteHost": "2405:201:4017:c9a5:78d2:ee4b:95e7:1bb0",
          "deviceMake": "",
          "deviceModel": "",
          "visitorData": "CgstVXYydkhNUWpOSSjivb_DBjIKCgJJThIEGgAgIA%3D%3D",
          "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36,gzip(gfe)",
          "clientName": "WEB",
          "clientVersion": "2.20250708.10.00",
          "osName": "Windows",
          "osVersion": "10.0",
          "originalUrl": "https://www.youtube.com/live_chat?continuation=0ofMyAOAARpeQ2lrcUp3b1lWVU5yUm1WdlRsTnhXVlJoTjNSeWJqYzFWMDA1ZEhObkVndDBUbXRhYzFKWE4yZ3lZeG9UNnFqZHVRRU5DZ3QwVG10YWMxSlhOMmd5WXlBQk1BQSUzRDABggEICAQYAiAAKACIAQGgAZq31JPQso4DqAEAsgEA&dark_theme=true&authuser=9&pageId=115456890412822029709",
          "screenPixelDensity": 2,
          "platform": "DESKTOP",
          "clientFormFactor": "UNKNOWN_FORM_FACTOR",
          "configInfo": {
            "appInstallData": "COK9v8MGEOmIzxwQmLnPHBDFu88cEKaasAUQk4bPHBD7tM8cEKCnzxwQmY2xBRCNrM8cEKSIgBMQibDOHBDgzbEFEJmYsQUQ7qDPHBDnr88cEOq7zxwQwr7PHBCr-M4cEOWuzxwQ2vfOHBDw4s4cEIKgzxwQl7XPHBDDioATEPyyzhwQjcywBRDYnM8cEKO2zxwQt-r-EhC-irAFEK-P_xIQr4bPHBDg4P8SEL2ZsAUQkLzPHBCuuc8cEL22rgUQ4IKAExCJ6K4FELWwzxwQvJzPHBCHrM4cENK2zxwQiIewBRDL0bEFEMzfrgUQ4tSuBRCzkM8cEJGM_xIQgo_PHBC45M4cEParsAUQlP6wBRDQpM8cENuvrwUQntCwBRC52c4cEM3RsQUQ0-GvBRDJ968FEPa6zxwQq5eAExCrnc8cEN68zhwQy8DPHBCBzc4cEIuvzxwQiOOvBRC72c4cENfBsQUQi4KAExCynf8SKjRDQU1TSWhVWm9MMndETkhrQnZQdDhRdVA5QTd2LXdiVl9BQzF6QWJCRTR5QkJjSmlIUWM9"
          },
          "screenDensityFloat": 2,
          "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
          "timeZone": "Asia/Calcutta",
          "browserName": "Chrome",
          "browserVersion": "116.0.0.0",
          "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
          "deviceExperimentId": "ChxOelV5TlRRM09EVTJOakkxTnpFeU1ERTRPUT09EOK9v8MGGOK9v8MG",
          "rolloutToken": "CL_F9pC8s9r2OBD_5YGpjL6LAxjI7d66pbKOAw%3D%3D",
          "screenWidthPoints": 400,
          "screenHeightPoints": 594,
          "utcOffsetMinutes": 330,
          "connectionType": "CONN_NONE",
          "memoryTotalKbytes": "2000000",
          "mainAppWebInfo": {
            "graftUrl": "https://www.youtube.com/live_chat?continuation=0ofMyAOAARpeQ2lrcUp3b1lWVU5yUm1WdlRsTnhXVlJoTjNSeWJqYzFWMDA1ZEhObkVndDBUbXRhYzFKWE4yZ3lZeG9UNnFqZHVRRU5DZ3QwVG10YWMxSlhOMmd5WXlBQk1BQSUzRDABggEICAQYAiAAKACIAQGgAZq31JPQso4DqAEAsgEA&dark_theme=true&authuser=9&pageId=115456890412822029709",
            "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
            "isWebNativeShareAvailable": False
          }
        },
        "user": {
          "lockedSafetyMode": False
        },
        "request": {
          "useSsl": True,
          "internalExperimentFlags": [],
          "consistencyTokenJars": []
        },
        "clickTracking": {
          "clickTrackingParams": "CCYQ8FsiEwiQ4N2V0LKOAxUQp9gFHey6BuU="
        },
        "adSignalsInfo": {
          "params": [
            {
              "key": "dt",
              "value": "1752162022876"
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
              "value": "3"
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
              "value": "1962"
            },
            {
              "key": "biw",
              "value": "1280"
            },
            {
              "key": "brdim",
              "value": "0,0,0,0,360,0,360,552,400,594"
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
      "params": "Q2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZeEFCR0FRJTNE",
      "clientMessageId": "CNms4JXQso4DFRCn2AUd7LoG5Q0",
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
    #print(f"=== Batch {batch_number} complete, waiting 60 minutes ===\n")
    #time.sleep(delay_between_batches)
    #batch_number += 1
