import json
import random
import sqlite3

import requests

# ვიყენებთ request-ის მინიმუმ რამოდენიმე ფუნქციებს/ატრიბუტებს
res = requests.get('https://api.imgflip.com/get_memes')
print(res.content)
print(res.url, res.status_code, res.ok)

# ვონახავთ json ფორმატის მონაცემი json ფაილში
raw_memes = res.json()
memes = raw_memes['data']['memes']
with open('meme.json', 'w') as file:
    file.write(json.dumps(memes))

# ვბეჭდავთ მიმებს/ლინკებს
for i in range(0, 10):
    print(memes[i]['name'], memes[i]['url'])

# ვინაცავთ შექმნილ ინფორმაციას ბაზაში
with sqlite3.connect('database.db') as con:
    db = con.cursor()
    db.execute("create table if not exists memes(id integer primary key autoincrement, name text, url text)")
    query1 = "insert into memes(name, url) values(?,?)"
    random_meme = random.choice(memes)
    db.execute(query1, [random_meme['name'], random_meme['url']])
    con.commit()


