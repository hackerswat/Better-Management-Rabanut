import requests
import json
import datetime

# part 1 (login)

def login (mail, password):
    url = "https://api.betterchains.com/api/user/login"
    
    headers={"User-Agent": "Mozilla/5.0 (Linux; Android 9; Primo H8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
          "Accept": "application/json, text/plain, */*",
          "Accept-Language": "en-US,en;q=0.5",
          "Accept-Encoding": "gzip, deflate",
          "Content-Type": "application/json",
          "Content-Length": "128",
          "Origin": "https://login.betterchains.com",
          "Referer": "https://login.betterchains.com/",
          "Sec-Fetch-Dest": "empty",
          "Sec-Fetch-Mode": "cors",
          "Sec-Fetch-Site": "same-site",
          "Sec-Ch-Ua-Platform": "Android",
          "Sec-Ch-Ua": '''"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"''',
          "Sec-Ch-Ua-Mobile": "?1",
          "Te": "trailers",
          "Connection": "close"
          }


    data={"username":mail,
          "password":password,
          "client_app":"NG-FOH",
          "client_version":"3.3.11.50",
          "platform":"web"}


    response = requests.post(url, headers=headers, json=data)

    token = response.json()["token"]
    name  = response.json()["user"]["last_name"][::-1] + " " + response.json()["user"]["first_name"][::-1]

    if response.status_code == 200 and len(token) == 26:
        return token,name



# part 2 get last time submmited

def getHistory(token):
    url = "https://api.betterchains.com/api/forms/getHistory?formId=6929&formType=1&token=" + token
    
    headers={"User-Agent": "Mozilla/5.0 (Linux; Android 9; Primo H8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
          "Accept": "application/json, text/plain, */*",
          "Accept-Language": "en-US,en;q=0.5",
          "Accept-Encoding": "gzip, deflate",
          "Sec-Fetch-Dest": "empty",
          "Sec-Fetch-Mode": "cors",
          "Sec-Fetch-Site": "same-site",
          "Sec-Ch-Ua-Platform": "Android",
          "Sec-Ch-Ua": '''"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"''',
          "Sec-Ch-Ua-Mobile": "?1",
          "Te": "trailers",
          "Connection": "close"
          }



    response = requests.get(url, headers=headers)
    
    lastsubmitted = response.json()["data"][0]["dateISO"]
    
    if response.status_code == 200 :    
        return lastsubmitted
    

def getadvinfo(token):
    # gets date & time & unit
    url = "http://api.betterchains.com/api/user?token=" + token
    
    headers={"User-Agent": "Mozilla/5.0 (Linux; Android 9; Primo H8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Origin": "https://atal.betterchains.com",
            "Referer": "https://atal.betterchains.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-Ch-Ua-Platform": "Android",
            "Sec-Ch-Ua": '''"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"''',
            "Sec-Ch-Ua-Mobile": "?1",
            "Te": "trailers",
            "Connection": "close"
          }

    response = requests.get(url, headers=headers)

    date = response.json()["esign_accepted_date"]
    date = tuple(date.split(" "))
    time = date[1]
    date = date[0]

    unit = response.json()["branches"][0]["name"]
    unit = tuple(unit.split("|"))
    unit = unit[1] +" | " +  unit[0][::-1]

    # gets jewish date
    
    url = "http://www.hebcal.com/converter?cfg=json&gy=2023&gm=3&gd=22"

    headers={"User-Agent": "Mozilla/5.0 (Linux; Android 9; Primo H8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Origin": "https://atal.betterchains.com",
            "Referer": "https://atal.betterchains.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-Ch-Ua-Platform": "Android",
            "Sec-Ch-Ua": '''"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"''',
            "Sec-Ch-Ua-Mobile": "?1",
            "Te": "trailers",
          }
    
    response = requests.get(url, headers=headers)

    
    ildate = response.json()["hebrew"][::-1]

    print(unit)
    print(date)
    print(time)
    print(ildate)




# part 4 send the form


def sendForm(token):
    url = "https://api.betterchains.com/api/forms/public/6929?token=" + token + "&scenario=1&formType=1&dueTime=0"
    
    headers={"User-Agent": "Mozilla/5.0 (Linux; Android 9; Primo H8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
          "Accept": "application/json, text/plain, */*",
          "Accept-Language": "en-US,en;q=0.5",
          "Accept-Encoding": "gzip, deflate",
          "Content-Type": "application/json",
          "Content-Length": "28780",
          "Origin": "https://atal.betterchains.com",
          "Referer": "https://atal.betterchains.com/",
          "Sec-Fetch-Dest": "empty",
          "Sec-Fetch-Mode": "cors",
          "Sec-Fetch-Site": "same-site",
          "Sec-Ch-Ua-Platform": "Android",
          "Sec-Ch-Ua": '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"''',
          "Sec-Ch-Ua-Mobile": "?1",
          "Te": "trailers",
          "Connection": "close"
          }






    data={
    "showLogo": False,
    "captureLocation": True,
    "form_id": "6929",
    "form_name": "יומן כשרות -רבנות",
    "logoAlign": "",
    "form_fields": [
        {
            "field_id": 64,
            "field_hint": "",
            "field_title": "",
            "field_type": "richText",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "multiple_upload": True,
            "trustHtml": [],
            "accordionContentStatus": False
        },
        {
            "field_id": 111,
            "field_hint": "",
            "field_title": "תאריך עברי",
            "field_type": "date",
            "field_value": "03/23/2023",
            "field_required": False,
            "field_disabled": True,
            "accordionContentStatus": False,
            "to_show_he_il_calendar_in_rtl": True,
            "error": False,
            "isDirty": False,
            "hebrew_date_format": "כ״ט בַּאֲדָר תשפ״ג"
        },
        {
            "field_id": 0,
            "field_hint": "",
            "field_title": "תאריך",
            "field_type": "date",
            "field_value": "03/23/2023",
            "field_required": False,
            "field_disabled": True,
            "accordionContentStatus": False,
            "error": False,
            "isDirty": False
        },
        {
            "field_id": 3,
            "field_hint": "",
            "field_title": "שעה",
            "field_type": "time",
            "field_value": "01:31 PM",
            "field_required": False,
            "field_disabled": True,
            "accordionContentStatus": False
        },
        {
            "field_id": 84,
            "field_hint": "",
            "field_title": "יחידה",
            "field_type": "user_information",
            "field_value": "מ-שמעון בוסקילה | 6471",
            "field_required": False,
            "field_disabled": False,
            "source_field": [
                "branch_id"
            ],
            "part_of_system": "form_filler",
            "accordionContentStatus": False,
            "error": False
        },
        {
            "field_id": 74,
            "field_hint": "",
            "field_title": "שם הממלא",
            "field_type": "user_information",
            "field_value": "נתן ציוני",
            "field_required": False,
            "field_disabled": False,
            "source_field": [
                "first_name",
                "last_name"
            ],
            "part_of_system": "form_filler",
            "accordionContentStatus": False,
            "error": False
        },
        {
            "field_id": 4,
            "field_hint": "",
            "field_title": "האם קיימת הפרדה בין חלבי/בשרי/פרווה",
            "field_type": "checkbox",
            "field_value": [
                {
                    "option_id": 1,
                    "option_title": "אפייה",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "שטיפה",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "ירקות",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "לא רלוונטי מטבח לא פעיל",
                    "option_value": 5,
                    "isChecked": False
                }
            ],
            "field_required": True,
            "field_disabled": False,
            "field_options": [
                {
                    "option_id": 0,
                    "option_title": "חדרי בישול",
                    "option_value": 1,
                    "predefined": True,
                    "isChecked": True
                },
                {
                    "option_id": 1,
                    "option_title": "אפייה",
                    "option_value": 2,
                    "isChecked": True
                },
                {
                    "option_id": 2,
                    "option_title": "שטיפה",
                    "option_value": 3,
                    "isChecked": True
                },
                {
                    "option_id": 3,
                    "option_title": "ירקות",
                    "option_value": 4,
                    "isChecked": True
                },
                {
                    "option_id": 4,
                    "option_title": "לא רלוונטי מטבח לא פעיל",
                    "option_value": 5,
                    "isChecked": False
                }
            ],
            "accordionContentStatus": False,
            "isDirty": True,
            "error": False
        },
        {
            "field_id": 5,
            "field_hint": "",
            "field_title": "טיפול בירקות עליים טריים",
            "field_type": "note",
            "field_value": "שימוש בירקות עליים ללא חרקים, שטיפה ע\"י המשגיח",
            "field_required": False,
            "field_disabled": False,
            "accordionContentStatus": False
        },
        {
            "field_id": 65,
            "field_hint": "",
            "field_title": "סמן את הירקות ששטפת",
            "field_type": "checkbox",
            "field_value": [
                {
                    "option_id": 1,
                    "option_title": "חסה",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "חסה ערבית",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "עשבי תיבול יבשים/טריים",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "תמרים",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 5,
                    "option_title": "צימוקים",
                    "option_value": 6,
                    "isChecked": False
                },
                {
                    "option_id": 6,
                    "option_title": "משמש מיובש",
                    "option_value": 7,
                    "isChecked": False
                },
                {
                    "option_id": 7,
                    "option_title": "סלק אדום",
                    "option_value": 8,
                    "isChecked": False
                },
                {
                    "option_id": 8,
                    "option_title": "בצל יבש",
                    "option_value": 9,
                    "isChecked": False
                },
                {
                    "option_id": 9,
                    "option_title": "שום יבש",
                    "option_value": 10,
                    "isChecked": False
                },
                {
                    "option_id": 10,
                    "option_title": "",
                    "option_value": 11,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "שמיר",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "סלרי",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "אחר",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 5,
                    "option_title": "כוסברה",
                    "option_value": 6,
                    "isChecked": False
                }
            ],
            "field_required": False,
            "field_disabled": False,
            "field_options": [
                {
                    "option_id": 0,
                    "option_title": "כוסברה",
                    "option_value": 1,
                    "predefined": True,
                    "isChecked": True
                },
                {
                    "option_id": 1,
                    "option_title": "סלרי",
                    "option_value": 2,
                    "isChecked": True
                },
                {
                    "option_id": 2,
                    "option_title": "פטרוזיליה",
                    "option_value": 3,
                    "isChecked": True
                },
                {
                    "option_id": 3,
                    "option_title": "שמיר",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "אחר",
                    "option_value": 5,
                    "isChecked": False
                }
            ],
            "accordionContentStatus": False,
            "isDirty": True
        },
        {
            "field_id": 78,
            "field_hint": "",
            "field_title": "אחר-נא רשום את הירק האחר",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "text",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70,
            "error": False
        },
        {
            "field_id": 13,
            "field_hint": "",
            "field_title": "בדיקת ירקות ופירות",
            "field_type": "note",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "accordionContentStatus": False
        },
        {
            "field_id": 66,
            "field_hint": "",
            "field_title": "סמן ירקות שטופלו כשרותית",
            "field_type": "checkbox",
            "field_value": [
                {
                    "option_id": 1,
                    "option_title": "חסה",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "חסה ערבית",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "עשבי תיבול יבשים/טריים",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "תמרים",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 5,
                    "option_title": "צימוקים",
                    "option_value": 6,
                    "isChecked": False
                },
                {
                    "option_id": 6,
                    "option_title": "משמש מיובש",
                    "option_value": 7,
                    "isChecked": False
                },
                {
                    "option_id": 7,
                    "option_title": "סלק אדום",
                    "option_value": 8,
                    "isChecked": False
                },
                {
                    "option_id": 8,
                    "option_title": "בצל יבש",
                    "option_value": 9,
                    "isChecked": False
                },
                {
                    "option_id": 9,
                    "option_title": "שום יבש",
                    "option_value": 10,
                    "isChecked": False
                },
                {
                    "option_id": 10,
                    "option_title": "",
                    "option_value": 11,
                    "isChecked": False
                },
                {
                    "option_id": 10,
                    "option_title": "חציל שלם לטיגון",
                    "option_value": 11,
                    "isChecked": False
                }
            ],
            "field_required": False,
            "field_disabled": False,
            "field_options": [
                {
                    "option_id": 0,
                    "option_title": "בצל יבש",
                    "option_value": 1,
                    "predefined": True,
                    "isChecked": False
                },
                {
                    "option_id": 1,
                    "option_title": "גמבה",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "חציל שלם לאפייה בתנור(יש להוריד את הראש ולחצות לשתיים)",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "משמש מיובש",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "סלק אדום",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 5,
                    "option_title": "פלפל",
                    "option_value": 6,
                    "isChecked": False
                },
                {
                    "option_id": 6,
                    "option_title": "פלפל חריף",
                    "option_value": 7,
                    "isChecked": False
                },
                {
                    "option_id": 7,
                    "option_title": "צימוקים",
                    "option_value": 8,
                    "isChecked": False
                },
                {
                    "option_id": 8,
                    "option_title": "קליפת הלימון",
                    "option_value": 9,
                    "isChecked": False
                },
                {
                    "option_id": 9,
                    "option_title": "שום טרי/יבש",
                    "option_value": 10,
                    "isChecked": False
                },
                {
                    "option_id": 10,
                    "option_title": "תמרים",
                    "option_value": 11,
                    "isChecked": False
                }
            ],
            "accordionContentStatus": False
        },
        {
            "field_id": 24,
            "field_hint": "",
            "field_title": "ברירת קטניות",
            "field_type": "note",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "accordionContentStatus": False
        },
        {
            "field_id": 85,
            "field_hint": "",
            "field_title": "אורז כמות-ק\"ג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70
        },
        {
            "field_id": 93,
            "field_hint": "",
            "field_title": "אפונה כמות-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70
        },
        {
            "field_id": 92,
            "field_hint": "",
            "field_title": "בורגול כמות-קג",
            "field_type": "textfield",
            "field_value": "5",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70,
            "isDirty": True,
            "error": False
        },
        {
            "field_id": 98,
            "field_hint": "",
            "field_title": "גריסים כמות-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70
        },
        {
            "field_id": 103,
            "field_hint": "",
            "field_title": "גרנולה כמות-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70
        },
        {
            "field_id": 88,
            "field_hint": "",
            "field_title": "חומוס כמות-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70
        },
        {
            "field_id": 97,
            "field_hint": "",
            "field_title": "חיטה כמות-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70
        },
        {
            "field_id": 89,
            "field_hint": "",
            "field_title": "שעועית כמות-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70
        },
        {
            "field_id": 99,
            "field_hint": "",
            "field_title": "סולת כמות-קג",
            "field_type": "textfield",
            "field_value": "2",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70,
            "isDirty": True,
            "error": False
        },
        {
            "field_id": 96,
            "field_hint": "",
            "field_title": "עדשים ירוקות כמות-קג",
            "field_type": "textfield",
            "field_value": "5",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70,
            "isDirty": True,
            "error": False
        },
        {
            "field_id": 95,
            "field_hint": "",
            "field_title": "עדשים כתומות כמות-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70
        },
        {
            "field_id": 100,
            "field_hint": "",
            "field_title": "קוסקוס כמות-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70
        },
        {
            "field_id": 90,
            "field_hint": "",
            "field_title": "קטניות קפואות כמות-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70
        },
        {
            "field_id": 91,
            "field_hint": "",
            "field_title": "קטניות שימורים כמות-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70
        },
        {
            "field_id": 94,
            "field_hint": "",
            "field_title": "קינואה כמות-קג",
            "field_type": "textfield",
            "field_value": "1",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70,
            "isDirty": True,
            "error": False
        },
        {
            "field_id": 102,
            "field_hint": "",
            "field_title": "שומשום כמות-קג",
            "field_type": "textfield",
            "field_value": "5",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70,
            "isDirty": True,
            "error": False
        },
        {
            "field_id": 101,
            "field_hint": "",
            "field_title": "שיבולת שועל כמות-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70
        },
        {
            "field_id": 115,
            "field_hint": "",
            "field_title": "עדשים אדומות כמות-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "layout": "vertical",
            "labelWidth": 70,
            "accordionContentStatus": False
        },
        {
            "field_id": 114,
            "field_hint": "",
            "field_title": "שעועית מש כמות-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "layout": "vertical",
            "labelWidth": 70,
            "accordionContentStatus": False
        },
        {
            "field_id": 109,
            "field_hint": "",
            "field_title": "אחר-",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "text",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70,
            "error": False
        },
        {
            "field_id": 110,
            "field_hint": "",
            "field_title": "אחר כמות-",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "text",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70,
            "error": False
        },
        {
            "field_id": 36,
            "field_hint": "",
            "field_title": "ניפוי קמח",
            "field_type": "note",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "accordionContentStatus": False
        },
        {
            "field_id": 77,
            "field_hint": "",
            "field_title": "סוג הנפה",
            "field_type": "checkbox",
            "field_value": [
                {
                    "option_id": 1,
                    "option_title": "לא תקין",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "תקין",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "נפה חשמלית תעשייתית",
                    "option_value": 3,
                    "isChecked": False
                }
            ],
            "field_required": False,
            "field_disabled": False,
            "field_options": [
                {
                    "option_id": 0,
                    "option_title": "נפה ידנית",
                    "option_value": 1,
                    "predefined": True,
                    "isChecked": False
                },
                {
                    "option_id": 1,
                    "option_title": "נפה חשמלית ביתית",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "נפה חשמלית תעשייתית",
                    "option_value": 3,
                    "isChecked": False
                }
            ],
            "accordionContentStatus": False
        },
        {
            "field_id": 69,
            "field_hint": "ניפוי בנפה, הקמח המנופה ניתן לשמרו ל-24 שעות. בקירור עד 7 ימים  קמח בואקום – אינו צריך ניפוי כל עוד נשאר הואקום",
            "field_title": "סוג הקמח",
            "field_type": "checkbox",
            "field_value": [
                {
                    "option_id": 1,
                    "option_title": "קמח מלא",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "קמח מצה",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "קמח בואקום",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "קמח מצה",
                    "option_value": 4,
                    "isChecked": False
                }
            ],
            "field_required": False,
            "field_disabled": False,
            "field_options": [
                {
                    "option_id": 0,
                    "option_title": "קמח לבן",
                    "option_value": 1,
                    "predefined": True,
                    "isChecked": False
                },
                {
                    "option_id": 1,
                    "option_title": "קמח מלא",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "קמח בואקום",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "קמח מצה",
                    "option_value": 4,
                    "isChecked": False
                }
            ],
            "accordionContentStatus": False
        },
        {
            "field_id": 76,
            "field_hint": "",
            "field_title": "בדיקת תקינות נפת הקמח",
            "field_type": "checkbox",
            "field_value": [
                {
                    "option_id": 1,
                    "option_title": "לא תקין",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "תקין",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "נפה חשמלית תעשייתית",
                    "option_value": 3,
                    "isChecked": False
                }
            ],
            "field_required": False,
            "field_disabled": False,
            "field_options": [
                {
                    "option_id": 0,
                    "option_title": "תקין",
                    "option_value": 1,
                    "predefined": True,
                    "isChecked": False
                },
                {
                    "option_id": 1,
                    "option_title": "לא תקין",
                    "option_value": 2,
                    "isChecked": False
                }
            ],
            "accordionContentStatus": False
        },
        {
            "field_id": 86,
            "field_hint": "",
            "field_title": "כמות ניפוי הקמח-קג",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "text",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70,
            "error": False
        },
        {
            "field_id": 40,
            "field_hint": "",
            "field_title": "בדיקת אבקות / תבלינים",
            "field_type": "note",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "accordionContentStatus": False
        },
        {
            "field_id": 70,
            "field_hint": "יש לברור על משטח לבן",
            "field_title": "בדיקה ירקות עליים יבשים",
            "field_type": "checkbox",
            "field_value": [
                {
                    "option_id": 1,
                    "option_title": "קמח מלא",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "קמח מצה",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "רוזמרין יבש",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "כוסברה יבשה",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "אורגנו",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 5,
                    "option_title": "זעתר",
                    "option_value": 6,
                    "isChecked": False
                },
                {
                    "option_id": 6,
                    "option_title": "אבקת שום",
                    "option_value": 7,
                    "isChecked": False
                },
                {
                    "option_id": 7,
                    "option_title": "פפריקה מתוקה",
                    "option_value": 8,
                    "isChecked": False
                },
                {
                    "option_id": 8,
                    "option_title": "פלפל שחור על כל סוגיו",
                    "option_value": 9,
                    "isChecked": False
                },
                {
                    "option_id": 9,
                    "option_title": "פלפל אנגלי",
                    "option_value": 10,
                    "isChecked": False
                },
                {
                    "option_id": 10,
                    "option_title": "פלפל שאטה",
                    "option_value": 11,
                    "isChecked": False
                },
                {
                    "option_id": 11,
                    "option_title": "כורכום",
                    "option_value": 12,
                    "isChecked": False
                },
                {
                    "option_id": 12,
                    "option_title": "כמון",
                    "option_value": 13,
                    "isChecked": False
                },
                {
                    "option_id": 13,
                    "option_title": "אחר",
                    "option_value": 14,
                    "isChecked": False
                },
                {
                    "option_id": 6,
                    "option_title": "טימין",
                    "option_value": 7,
                    "isChecked": False
                },
                {
                    "option_id": 7,
                    "option_title": "אחר",
                    "option_value": 8,
                    "isChecked": False
                }
            ],
            "field_required": False,
            "field_disabled": False,
            "field_options": [
                {
                    "option_id": 0,
                    "option_title": "זעתר",
                    "option_value": 1,
                    "predefined": True,
                    "isChecked": False
                },
                {
                    "option_id": 1,
                    "option_title": "בזילקום יבש",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "רוזמרין יבש",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "כוסברה יבשה",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "אורגנו",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 5,
                    "option_title": "פטרוזיליה",
                    "option_value": 6,
                    "isChecked": False
                },
                {
                    "option_id": 6,
                    "option_title": "טימין",
                    "option_value": 7,
                    "isChecked": False
                },
                {
                    "option_id": 7,
                    "option_title": "אחר",
                    "option_value": 8,
                    "isChecked": False
                }
            ],
            "accordionContentStatus": False
        },
        {
            "field_id": 113,
            "field_hint": "",
            "field_title": "בדיקה ירקות עליים יבשים -אחר",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "text",
            "layout": "vertical",
            "labelWidth": 70,
            "accordionContentStatus": False,
            "error": False
        },
        {
            "field_id": 112,
            "field_hint": "",
            "field_title": "בדיקת חזותית",
            "field_type": "checkbox",
            "field_value": [
                {
                    "option_id": 1,
                    "option_title": "קמח מלא",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "קמח מצה",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "רוזמרין יבש",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "כוסברה יבשה",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "אורגנו",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 5,
                    "option_title": "זעתר",
                    "option_value": 6,
                    "isChecked": False
                },
                {
                    "option_id": 6,
                    "option_title": "אבקת שום",
                    "option_value": 7,
                    "isChecked": False
                },
                {
                    "option_id": 7,
                    "option_title": "פפריקה מתוקה",
                    "option_value": 8,
                    "isChecked": False
                },
                {
                    "option_id": 8,
                    "option_title": "פלפל שחור על כל סוגיו",
                    "option_value": 9,
                    "isChecked": False
                },
                {
                    "option_id": 9,
                    "option_title": "פלפל אנגלי",
                    "option_value": 10,
                    "isChecked": False
                },
                {
                    "option_id": 10,
                    "option_title": "פלפל שאטה",
                    "option_value": 11,
                    "isChecked": False
                },
                {
                    "option_id": 11,
                    "option_title": "כורכום",
                    "option_value": 12,
                    "isChecked": False
                },
                {
                    "option_id": 12,
                    "option_title": "כמון",
                    "option_value": 13,
                    "isChecked": False
                },
                {
                    "option_id": 13,
                    "option_title": "אחר",
                    "option_value": 14,
                    "isChecked": False
                }
            ],
            "field_required": False,
            "field_disabled": False,
            "field_options": [
                {
                    "option_id": 0,
                    "option_title": "אבקת מרק",
                    "option_value": 1,
                    "predefined": True,
                    "isChecked": False
                },
                {
                    "option_id": 1,
                    "option_title": "אבקת שום",
                    "option_value": 2,
                    "isChecked": True
                },
                {
                    "option_id": 2,
                    "option_title": "פפריקה מתוקה",
                    "option_value": 3,
                    "isChecked": True
                },
                {
                    "option_id": 3,
                    "option_title": "פלפל שחור על כל סוגיו",
                    "option_value": 4,
                    "isChecked": True
                },
                {
                    "option_id": 4,
                    "option_title": "פלפל אנגלי",
                    "option_value": 5,
                    "isChecked": True
                },
                {
                    "option_id": 5,
                    "option_title": "פלפל שאטה",
                    "option_value": 6,
                    "isChecked": True
                },
                {
                    "option_id": 6,
                    "option_title": "כורכום",
                    "option_value": 7,
                    "isChecked": True
                },
                {
                    "option_id": 7,
                    "option_title": "כמון",
                    "option_value": 8,
                    "isChecked": True
                },
                {
                    "option_id": 8,
                    "option_title": "אחר",
                    "option_value": 9,
                    "isChecked": False
                }
            ],
            "accordionContentStatus": False,
            "isDirty": True
        },
        {
            "field_id": 87,
            "field_hint": "",
            "field_title": "בדיקה חזותית -אחר",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "text",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70,
            "error": False
        },
        {
            "field_id": 45,
            "field_hint": "",
            "field_title": "בדיקת ביצים",
            "field_type": "note",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "accordionContentStatus": False
        },
        {
            "field_id": 108,
            "field_hint": "",
            "field_title": "כמות ביצים ששברת",
            "field_type": "textfield",
            "field_value": "30",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70,
            "isDirty": True,
            "error": False
        },
        {
            "field_id": 48,
            "field_hint": "",
            "field_title": "הפרשת חלה",
            "field_type": "note",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "accordionContentStatus": False
        },
        {
            "field_id": 81,
            "field_hint": "",
            "field_title": "בלילה רכה- נילושה במי פירות/מיועדת לטיגון יש להפריש בלא ברכה.- ציין כמות",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "text",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70,
            "error": False
        },
        {
            "field_id": 80,
            "field_hint": "",
            "field_title": "עיסה עבה- המיועדת לאפיה יש להפריש בברכה-ציין כמות",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "number",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70
        },
        {
            "field_id": 51,
            "field_hint": "",
            "field_title": "בדיקת סכו\"ם",
            "field_type": "note",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "accordionContentStatus": False
        },
        {
            "field_id": 72,
            "field_hint": "",
            "field_title": "האם ביצעת בדיקת סכו\"ם לפני כל ארוחה",
            "field_type": "radio",
            "field_value": 1,
            "field_required": True,
            "field_disabled": False,
            "calculate_by_additional_val": False,
            "field_options": [
                {
                    "option_id": 0,
                    "option_title": "כן",
                    "option_value": 1,
                    "option_additional_value": 0
                },
                {
                    "option_id": 1,
                    "option_title": "לא",
                    "option_value": 2,
                    "option_additional_value": 0
                },
                {
                    "option_id": 2,
                    "option_title": "לא רלוונטי המטבח לא פעיל",
                    "option_value": 3,
                    "option_additional_value": 0
                }
            ],
            "accordionContentStatus": False,
            "error": False,
            "isDirty": True
        },
        {
            "field_id": 82,
            "field_hint": "",
            "field_title": "ציין כמות של סכו\"ם מעורב שנמצא",
            "field_type": "textfield",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "input_type": "text",
            "accordionContentStatus": False,
            "layout": "vertical",
            "labelWidth": 70,
            "error": False
        },
        {
            "field_id": 104,
            "field_hint": "",
            "field_title": "האם בוצע רכש חוץ נא דווח בטופס רכש חוץ",
            "field_type": "radio",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "calculate_by_additional_val": False,
            "field_options": [
                {
                    "option_id": 0,
                    "option_title": "כן",
                    "option_value": 1,
                    "option_additional_value": 0
                },
                {
                    "option_id": 1,
                    "option_title": "לא",
                    "option_value": 2,
                    "option_additional_value": 0
                }
            ],
            "accordionContentStatus": False
        },
        {
            "field_id": 55,
            "field_hint": "",
            "field_title": "כלים חדשים",
            "field_type": "note",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "accordionContentStatus": False
        },
        {
            "field_id": 73,
            "field_hint": "",
            "field_title": "הוטבלו כלים חדשים ממתכת / זכוכית",
            "field_type": "radio",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "calculate_by_additional_val": False,
            "field_options": [
                {
                    "option_id": 0,
                    "option_title": "כן",
                    "option_value": 1,
                    "option_additional_value": 0
                },
                {
                    "option_id": 1,
                    "option_title": "לא",
                    "option_value": 2,
                    "option_additional_value": 0
                }
            ],
            "accordionContentStatus": False
        },
        {
            "field_id": 107,
            "field_hint": "",
            "field_title": "בדיקות ניקיון סוף יום",
            "field_type": "checkbox",
            "field_value": [
                {
                    "option_id": 1,
                    "option_title": "ניקיון חדר אפייה",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "ניקיון מכונת קמח",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "ניקיון מכונת אורז",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "ניקיון חדר כשרות",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 5,
                    "option_title": "רק ביום חמישי-בדיקת ניקיון פחי מזון מיכלי קטניות/קמח",
                    "option_value": 6,
                    "isChecked": False
                }
            ],
            "field_required": False,
            "field_disabled": False,
            "field_options": [
                {
                    "option_id": 0,
                    "option_title": "מרדדת הבצק",
                    "option_value": 1,
                    "predefined": True,
                    "isChecked": False
                },
                {
                    "option_id": 1,
                    "option_title": "חדר אפייה",
                    "option_value": 2,
                    "isChecked": False
                },
                {
                    "option_id": 2,
                    "option_title": "מכונת קמח",
                    "option_value": 3,
                    "isChecked": False
                },
                {
                    "option_id": 3,
                    "option_title": "מכונת אורז",
                    "option_value": 4,
                    "isChecked": False
                },
                {
                    "option_id": 4,
                    "option_title": "חדר כשרות",
                    "option_value": 5,
                    "isChecked": False
                },
                {
                    "option_id": 5,
                    "option_title": "רק ביום חמישי-בדיקת פחי מזון מיכלי קטניות/קמח",
                    "option_value": 6,
                    "isChecked": False
                }
            ],
            "accordionContentStatus": False
        },
        {
            "field_id": 59,
            "field_hint": "",
            "field_title": "תקלות/ אירועים מיוחדים",
            "field_type": "note",
            "field_value": "רשום האם הוכשרו כלים,\nהאם סימנת את הכלים ,\nהאם היתה תקלה כשרותית וכדו'",
            "field_required": False,
            "field_disabled": False,
            "accordionContentStatus": False
        },
        {
            "field_id": 61,
            "field_hint": "",
            "field_title": "פרט+ הערות(במצב שבו הגדוד באימון ולא מנהל יומן  אנא רשום את מיקום האימון)",
            "field_type": "textarea",
            "field_value": "",
            "field_required": False,
            "field_disabled": False,
            "accordionContentStatus": False,
            "error": False
        },
        {
            "field_id": 62,
            "field_hint": "",
            "field_title": "הוסף צילומים רלוונטים",
            "field_type": "file",
            "field_value": [],
            "field_required": False,
            "field_disabled": False,
            "multiple_upload": True,
            "accordionContentStatus": False,
            "error": False
        }
    ],
    "toFillOnce": 0,
    "isHTMLForm": False,
    "allowToDownloadPdfOnFE": True,
    "allowToDownloadOnlyDigitallySigned": False,
    "digitallySignOnSubmit": False,
    "selfProvisionTemplate": 0,
    "additional_title": "",
    "routeParams_id": 1,
    "type": "1",
    "submitted": True,
    "pdf_template_file": "",
    "pdf_template_coordinates_file": "",
    "apply_specific_pdf": 0,
    "pdf_result": "",
    "coordinates_result": "",
    "attachPdfToEmail": True,
    "includeInSignWizard": False,
    "is_editable_after_submitting": False,
    "shared_form": False,
    "checkModifyRules": 1,
    "checkSaveRules": 1,
    "checkSignRules": 1,
    "showReopenButton": False,
    "reopenedMode": False,
    "approvers": [],
    "lockSignButtonsTillEmployeeFromPickerSigns": 0,
    "canModifyApprovers": 0,
    "isDraft": 0,
    "realFormId": 6929,
    "allowToDownloadPdfOnFe": 0,
    "showCancelDraft": 0,
    "isEditableSingletonCopy": 0,
    "checkDownloadPdf": 0,
    "showRequestModifySingleton": 0,
    "nfc_lock": False
}


    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200 :    
        print("[+] eveything os ok")


try:
    token, name  = login("mail", "password") 

    if token:
        print("[+] login is successful")
        print("[+] user " + name)
except:
    raise Exception("[-] the email or password is in correct") 

try:
    lastsubmitted = getHistory(token)
except:
    raise Exception("[-] unable to get data from the server")

getadvinfo(token)


if lastsubmitted :
    if str(datetime.date.today()) != str(lastsubmitted):
        print("[+] last date submited " + lastsubmitted)
    else:
        raise Exception ("[-] the user already submited today ")

sendForm(token)