import discord

import config
from make_predictions import make_predictions

client = discord.Client()


@client.event
async def on_ready():
    print('started')


@client.event
async def on_message(message: discord.Message):
    preds = await make_predictions(message.content)
    await message.add_reaction(preds['toxic'])
    await message.add_reaction(preds['sentiment'])


client.run(config.token)
