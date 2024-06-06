import requests
from datetime import datetime, date
from time import sleep
from random import randint, choice

class client():

    def __init__(self, mail: str, password: str):
        self.mail = mail
        self.password = password
    
    def login(self):

        url = "https://api.betterchains.com/api/user/login"

        headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 9; Primo H8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
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

        data = {"username": self.mail,
                "password": self.password,
                "client_app": "NG-FOH",
                "client_version": "3.3.11.50",
                "platform": "web"}
        try:
            response = requests.post(url, headers=headers, json=data)
            token = response.json()["token"]
            fname = response.json()["user"]["last_name"] + \
                " " + response.json()["user"]["first_name"]

            if response.status_code == 200 and len(token) == 26:
                self.token = token
                self.fname = fname
                return 0
            else:
                return 1
        except:
            return 1

    def getInfo(self):
        # gets date & time & unit
        url = "http://api.betterchains.com/api/user?token=" + self.token

        headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 9; Primo H8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
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

 
        unit = response.json()["branches"][0]["name"]


        # gets jewish date
        url = "http://www.hebcal.com/converter?cfg=json&gy=2023&gm=3&gd=22"

        headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 9; Primo H8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
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

        ildate = response.json()["hebrew"]

        current_date = str(date.today()).split("-")
        current_date = str(current_date[2] + "/" +  current_date[1] + "/" +  current_date[0])

        current_time = str(datetime.today().strftime("%I:%M %p"))

        self.time = current_time
        self.date = current_date
        self.unit = unit
        self.ildate = ildate

    def userChacks(self):
        url = "https://api.betterchains.com/api/forms/getHistory?formId=6929&formType=1&token=" + self.token

        headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 9; Primo H8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
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

        if response.status_code == 200:
            if str(date.today()) != str(lastsubmitted):
                return 0
            else:
                return 1

    def buildForm(self,form):
        url = "https://api.betterchains.com/api/forms/public/6929?token=" + self.token + "&scenario=1&formType=1&dueTime=0"

        headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 9; Primo H8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
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

        data = form

        self.request_data = (url, headers, data)

    def sendForm(self):
        response = requests.post(self.request_data[0], headers=self.request_data[1], json=self.request_data[2])
        if response.status_code == 200:
            return 0 
        else:
            return 1

class formBuilder():
    def __init__(self, ildate, date, time, unit, fname):
        
        self.ildate = ildate
        self.date = ildate
        self.date = date
        self.time = time
        self.unit = unit
        self.fname = fname

        ### in Kilos
        self.orez= "" 
        self.afuna = ""
        self.burgol = ""
        self.grisim = ""
        self.granola = ""
        self.homos = ""
        self.hita = ""
        self.shashoit = ""
        self.solet = ""
        self.adashim = ""
        self.koskos = ""
        self.kinoah = ""
        self.shomshom = ""
        self.shibolet_shoal = ""
        self.adashim_ktomote = ""
        self.adashim_adumote = ""
        self.shashoit_mash = ""
        self.baitzim = ""
        self.kemah = ""

        ## yes OR no checkbox

        ### kitchen Areas
        self.cooking_room = True
        self.baking_room = True
        self.washing_room = True
        self.vegetables_room = True

        ###  washed leaves

        self.kosbra = True
        self.selery = True
        self.petrozilia = True
        self.shamir = True

        ###  washed vegetables

        self.bazal = False
        self.gamba = False
        self.hatzil = False
        self.mishmish = False
        self.selek = False
        self.pealpel = False
        self.pealpel_harif = False
        self.tzimokim = False
        self.klipat_limon = False
        self.shum = False
        self.tmarim = False

        ### kemah

        self.napa_yadanit = False
        self.napa_hashmailt = False
        self.napa_hashmailt_tasytit = False
        self.bazeck = ""    # in KG

        ### kemah type

        self.kemah_lavan = False
        self.kemah_malea = False
        self.kemah_b_vakom = False
        self.kemah_maza = False

        ### check if the sieve OK

        self.napa_beseder = False
        self.napa_la_beseder = False

        ### check if powders OK

        self.zaatar_powder = False
        self.bazzilikom_powder = False
        self.rusmarin_powder = False
        self.kosbra_powder = False
        self.organo_powder = False
        self.petrozilia_powder = False
        self.timin_powder = False

        ### visual testing

        self.avkat_marak_tavlin = False
        self.avkat_shum_tavlin = False
        self.paprika_metoka_tavlin = False
        self.pealpel_shahor_tavlin = False
        self.pealpel_angli_tavlin = False
        self.pealpel_shate_tavlin = False
        self.kurkum_tavlin = False
        self.kamun_tavlin = False

        ### sakom visual testing
        self.sakom_visual_testing = True
        self.sakom_found_mixed = "" # number
        

        ### outside baying
        
        self.rehash_hootz = False

        ### tvilat keleam

        self.tvilat_keleam = ""

        ### and of the date\week cleaning

        self.meradedet_bazeck_ia_clean = False
        self.baking_room_is_clean = False
        self.kemah_machine_is_clean = False
        self.orez_machine_is_clean = False
        self.kashrut_room_is_clean = False
        self.pahi_kitnion_clean_only_in_thursday = False # only in thursday

    def randomValues(self):

        self.orez= str(choice(["", 10, 12, 20, 24, 30, 36, 40]))
        self.afuna = ""
        self.burgol = str(choice(["", "", "",  1 , 2, 3, 4, 5]))
        self.grisim = ""
        self.granola = ""
        self.homos = ""
        self.hita = ""
        self.shashoit = ""
        self.solet = ""
        self.adashim = ""
        self.koskos = str(choice(["","","","","","","",10, 12, 20, 24, 30, 36]))
        self.kinoah = str(choice(["", "", "", "", "", "", "", 1 , 2, 3]))
        self.shomshom = str(choice(["", "", "" ,1 , 2, 3]))
        self.shibolet_shoal = ""
        self.adashim_ktomote = ""
        self.adashim_adumote = ""
        self.shashoit_mash = ""
        self.baitzim = str(choice(["", 120 , 150, 240, 270, 330, 450, 540, 600]))
        self.kemah = str(choice(["","","","", "",10, 12, 20, 36]))

        self.cooking_room = False
        self.baking_room = False
        self.washing_room = False
        self.vegetables_room = False
        
        self.kosbra = choice([False, False, False, False, False, True])
        self.selery = choice([False, False, False, False, False, True])
        self.petrozilia = choice([False, False, False, False, False, True])
        self.shamir = choice([False, False, False, False, False, True])
        self.bazal = False
        self.gamba = False
        self.hatzil = False
        self.mishmish = False
        self.selek = False
        self.pealpel = False
        self.pealpel_harif = False
        self.tzimokim = False
        self.klipat_limon = False
        self.shum = False
        self.tmarim = choice([False, False, False, False, False, True])
        self.napa_yadanit = False
        
        self.napa_hashmailt = False
        self.napa_hashmailt_tasytit = False
        self.bazeck = "" 
        
        self.kemah_lavan = False
        self.kemah_malea = False
        self.kemah_b_vakom = False
        self.kemah_maza = False
        self.napa_beseder = False
        self.napa_la_beseder = False
        
        self.zaatar_powder = choice([False, False, False, False, False, True])
        self.bazzilikom_powder = choice([False, False, False, False, False, True])
        self.rusmarin_powder = choice([False, False, False, False, False, True])
        self.kosbra_powder = False
        self.organo_powder = False
        self.petrozilia_powder = False
        self.timin_powder = False
        self.avkat_marak_tavlin = choice([False, False, False, False, False, True])
        self.avkat_shum_tavlin = choice([False, False, False, False, False, True])
        self.paprika_metoka_tavlin = choice([True,True,True,False])
        self.pealpel_shahor_tavlin = choice([True,True,True,False])
        self.pealpel_angli_tavlin = False
        self.pealpel_shate_tavlin = False
        self.kurkum_tavlin = choice([True,True,True,False])
        self.kamun_tavlin = choice([True,True,True,False])
        self.sakom_visual_testing = choice([True,True,True,False])
        self.sakom_found_mixed = str(choice(["", "", "","", 1 , 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15]))
        
        self.rehash_hootz = False
        self.tvilat_keleam = ""
        
        self.meradedet_bazeck_is_clean = False
        self.baking_room_is_clean = False
        self.kemah_machine_is_clean = False
        self.orez_machine_is_clean = False
        self.kashrut_room_is_clean = False
        self.pahi_kitnion_clean_only_in_thursday = False

    def buildJsonForm(self):
        ## date chacking

        if self.sakom_visual_testing == True:
            self._sakom_found_mixed_final = self.sakom_found_mixed
            self._sakom_visual_testing_result = 1
        else:
            self._sakom_visual_testing_result = 2
            self._sakom_found_mixed_final = "0"

        if self.rehash_hootz == True:
            self._rehash_hootz_final = 0
        elif self.rehash_hootz == False:
            self._rehash_hootz_final = 1
        else:
            self._rehash_hootz_final = ""

        if self.tvilat_keleam == True:
            self._tvilat_keleam_final = 0
        elif self.tvilat_keleam == False:
            self._tvilat_keleam_final = 1
        else:
            self._tvilat_keleam_final = ""

        data = {
            "showLogo": False,
            "captureLocation": True,
            "form_id": "6929",
            "form   _name": "יומן כשרות -רבנות",
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
                    "field_value": self.date,
                    "field_required": False,
                    "field_disabled": True,
                    "accordionContentStatus": False,
                    "to_show_he_il_calendar_in_rtl": True,
                    "error": False,
                    "isDirty": False,
                    "hebrew_date_format": self.date
                },
                {
                    "field_id": 0,
                    "field_hint": "",
                    "field_title": "תאריך",
                    "field_type": "date",
                    "field_value": self.date,
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
                    "field_value": self.time,
                    "field_required": False,
                    "field_disabled": True,
                    "accordionContentStatus": False
                },
                {
                    "field_id": 84,
                    "field_hint": "",
                    "field_title": "יחידה",
                    "field_type": "user_information",
                    "field_value": self.unit,
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
                    "field_value": self.fname,
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
                            "isChecked": self.cooking_room
                        },
                        {
                            "option_id": 1,
                            "option_title": "אפייה",
                            "option_value": 2,
                            "isChecked": self.baking_room
                        },
                        {
                            "option_id": 2,
                            "option_title": "שטיפה",
                            "option_value": 3,
                            "isChecked": self.washing_room
                        },
                        {
                            "option_id": 3,
                            "option_title": "ירקות",
                            "option_value": 4,
                            "isChecked": self.vegetables_room
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
                            "isChecked": self.kosbra
                        },
                        {
                            "option_id": 1,
                            "option_title": "סלרי",
                            "option_value": 2,
                            "isChecked": self.selery
                        },
                        {
                            "option_id": 2,
                            "option_title": "פטרוזיליה",
                            "option_value": 3,
                            "isChecked": self.petrozilia
                        },
                        {
                            "option_id": 3,
                            "option_title": "שמיר",
                            "option_value": 4,
                            "isChecked": self.shamir
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
                            "isChecked": self.bazal
                        },
                        {
                            "option_id": 1,
                            "option_title": "גמבה",
                            "option_value": 2,
                            "isChecked": self.gamba
                        },
                        {
                            "option_id": 2,
                            "option_title": "חציל שלם לאפייה בתנור(יש להוריד את הראש ולחצות לשתיים)",
                            "option_value": 3,
                            "isChecked": self.hatzil
                        },
                        {
                            "option_id": 3,
                            "option_title": "משמש מיובש",
                            "option_value": 4,
                            "isChecked": self.mishmish
                        },
                        {
                            "option_id": 4,
                            "option_title": "סלק אדום",
                            "option_value": 5,
                            "isChecked": self.selek
                        },
                        {
                            "option_id": 5,
                            "option_title": "פלפל",
                            "option_value": 6,
                            "isChecked": self.pealpel
                        },
                        {
                            "option_id": 6,
                            "option_title": "פלפל חריף",
                            "option_value": 7,
                            "isChecked": self.pealpel_harif
                        },
                        {
                            "option_id": 7,
                            "option_title": "צימוקים",
                            "option_value": 8,
                            "isChecked": self.tzimokim
                        },
                        {
                            "option_id": 8,
                            "option_title": "קליפת הלימון",
                            "option_value": 9,
                            "isChecked": self.klipat_limon
                        },
                        {
                            "option_id": 9,
                            "option_title": "שום טרי/יבש",
                            "option_value": 10,
                            "isChecked": self.shum
                        },
                        {
                            "option_id": 10,
                            "option_title": "תמרים",
                            "option_value": 11,
                            "isChecked": self.tmarim
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
                    "field_value": self.orez,
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
                    "field_value": self.afuna,
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
                    "field_value": self.burgol,
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
                    "field_value": self.grisim,
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
                    "field_value": self.granola,
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
                    "field_value": self.homos,
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
                    "field_value": self.hita,
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
                    "field_value": self.shashoit,
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
                    "field_value": self.solet,
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
                    "field_value": self.adashim,
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
                    "field_value": self.adashim_ktomote,
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
                    "field_value": self.koskos,
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
                    "field_value": self.kinoah,
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
                    "field_value": self.shomshom,
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
                    "field_value": self.shibolet_shoal,
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
                    "field_value": self.adashim_adumote,
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
                    "field_value": self.shashoit_mash,
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
                            "isChecked": self.napa_yadanit
                        },
                        {
                            "option_id": 1,
                            "option_title": "נפה חשמלית ביתית",
                            "option_value": 2,
                            "isChecked": self.napa_hashmailt
                        },
                        {
                            "option_id": 2,
                            "option_title": "נפה חשמלית תעשייתית",
                            "option_value": 3,
                            "isChecked": self.napa_hashmailt_tasytit
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
                            "isChecked": self.kemah_lavan
                        },
                        {
                            "option_id": 1,
                            "option_title": "קמח מלא",
                            "option_value": 2,
                            "isChecked": self.kemah_malea
                        },
                        {
                            "option_id": 2,
                            "option_title": "קמח בואקום",
                            "option_value": 3,
                            "isChecked": self.kemah_b_vakom
                        },
                        {
                            "option_id": 3,
                            "option_title": "קמח מצה",
                            "option_value": 4,
                            "isChecked": self.kemah_maza
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
                            "isChecked": self.napa_beseder
                        },
                        {
                            "option_id": 1,
                            "option_title": "לא תקין",
                            "option_value": 2,
                            "isChecked": self.napa_la_beseder
                        }
                    ],
                    "accordionContentStatus": False
                },
                {
                    "field_id": 86,
                    "field_hint": "",
                    "field_title": "כמות ניפוי הקמח-קג",
                    "field_type": "textfield",
                    "field_value": self.kemah,
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
                            "isChecked": self.zaatar_powder
                        },
                        {
                            "option_id": 1,
                            "option_title": "בזילקום יבש",
                            "option_value": 2,
                            "isChecked": self.bazzilikom_powder
                        },
                        {
                            "option_id": 2,
                            "option_title": "רוזמרין יבש",
                            "option_value": 3,
                            "isChecked": self.rusmarin_powder
                        },
                        {
                            "option_id": 3,
                            "option_title": "כוסברה יבשה",
                            "option_value": 4,
                            "isChecked": self.kosbra_powder
                        },
                        {
                            "option_id": 4,
                            "option_title": "אורגנו",
                            "option_value": 5,
                            "isChecked": self.organo_powder
                        },
                        {
                            "option_id": 5,
                            "option_title": "פטרוזיליה",
                            "option_value": 6,
                            "isChecked": self.petrozilia_powder
                        },
                        {
                            "option_id": 6,
                            "option_title": "טימין",
                            "option_value": 7,
                            "isChecked": self.timin_powder
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
                            "isChecked": self.avkat_marak_tavlin
                        },
                        {
                            "option_id": 1,
                            "option_title": "אבקת שום",
                            "option_value": 2,
                            "isChecked": self.avkat_shum_tavlin
                        },
                        {
                            "option_id": 2,
                            "option_title": "פפריקה מתוקה",
                            "option_value": 3,
                            "isChecked": self.paprika_metoka_tavlin
                        },
                        {
                            "option_id": 3,
                            "option_title": "פלפל שחור על כל סוגיו",
                            "option_value": 4,
                            "isChecked": self.pealpel_shahor_tavlin
                        },
                        {
                            "option_id": 4,
                            "option_title": "פלפל אנגלי",
                            "option_value": 5,
                            "isChecked": self.pealpel_angli_tavlin
                        },
                        {
                            "option_id": 5,
                            "option_title": "פלפל שאטה",
                            "option_value": 6,
                            "isChecked": self.pealpel_shate_tavlin
                        },
                        {
                            "option_id": 6,
                            "option_title": "כורכום",
                            "option_value": 7,
                            "isChecked": self.kurkum_tavlin
                        },
                        {
                            "option_id": 7,
                            "option_title": "כמון",
                            "option_value": 8,
                            "isChecked": self.kamun_tavlin
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
                    "field_value": self.baitzim,
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
                    "field_value": self.bazeck,
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
                    "field_value": self._sakom_visual_testing_result,
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
                    "field_value": self._sakom_found_mixed_final,
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
                    "field_value": self._rehash_hootz_final,
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
                    "field_value": self._tvilat_keleam_final,
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
                            "isChecked": self.meradedet_bazeck_ia_clean
                        },
                        {
                            "option_id": 1,
                            "option_title": "חדר אפייה",
                            "option_value": 2,
                            "isChecked": self.baking_room_is_clean
                        },
                        {
                            "option_id": 2,
                            "option_title": "מכונת קמח",
                            "option_value": 3,
                            "isChecked": self.kemah_machine_is_clean
                        },
                        {
                            "option_id": 3,
                            "option_title": "מכונת אורז",
                            "option_value": 4,
                            "isChecked": self.orez_machine_is_clean
                        },
                        {
                            "option_id": 4,
                            "option_title": "חדר כשרות",
                            "option_value": 5,
                            "isChecked": self.kashrut_room_is_clean
                        },
                        {
                            "option_id": 5,
                            "option_title": "רק ביום חמישי-בדיקת פחי מזון מיכלי קטניות/קמח",
                            "option_value": 6,
                            "isChecked": self.pahi_kitnion_clean_only_in_thursday
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
        return data

    def safeBuildJsonForm(self):

        list_of_strings =[self.orez,
        self.afuna,
        self.burgol,
        self.grisim,
        self.granola,
        self.homos,
        self.hita,
        self.shashoit,
        self.solet,
        self.adashim,
        self.koskos,
        self.kinoah,
        self.shomshom,
        self.shibolet_shoal,
        self.adashim_ktomote,
        self.adashim_adumote,
        self.shashoit_mash,
        self.baitzim,
        self.kemah,
        self.bazeck,
        self.sakom_found_mixed,
        self.tvilat_keleam
        ]

        list_of_booleans = [self.cooking_room
        ,self.baking_room
        ,self.washing_room
        ,self.vegetables_room
        ,self.kosbra
        ,self.selery
        ,self.petrozilia
        ,self.shamir
        ,self.bazal
        ,self.gamba 
        ,self.hatzil
        ,self.mishmish
        ,self.selek
        ,self.pealpel
        ,self.pealpel_harif
        ,self.tzimokim
        ,self.klipat_limon
        ,self.shum
        ,self.tmarim
        ,self.napa_yadanit
        ,self.napa_hashmailt
        ,self.napa_hashmailt_tasytit
        ,self.kemah_lavan
        ,self.kemah_malea
        ,self.kemah_b_vakom
        ,self.kemah_maza
        ,self.napa_beseder
        ,self.napa_la_beseder
        ,self.zaatar_powder
        ,self.bazzilikom_powder
        ,self.rusmarin_powder
        ,self.kosbra_powder
        ,self.organo_powder
        ,self.petrozilia_powder
        ,self.timin_powder
        ,self.avkat_marak_tavlin
        ,self.avkat_shum_tavlin
        ,self.paprika_metoka_tavlin
        ,self.pealpel_shahor_tavlin
        ,self.pealpel_angli_tavlin
        ,self.pealpel_shate_tavlin
        ,self.kurkum_tavlin
        ,self.kamun_tavlin
        ,self.sakom_visual_testing
        ,self.rehash_hootz
        ,self.meradedet_bazeck_ia_clean
        ,self.baking_room_is_clean
        ,self.kemah_machine_is_clean
        ,self.orez_machine_is_clean
        ,self.kashrut_room_is_clean
        ,self.pahi_kitnion_clean_only_in_thursday
        ]
        
        for var in list_of_strings:
            if var != "":
                try:
                    str(int(var))
                except:
                    raise TypeError( var + " must be number")

        for var in list_of_booleans:
            if not isinstance(var, bool):
                raise TypeError( var + " must be boolean")
        
        return self.buildJsonForm()
        
creds = [("mail","password")]


for mail,password in creds:
    
    print("[*] " + str(date.today()))
    
    t_sleep = randint(0, 18000)
    print("[*] sleeping for " + str(t_sleep/60)[:4] + " minutes")
    sleep(t_sleep)


    a = client(mail, password)
    
    if a.login() != 0:
        print("[-] user or password incorrect")
        break
    
    a.getInfo()
    if a.userChacks() != 0:
        print("[-] " + a.fname[::-1] + " already submitted today")
        break

    form = formBuilder(a.ildate, a.date, a.time, a.unit, a.fname)
    form.randomValues()

    a.buildForm(form.safeBuildJsonForm())
    if a.sendForm() == 0:
        print("[*] the upload is successful")
    else:
        print("[-] error occurred")
    
print("-------end-of-day-------")
print("")
