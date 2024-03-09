import discord
from discord.ext import commands
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests




#important variables :
#anime link getter :
link = ''
backuplink = ''
#weather resulte
weatherresult = ''
#thejoke :
joke = ''
#decrept_cod
Cc = []
dec=[]
Coded_message = ''
dcoded_message = ''

def DMK_DCod(message):
    global dcoded_message
    Cc = [*message]
    while len(Cc) > 31:
        try:
            for i in range(0,len(Cc)) :
                if i ==23:
                    dec.append(Cc[i])
                    pass
                if i ==25:
                    dec.append(Cc[i])
                    pass
                if i ==39:
                    dec.append(Cc[i])
                    pass
                if i ==50:
                    dec.append(Cc[i])
                    pass
                if i ==56:
                    dec.append(Cc[i])
                    pass

        except:
            pass
        del Cc[0:57]

    D = 4

    for i in range(0,len(dec)):
        try:
            if i == D:
                del dec[i]
                D +=4
        except:
            pass

    listToStr = ''.join(map(str, dec))
    dcoded_message = listToStr




def DMK_Cod(message):
	global Coded_message
	m = message
	def Convert(string):
		list1 = []
		list1[:0] = string
		return list1
	mt = Convert(m)
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+']
	try :
		for i in range(0,len(m)):
			random.shuffle(letters)
			for n in range(0,23):
				Cc.append(letters[n])
				if n == 22:
					Cc.append(mt[0])
			del mt[0]
			random.shuffle(letters)
			for n in range(1,2):
				Cc.append(letters[n])
				if n ==1:
					Cc.append(mt[0])
			del mt[0]
			random.shuffle(letters)
			for n in range(0,13):
				Cc.append(letters[n])
				if n ==12:
					Cc.append(mt[0])
			del mt[0]
			random.shuffle(letters)
			for n in range(0,10):
				Cc.append(letters[n])
				if n ==9:
					Cc.append(mt[0])
			del mt[0]
			random.shuffle(letters)
			for n in range(0,5):
				Cc.append(letters[n])
				if n ==4:
					Cc.append(mt[0])
	except IndexError:
		pass
	lr = ''.join(map(str, Cc))
	Coded_message = lr

#joke teller
def joke_telling():
    global joke
    url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"
    querystring = {"format":"json","idRange":"0-150"}
    headers = {
        "X-RapidAPI-Key": "5c2916c5b4mshc1148e672307234p15e3e4jsn3296dd895c8a",
        "X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    result = response.json()
    joke = f'{result["setup"]} {result["delivery"]}'

#weather finder
def findtemp(country , city):
    global weatherresult
    url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
    querystring = {"city":city,"country":country}
    headers = {
        "X-RapidAPI-Key": "5c2916c5b4mshc1148e672307234p15e3e4jsn3296dd895c8a",
        "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    try:
        temp_info = response.json()
        weatherresult = f'-min/max temp will be : {temp_info["min_temp"]}/{temp_info["max_temp"]} \n-could_pct : {temp_info["cloud_pct"]}% \n-humidity : {temp_info["humidity"]} \n-wind speed/degress : {temp_info["wind_speed"]}/{temp_info["wind_degrees"]}'
    except Exception as e:
        print(f"Error fetching weather: {e}")
        weatherresult = "Error fetching weather information."

#anime getter
def animelink(anime):
    global link
    global backuplink
    Links = []
    name = []
    #options = Options()
    #options.add_argument('headless')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', {
        "profile.default_content_setting_values.cookies": 1,
        "profile.block_third_party_cookies": False
    })
    #driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    driver.get("https://9animetv.to")
    main_page = driver.current_window_handle
    driver.find_element(By.NAME ,'keyword').send_keys(anime)
    searchB = driver.find_element(By.XPATH,('//*[@id="search-form"]/div/div'))
    ActionChains(driver).double_click(searchB).perform()
    driver.switch_to.window(main_page)
    ActionChains(driver).double_click(searchB).perform()
    url = driver.current_url
    re = requests.get(url)
    content = re.text
    soup = BeautifulSoup(content,'html.parser')
    for x in soup.find_all(name='a',class_='dynamic-name'):
        y = x.get('title')
        name.append(y)
    for x in soup.find_all(name='a',class_='film-poster-ahref'):
        y = x.get('href')
        Links.append(y)

    del name[len(Links):100]

    try :
        link = f'https://www.google.com/search?client=opera-gx&q={Links[1]}'
    except :
        link = 'NO RESULTE FOUND aktab al asam msagam ya m9wd'

#welcom list :
insults = ["hmar","m9wd","idiot","retard","no9sh","9ahba"]


#bot setup
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix='%',intents=intents)
@client.event
async def on_ready():
    print("bot online")

@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name} yal {insults[random.randint(0,len(insults)-1)]}'
        await guild.system_channel.send(to_send)

###################################################################COMMANDS#########################################################################################




@client.command()
async def hello(ctx):
    await ctx.send("hello")


@client.command()
async def getlink(ctx, *nameanime: str):
    await ctx.send('Searching...')
    animelink(' '.join(nameanime))
    await ctx.send(link)


@client.command()
async def weather(ctx , cityy:str,countryy:str):
    findtemp(country=countryy,city=cityy)
    await ctx.send(weatherresult)


@client.command()
async def clc(ctx, amount: int):
    if ctx.author.id == 553926442707189761 :
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Cleared {amount} messages.', delete_after=5)
    else :
        await ctx.send('Command invalide for you lil boy')


@client.command()
async def tell_joke(ctx):
    joke_telling()
    await ctx.send(joke)

@client.command()
async def codm(ctx, *message: str):
    DMK_Cod(' '.join(message))
    await ctx.send(Coded_message)

@client.command()
async def dcodm(ctx, *message: str):
    DMK_DCod(' '.join(message))
    await ctx.send(dcoded_message)




client.run(token)


