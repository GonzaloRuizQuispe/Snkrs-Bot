from typing_extensions import runtime
import discord
from discord.ext import commands
from discord.utils import get
import mysql.connector
from mysql.connector import Error

#Discord
TOKEN = 'OTM2MDE1ODc1MTQyNzEzMzg0.YfHCtg.h6RBcl7XXSyt_q9kJMRZaIvbYJQ'
BOT_PREFIX = 's/'

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)
client = commands.Bot(command_prefix=BOT_PREFIX, intents = intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Webs Snkrs"))
    print("Logged in as: " + client.user.name + "\n")

    channel = client.get_channel(936323586002657340)

    while True:
        try:    
            connection = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'Pool!Live45427752',
            db = 'snkrs'
            )

            ###
            if connection.is_connected():

                ###
                print("Conexion Exitosa SNKRS INDEX BOT")
                cursor = connection.cursor()
                
                cursor.execute("SELECT database();")
                registro = cursor.fetchone()
                print("Conectado a la BD:",registro,"\n")

                #Todas Las Web Que Tienen Registro - Esto Es Agregado Manual Mente Por El Programador
                Web = ["grid"]
                #----------------

                cursor.execute("SELECT * FROM productos_"+Web[0])
                cantidad_f = cursor.fetchall()

                ###
                for fila in cantidad_f:

                    if fila[5] == 'StockOn':
                        embed = discord.Embed(
                            title = ''+fila[1]+'',
                            colour = discord.Colour.orange(),
                            url = ''+fila[4]+''
                        )
                        embed.set_thumbnail(url=''+fila[3]+'')
                        embed.set_author(name='SNKRS-BOT',icon_url='https://w7.pngwing.com/pngs/672/449/png-transparent-sneakers-shoe-graphy-others-white-logo-monochrome.png')
                        embed.add_field(name='PRICE',value='$'+fila[2]+'',inline=False)
                        embed.add_field(name='SIZE',value=''+fila[6]+'',inline=False)
                        embed.set_footer(text='BY : ˞𝕮𝖍𝖆𝖈𝖍𝖆.𝕵𝖗˞#5812    ID : '+str(fila[0])+'   WEB : '+str(Web)+'')

                        cursor.execute("UPDATE productos_grid SET Cambios='Nuevo' WHERE ID_Producto="+str(fila[0]))
                        connection.commit()

                        await channel.send(embed=embed)
                    
                    elif fila[5] == 'Talles':
                        embed = discord.Embed(
                            title = ''+fila[1]+'',
                            colour = discord.Colour.orange(),
                            url = ''+fila[4]+''
                        )
                        embed.set_thumbnail(url=''+fila[3]+'')
                        embed.set_author(name='SNKRS-BOT',icon_url='https://w7.pngwing.com/pngs/672/449/png-transparent-sneakers-shoe-graphy-others-white-logo-monochrome.png')
                        embed.add_field(name='PRICE',value='$'+fila[2]+'',inline=False)
                        embed.add_field(name='SIZE',value=''+fila[6]+'',inline=False)
                        embed.set_footer(text='BY : ˞𝕮𝖍𝖆𝖈𝖍𝖆.𝕵𝖗˞#5812    ID : '+str(fila[0])+'   WEB : '+str(Web)+'')

                        cursor.execute("UPDATE productos_grid SET Cambios='Nuevo' WHERE ID_Producto="+str(fila[0]))
                        connection.commit()

                        await channel.send(embed=embed)

        except TypeError:
            print("Existe un error en el articulo\n",fila[0])
            pass
            ###
client.run(TOKEN)