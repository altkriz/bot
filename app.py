import os
import discord
from discord.ext import commands
from gradio_client import Client

# Initialize Gradio Client with the specified URL
redirect_uri = os.environ.get('REDIRECT_URI', 'https://bot-eta-swart.vercel.app/')
client_url = "https://bytedance-sdxl-lightning.hf.space/"
client = Client(client_url)

bot = commands.Bot(command_prefix='/')  # Define the bot's command prefix

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Define a command to generate images
@bot.command()
async def generate(ctx, *, prompt):
    inference_steps = '8-Step'  # You can customize this if needed
    result = client.predict(prompt, inference_steps, api_name="/generate_image")
    image_path = result.split("✔ ")[-1]
    await ctx.send(file=discord.File(image_path))

if __name__ == '__main__':
    bot_token = os.environ.get('DISCORD_BOT_TOKEN')
    bot.run(bot_token)
