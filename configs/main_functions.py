import amino

def spam_blogs(title: str, content: str):
	client = amino.Client()
	email = input("-- Email::: ")
	password = input("-- Password::: ")
	client.login(email=email, password=password)
	clients =  client.sub_clients(start=0, size=1000)
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
	sub_client = amino.SubClient(comId=com_id, profile=client.profile)
	while True:
		try:
			sub_client.post_blog(title=title, content=content)
			print("-- Blog is created!")
		except amino.lib.util.exceptions.VerificationRequired as e:
			print(f"-- VerificationRequired::: {e.args[0]['url]}")
			verification = input("-- Press enter after verification! ")
		except Exception as e:
			print(e)

def spam_wikis(title: str, content: str):
	client = amino.Client()    
	email = input("-- Email::: ")
	password = input("-- Password::: ")
	client.login(email=email, password=password)
	clients =  client.sub_clients(start=0, size=1000)
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
	sub_client = amino.SubClient(comId=com_id, profile=client.profile)
	while True:
		try:
			sub_client.post_wiki(title=title, content=content)
			print("-- Wiki is created!")
		except amino.lib.util.exceptions.VerificationRequired as e:
			print(f"-- VerificationRequired::: {e.args[0]['url]}")
			verification = input("-- Press enter after verification! ")
		except Exception as e:
			print(e)
