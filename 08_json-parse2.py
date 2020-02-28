import urllib.parse
import requests
main_api="https://www.mapquestapi.com/directions/v2/route?"
orig="Washington"
dest="Baltimore"
key="9e30hHbYZO3R6Y9JeiYtdkA1XFT73Uoy"
url=main_api+urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
json_data=requests.get(url).json()
print("URL: "+(url))

json_data=requests.get(url).json()
json_status=json_data["info"]["statuscode"]

if json_status==0:
    print("API Status: "+str(json_status)+" = A successful route call.\n")
