from termcolor import colored
import pyfiglet
import requests
                 
print(colored("Welcome to Project 9","green",attrs=["blink"]))
print(colored(pyfiglet.figlet_format("Website-Scanner"),"cyan"))


website=input("Enter the name of website:")
new_url="http://"

if website[:7] != "http://":
	new_url+=website
	website=new_url

website_text="Target website"+website
print(colored(website_text,"yellow"))

print(colored("1)Basic scanning:","green"))
print(colored("2)Search through nmap","green"))
print(colored("3)Search the databse","green"))
print(colored("4)Download the website","green"))
print(colored("5)Exit","green"))


n=int(input("Choose:"))


if n ==1:
	try:
		data=requests.get(website,timeout=5)
		for i in data.headers:
			print(i,":",data.headers[i])
	except:
		print("Something went wrong (*_*)")
if n ==2:
	try:
		data=requests.get(website,timeout=5)
		for i in data:
			print(i)
	except:
		print("Something went wrong (*_*)")

