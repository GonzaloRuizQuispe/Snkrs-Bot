import discord
from discord.ext import commands
from discord.utils import get
import mysql.connector
import time

#Discord
TOKEN = 'OTM5NjMxMzk0NDk2MzQ0MTU1.Yf7p7Q.gl6e2_PQ3wniC8iVgx0TRxEylsk'
BOT_PREFIX = 'd/'

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)
client = commands.Bot(command_prefix=BOT_PREFIX, intents = intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="Database"))
    print("Logged in as: " + client.user.name + "\n")

@client.event
async def on_member_join(ctx):
    autorole = discord.utils.get(ctx.guild.roles, name = '𝓝𝓔𝓦')
    await ctx.add_roles(autorole)

@client.command(pass_context = True) 
async def clear(ctx, num_parametro = 10):
    await ctx.channel.purge(limit = int(num_parametro))
    await ctx.send("Terminado")

@client.command(pass_context=True)
async def Help(ctx):
    await ctx.message.delete()
    await ctx.send(':mobile_phone:**Mis Comandos Son**:mobile_phone:\n```d/producto name_web <link_producto>\nd/seccion name_web <link_seccion>\nname_web : grid/etc```')

@client.command(pass_context=True)
@commands.has_role('𝓐𝓓𝓜𝓘𝓝𝓘𝓢𝓣𝓡𝓐𝓣𝓞𝓡')
async def producto(ctx,web,url):

    connection = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'Pool!Live45427752',
        db = 'snkrs'
        )

    if connection.is_connected():
        cursor = connection.cursor()

        cursor.execute("SELECT URL_WEB FROM productos_"+web+" WHERE URL_WEB='"+url[1:-1]+"'")
        cantidad_f = cursor.fetchone()

        if cantidad_f == None:
            cursor.execute("INSERT INTO productos_"+web+" (URL_WEB) VALUES ('"+url[1:-1]+"')")
            connection.commit()
            await ctx.message.delete()
            
            msg = await ctx.send("Este link fue agregado correctamente")
            time.sleep(5)
            await msg.delete()

        elif cantidad_f[0] == url[1:-1] :
            await ctx.message.delete()

            msg = await ctx.send("Ya Existe En La DB")
            time.sleep(5)
            await msg.delete()

@client.command(pass_context=True)
@commands.has_role('𝓐𝓓𝓜𝓘𝓝𝓘𝓢𝓣𝓡𝓐𝓣𝓞𝓡')
async def seccion(ctx,web,url):

    connection = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'Pool!Live45427752',
        db = 'snkrs'
        )

    if connection.is_connected():
        cursor = connection.cursor()

        cursor.execute("SELECT URL_Seccion FROM secciones_"+web+" WHERE URL_Seccion='"+url[1:-1]+"'")
        cantidad_f = cursor.fetchone()

        if cantidad_f == None:
            cursor.execute("INSERT INTO secciones_"+web+" (URL_Seccion) VALUES ('"+url[1:-1]+"')")
            connection.commit()
            await ctx.message.delete()

            msg = await ctx.send("Esta sección se agrego correctamente")
            time.sleep(5)
            await msg.delete()

        elif cantidad_f[0] == url[1:-1] :
            await ctx.message.delete()

            msg = await ctx.send("Esta seccion ya existe en la DB")
            time.sleep(5)
            await msg.delete()


client.run(TOKEN)