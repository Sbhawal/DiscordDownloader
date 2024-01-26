import os

filterByAuthor = False

# Reading config file
try:
    with open('config.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()
except Exception as e:
    print(e)
    exit(1)

filters ={}

for line in lines:
    if line.startswith('#'):
        continue
    line = line.strip()
    if line == '':
        continue
    if line.count('TOKEN'):
        TOKEN = line.split('=')[1].strip()
    elif line.count('GUILD_ID'):
        GUILD_ID = line.split('=')[1].replace(" ","")
    elif line.count('filterByAuthor'):
        filterByAuthor = line.split('=')[1].replace(" ","")
    elif line.count('STREAM'):
        STREAM = line.split('=')[1].replace(" ","")
    else:
        line = line.split('=')
        filters[line[0].strip()] = line[1].strip()

params = []

for i in filters:
    if not i.count('HAS') and filters[i].isdigit():
        params.append(str(i) + '=' + str(filters[i]))
    elif filters[i] == 'YES':
        params.append("has="+str(i.split('_')[1]))
    elif i.count('INCLUDE_NSFW'):
        params.append(str(i) + '=' + str(filters[i]))


BASE_URL = f"https://discord.com/api/v9/guilds/{GUILD_ID}/messages/search?"
FINAL_URL = BASE_URL + "&".join(params).strip().lower()