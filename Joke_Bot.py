import json

import requests
from discord.ext import commands


with open("config.json", "r") as f:
    config = json.loads(f.read())

# https://v2.jokeapi.dev/joke/Any?type=single
# https://v2.jokeapi.dev/joke/Programming?type=single&blacklistFlags=nsfw

class JokeAPI:
    def __init__(self):
        self.URL = 'https://v2.jokeapi.dev/joke/'
        self.allowed_categories = ['programming', 'miscellaneous', 'dark', 'pun', 'spooky', 'christmas', 'any']


    def get_joke(self, category, nsfw):
        if category not in self.allowed_categories:
            return 'No joke :('
        if nsfw == 'nsfw':
            url = self.URL + str(category).capitalize() + '?type=single&blacklistFlags=religious,political,racist,sexist,explicit'
        else:
            url = self.URL + str(category).capitalize() + '?type=single&blacklistFlags=nsfw'
        response = requests.get(url)
        content = response.json()
        return content['joke']

bot = commands.Bot(command_prefix='!')
joke_api = JokeAPI()

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def joke(ctx, arg_1=None, arg_2=None):
    if not arg_1:
        await ctx.send('Allowed categories are: ' + ', '.join(joke_api.allowed_categories) + '. \nAlso you can allow nsfw jokes by using nsfw argumnet.')
    else:
        await ctx.send(joke_api.get_joke(arg_1, arg_2))

print('Bot Started.')
bot.run(config['TOKEN'])

