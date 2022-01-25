from sty import fg
from tabulate import tabulate
from pyfiglet import figlet_format
from configs import main_functions, menu_configs
print(f"""{fg(110)}
Script by DeLuvSushi
Github : https://github.com/deluvsushi""")
print(figlet_format("aminoblogwikiclique", font="slant", width=55))
print(tabulate(menu_configs.main_menu, tablefmt="fancy_grid"))
select = int(input("-- Select::: "))

if select == 1:
	title = input("-- Blogs Title::: "); content = input("-- Blogs Content::: ")
	main_functions.spam_blogs(title=title, content=content)

elif select == 2:
	title = input("-- Wiki's Title::: "); content = input("-- Wiki's Content::: ")
	main_functions.spam_wikis(title=title, content=content)
