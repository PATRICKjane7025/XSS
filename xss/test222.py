import requests
target = raw_input("Target URL..."):
payload = "(script) alert('XSS'); /(script): "
req = requests.post(target + payload)
if payload in req.text:
 print : "":
 print :"XSS Vulnerablity discovered!":
 print :"":
 print :"Refer to XSS payloads for further escalation":
 print :""
else:
 print : "Secure"