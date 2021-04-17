import discord
from discord.ext import commands
import os
import asyncio

client = commands.Bot(command_prefix = "-")


@client.command()
async def settime(ctx, timeInput,timeInput1, timeInput2):
    try:
  

        try:
            time = int(timeInput) + int(timeInput1) + int(timeInput2)
        except:
            convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}

            
              
           
         

            time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]] + int(timeInput1[:-1]) * convertTimeList[timeInput1[-1]] + int(timeInput2[:-1]) * convertTimeList[timeInput2[-1]]

        if time > 86400:
            await ctx.send("1 günden uzun süren zamanlayıcı yapamam")
            return
        if time <= 0:
            await ctx.send("Negatif sayı vermeyin")
            return
        embed=discord.Embed(title="Zamanlayıcı", description="Zaman")
        embed.add_field(name="Saat", value=timeInput, inline=False)
        embed.add_field(name="Dakika", value= timeInput1, inline=False)
        embed.add_field(name="Saniye", value= timeInput2, inline=True)                    
        
        await ctx.send(embed=embed)
        
        while True:
            try:
                await asyncio.sleep(1)
                time -= 1
                
                
                
                
                if time <= 0:
                    
                    await ctx.send(f"{ctx.author.mention} Süre doldu!")
                    break
            except:
        
                break
    
                embed=discord.Embed(title="Zamanlayıcı", description="Zaman")
                embed.add_field(name="Saat", value=time%3600, inline=False)
                embed.add_field(name="Dakika", value=time%60, inline=False)
                embed.add_field(name="Saniye", value=time, inline=True)
                await ctx.send(embed=embed)    
    except:
        await ctx.send(f"Lütfen saati, h m s şeklinde belirtiniz **{timeInput}**....")


@client.event
async def on_command_error(ctx,error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Lütfen saat, dakika, saniye şeklinde giriniz!")








client.run("ODMyNzA5MTA4NDE5MDAyMzc4.YHnuyg.jOycO4HNj39FzuHHmBYhkFvX2D4")
