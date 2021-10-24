import aminofix

def spam_blogs(title: str, content: str):
	client = aminofix.Client()
	client.login(email=input("Email >> "), password=input("Password >> "))
	clients =  client.sub_clients(start=0, size=1000)
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	com_Id = clients.comId[int(input("Select the community >> "))-1]
	sub_client =  aminofix.SubClient(comId=com_Id, profile=client.profile)
	while True:
		try:
			sub_client.post_blog(title=title, content=content)
			print("Created Blog...")
		except aminofix.lib.util.exceptions.VerificationRequired as e:
			print("VerificationRequired")
			verification_link = e.args[0]["url"]; print(verification_link)
			verification = input("Waiting for verification >> ")
		except Exception as e:	print(e)

def spam_wikis(title: str, content: str):
	client = aminofix.Client()    
	client.login(email=input("Email >> "), password=input("Password >> "))
	clients =  client.sub_clients(start=0, size=1000)
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	com_Id = clients.comId[int(input("Select the community >> "))-1]
	sub_client =  aminofix.SubClient(comId=com_Id, profile=client.profile)
	while True:
		try:
			sub_client.post_wiki(title=title, content=content)
			print("Created Wiki...")
		except aminofix.lib.util.exceptions.VerificationRequired as e:
			print("VerificationRequired")
			verification_link = e.args[0]["url"]; print(verification_link)
			verification = input("Waiting for verification >> ")
		except Exception as e:	print(e)
