import amino
from BotAmino import *
from fancy_text import fancy
from BotAmino import BotAmino
import sys
from gtts import gTTS, lang
import emoji
import urllib.request
import time
from pathlib import Path
from google_trans_new import google_translator
import random
import os
from os import path
from random import uniform, choice, randint
email = "ravimourya526@yahoo.com"
password = "ravi1234oppo"
client = BotAmino(email=email, password=password)
vers = "2.0.4"
print(f"Bot Version = {vers}")

 
def tradlist(sub):
    sublist = []
    for elem in sub:
        try:
            sublist.append(client.get_from_code(f"http://aminoapps.com/u/{elem}").objectId)
            continue
        except Exception:
            pass
        sublist.append(elem)
    return sublist


whitefile = 'whitelist.txt'
whitelist = []
try:
    with open(whitefile, 'r') as file:
        for whitelistmember in file.readlines():
            whitelist.append(whitelistmember.strip())
except FileNotFoundError:
    a = open(whitefile, "w")
    a.close()


whitelist = tradlist(whitelist)


def is_whitelisted(data):
    if any(user in data.authorId for user in whitelist):
        return True
    data.subClient.send_message(chatId=data.chatId, message="You don't have permissions")
    return False


@client.command()
def hey(data):
    data.subClient.send_message(chatId=data.chatId, message="work status: True")


@client.command(condition=is_whitelisted)
def join(data):
    data.subClient.join_all_chat()
    data.subClient.send_message(data.chatId, "all chat joined")


@client.on_all()
def on_message(data):
    content = str(data.message).split()
    mtype = data.info.message.type

    if (mtype == 100) | (mtype == 109) | (mtype == 107) | (mtype == 110) | (mtype == 108) | (mtype == 111) | (mtype == 111):
        if mtype == 100 and not content:
            pass
        else:
            data.subClient.kick(chatId=data.chatId, userId=data.authorId, allowRejoin=False)
            data.subClient.send_message(data.chatId, f'MessageType {mtype} detected! Nickname: {data.author} | userId: {data.authorId} | messageId: {data.messageId}.')
            try:
                data.subClient.ban(data.authorId, f'MessageType {mtype} detected! Nickname: {data.author} | userId: {data.authorId} | messageId: {data.messageId}.')
            except Exception:
                pass


client.launch(False)
print("ready")
  		





print("ready\n")

@client.command("global")
def g(data):
																		mention=data.subClient.get_message_info(chatId=data.chatId,messageId=data.messageId).mentionUserIds
																		for user in mention:
																			link=client.get_from_id(user,0).shortUrl
																			data.subClient.send_message(data.chatId,message=link)											

@client.command("check")
def test(data):
    data.subClient.send_message(data.chatId, f"BOT IS ONLINE {data.author}")


@client.command("say")
def say_something(data):
    audio_file = f"soundfx.mp3"
    gTTS(text=data.message, lang='en', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)

@client.command("addtitle")
def give_a_title(data):
    data.subClient.add_title(data.authorId, data.message)
    data.subClient.send_message(chatId=data.chatId, message="Done!")
    
@client.command("removetitle")
def remove_title(data):
    data.subClient.remove_title(data.authorId, data.message)
    data.subClient.send_message(chatId=data.chatId, message="removed!")  
  

@client.command("help")
def vkidsnusovski(data):
    data.subClient.send_message(data.chatId, message="""
[C] I'm a bot vkidsnusovski! My Commands / My Commands
[C]! help [Bott Information!]
[C]! Zabiv [player1, player2] - game scoring without rules au🦁💪🏿
[C]! SNUS [User] - Make a Thermonuclear WC
[C]! Randemoji - team so that the bot threw 5 random stickers!
[C]! FancyText [Text] - team so that the bot decorated the text!
[C]! LUV [User - 1, User - 2] - Team To Check who sucks!
[C]! Google [Text] - a team to look for something in Google!
[C]! QS [Text] - team to ask a bot!
[C]! Joinallchats - team so that the bot entered all active chats.
[C]! Chatinfo - team to get a Chatid chat from the bot.
[C]! Text [Text] - write something on behalf of the bot
[C]! help2[Second part of the bots!""")

@client.command("help2")
def vkidsnusovski2(data):
	data.subClient.send_message(data.chatId, message="""
[C]! Follow - team to subscribe to you.
[C]! Unfollow - team so that the bot unsubscribed from you.
[C]! JOINCHAT [LINK TO CHAT / CHAT LINK] - A command to go to the selected chat by reference
[C]! Backgr - team to get a chat background!)
[C]! Staffask [Text] - a team to anonymously write through the bot all the curators, leaders.
[C]! SPERM - Secret Team
[C]! TRANSLATE [Text] - team to translate something into English
[C]! Stickmg - command to get a sticker as an image.
[C]! Reboot - team to restart the bot!
[C]! Msgtypes - command to get message types.
[C]! help3 [third part of the bots!
""") 

@client.command("help3")
def help3(data):
	data.subClient.send_message(data.chatId, message="""
[b]Command
[C]!check- for bot online or offline
[c]!profileinfo-for user information
[C]!global- for user global id (global) mention
[C]!say- (say)textmsg
[C]!addtitle- (title) if bot have leadership
[C]!removetitle - 
[C]!comment-(?)""") 


@client.on_member_leave_chat(["chatId"]) # the chatId is not necessary, put one if you want a specified chat only
def poka(data):
    data.subClient.send_message(data.chatId, f"Someone Left the group i hope he/she will be back Now  (RIP) {data.author} ")


############################Commands info in english!############################
#vkidsnusovski [Information about the bot!]
#vkidsnusovski2 [information about the bot2!]
#!zabiv [player1, player2] - Scoring game without rules  🦁 💪 🏿 command  author github.com/BrenoMartinsDeOliveiraVasconcelo
#!snus - [User] - A fun command for snus🥴
#!luv [User-1, User-2] - A command to Check who sucks who!
#!google [Text] - A command to search for something in google!
#!qs [Text] - Command to ask a question to the bot!
#!joinallchats-A command for the bot to log in to all active chats.
#!joinchat [Link to the chat/Chat Link] - Command for the bot to enter the selected chat using the link
#!chatinfo - Command for get chatId of the chat
#!follow - command to let the bot follow to you
#!backgr - Command for get background image of the chat!
#!staffask [Text] - A command to write anonymously through the bot to all curators and leaders.
#!sperm - secret command
#!translate [Text] - A command to translate something into English
#!stickmg - Command for convert sticker to image.
#
################################################commands/команды################################################
@client.command("luv")
def luv(data):
		msg = data.message + " null null "
		msg = msg.split(" ")
		msg[2] = msg[1]
		msg[1] = msg[0]
		try:
			data.subClient.send_message(chatId=data.chatId, message=f"Вероятность того что  {msg[1]} сосет у {msg[2]} равна {random.randint(0,100)}%")
		except:
			pass

@client.command("google")
def google(data):
    msg = data.message.split(" ")
    msg = '+'.join(msg)
    data.subClient.send_message(chatId=data.chatId, message=f"https://www.google.com/search?q={msg}")

@client.command("snus")
def snus(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[1] = msg[0]
	try:
		data.subClient.send_message(chatId=data.chatId, message=f"{msg[1]} сделал термоядерный снюсовый супер вкид овсянкасер🥴...")
	except:
		pass
#command author github.com/BrenoMartinsDeOliveiraVasconcelos
@client.command("zabiv")
def zabiv(data):
	msg = data.message + " null null "
	msg = msg.split(" ")
	try:
		rounds = int(msg[0])
	except (TypeError, ValueError):
		rounds = 5
		msg[2] = msg[1]
		msg[1] = msg[0]
		msg[0] = 5
	data.subClient.send_message(chatId=data.chatId, message=f"Начинается забив между  {msg[1]} и {msg[2]}...")
	win1 = 0
	win2 = 0
	round = 0
	agress = ''
	defens = ''
	for zabiv in range(0, rounds):
		round = round + 1
		data.subClient.send_message(chatId=data.chatId, message=f"[bc]Round/Раунд {round}/{rounds}")
		punch = randint(0, 1)
		if punch == 0:
			win1 = win1 + 1
			agress = msg[1]
			defens = msg[2]
		else:
			     	win2 = win2 + 1
			     	agress = msg[2]
			     	defens = msg[1]
		time.sleep(4)
		data.subClient.send_message(chatId=data.chatId, message=f"[ic] {agress} ударил👊🏿 {defens}!")
		if win1 > win2:
		  data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[1]} Выиграл в забиве!")
		elif win1 < win2:
		  	data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[2]} Выиграл в забиве!")
		elif win1 == win2:
		  		data.subClient.send_message(chatId=data.chatId, message=f"[iC]Ничья никто не выиграл кроме бабки в кедах!.")
#Команда для вопросов для бота
@client.command("qs")
def qs(data):
	lis = ['Возможно', 'Да', 'Нет', 'Конечно', 'Наверное']
	msg = data.message + "null?"
	msg = data.message.split(" ")
	data.subClient.send_message(chatId=data.chatId, message=str(random.choice(lis)))

@client.command("sperm")
def sperm(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[2] = msg[1]
	msg[1] = msg[0]
	try:
		data.subClient.send_message(chatId=data.chatId, message=f"{msg[1]} получил сперму в рот и был забит членом досмерти...")
	except:
		pass
#Команда чтобы бот заходил во все активные чаты
@client.command("joinallchats")
def joinallchats(data):
	print(type(data))
	data.subClient.send_message(chatId=data.chatId, message="We go to all active chats in the community ...")
	data.subClient.join_all_chat()
	data.subClient.send_message(chatId=data.chatId, message="Located in all active chats!")
@client.command("joinchat")
def joinchat(data):
	try:
		data.subClient.send_message(chatId=data.chatId, message="Заходим в выбранный чат")
		data.subClient.join_chatroom(data.message)
		data.subClient.send_message(chatId=data.chatId, message="Зашли в выбранный чат")
	except:
		data.subClient.send_message(chatId=data.chatId, message="Не удалось зайти в выбранный чат возможно бота кикнули!")
		pass

@client.command("follow")
def follow(data):
	try:
		data.subClient.send_message(data.chatId, f'following now {data.author}')
		data.subClient.follow_user(data.authorId)
	except:
		data.subClient.send_message(data.chatId, f'Failed to subscribe to {data.author}')
		pass

@client.command("chatinfo")
def chatinfo(data):
	data.subClient.send_message(data.chatId, f"chatId = {data.chatId}")

@client.command("backgr")
def backgr(data):
        image = data.subClient.get_chat_thread(chatId=data.chatId).backgroundImage
        if image:
            filename = path.basename(image)
            urllib.request.urlretrieve(image, filename)
            with open(filename, 'rb') as fp: data.subClient.send_message(data.chatId, file=fp, fileType="image")
            os.remove(filename)

@client.command("staffask")
def staffask(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[2] = msg[1]
	msg[1] = msg[0]
	data.subClient.ask_amino_staff(message=msg[1])
	data.subClient.ask_amino_staff(message=f"This message was sent to {data.author} / I'm a bot! Have a nice day")

@client.command("translate")
def translate(data):
    translator = google_translator()
    translate_text = translator.translate(data.message)
    data.subClient.send_message(data.chatId, f"Перевод: {translate_text}")

@client.command("stickmg")
def stickmg(data):
	info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
	reply_message = info.json['extensions']
	if reply_message:
	   image = info.json['extensions']['replyMessage']['extensions']['sticker']['icon']
	   filename = image.split("/")[-1]
	   filetype = image.split(".")[-1]
	   if filetype!="gif":
	   	filetype = "image"
	   	urllib.request.urlretrieve(image, filename)
	   	with open(filename, 'rb') as fp: data.subClient.send_message(data.chatId, file=fp, fileType="image")
	os.remove(filename)

#########Команда для изменения ника бота/Command to change the bot's nickname############
@client.command("nckname")
def nckname(data):
	data.subClient.subclient.edit_profile(nickname=data.message)
	data.subClient.send_message(chatId=data.chatId,message=f"Bot nickname changed to {data.message}")

@client.command("unfollow")
def unfollow(data):
    data.subClient.send_message(data.chatId, f'Unsubscribed from {data.author}')
    data.subClient.unfollow_user(data.authorId)

@client.command("welcome")
def welcome(data):
        data.subClient.set_welcome_message(data.message)
        data.subClient.send_message(data.chatId, "Welcome message changed ")
        
@client.command("randemoji")
def randemoji(data):
	lis = ['😰😨😱😓🤯', '😎🤡🥴🤕🌚', '🌝🥸👻🎃', '😺👹😈😇💩', '😛😉😊😘🥳', '🤣😀😆🥰🙂', '☺️😑🙃😶🤗', '🤩😋😔😌☺️', '🤫🤐🥺🙄🤔', '🧐😤😠😳🤯', '😓😥😩😖😵', '🌞🤮🤧🤒🎃', '😍😚🤭🥲😄', '😃😂🤣😭😰', '🤬😡😮😯😲', '🤓🤑🤠😇😷', '🥵🥶👺☠️👽', '😸😹😺😻😼', '😽🙀😿😾💀', '❤️🧡💛💚💙', '💜🤎🖤🤍♥️', '💘💝💖💗💓', '💞💕💌💟❣️', '💔💋👅👄👀', '🦾🦠🦷🏵️💐', '🧝🧙🧛🧟🥷', '😪😴🥱🤤🙄', '👿😈🔥⭐🌟', '🎊🎉🕳️💤💦', '🌜👻🤖💢⚡', '✨💫👁️🍂☀️', '🧠🫀🫁🩸🌡️', '👉👌🍺🍷👄', '🦁🐻🐼🐨🐹', '🐭🐷🐸🙉🐶', '🌌🌠🌉🌆🌃', '🕊️🦅🐦🦥🦏', '🐲🦖🐢🦮🐈', '🐐🦬🐖🐑🐆', '🦍🦧🐿️🦦🦈', '🐝🐠🐋🦋🐜', '🍔🍖🍗🌭🥪', '🥞🍳🫓🌮🍕', '🍉🍓🍒🫐🍎', '🧆🥙🥘🍜🦪', '🍧🍱🥟🍚🍢', '🍰🍙🍡🍣🍟', '🧇🥯🌯🥟🥡', '🍭🍩🍪🥮🍨', '🥗🍲🫕🍥🍿', '🥃🍾🍹🍸🍻', '🅿️🅾️🆘ℹ️🖕🏿', '🤏✋👊🙌👇', '👾🕹️🎮🎲🃏', '💵💴💶💷💰', '🇺🇸🇹🇨🇸🇻🇺🇦🇼🇸', '🏤🏣🏨🏥🏩']
	data.subClient.send_message(data.chatId, message=str(random.choice(lis)))

@client.command("fancytext")
def fancytext(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[1] = msg[0]
	data.subClient.send_message(data.chatId, message=fancy.light(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.bold(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.box(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.sorcerer(msg[1]))



@client.command("comment")
def comment_profile(data):
	data.subClient.comment(message="Painting from http://aminoapps.com/p/5kk6y48😎 I wish you all the best!", userId=data.authorId)
	data.subClient.send_message(data.chatId, message="The bot left you a painting on the wall!")

@client.command("msgtypes")
def msgtypes(data):
	data.subClient.send_message(data.chatId, message="""
[BC]--MESSAGETYPES--
[C]0 - BASE
[C]1 - STRIKE
[C]50 - UNSUPPORTED_MESSAGE
[C]57 - REJECTED_VOICE_CHAT
[C]58 - MISSED_VOICE_CHAT
[C]59 - CANCELED_VOICE_CHAT
[C]100 - DELETED_MESSAGE
[C]101 - JOINED_CHAT
[C]102 - LEFT_CHAT
[C]103 - STARTED_CHAT
[C]104 - CHANGED_BACKGROUND
[C]105 - EDITED_CHAT
[C]106 - EDITED_CHAT_ICON
[C]107 - STARTED_VOICE_CHAT
[C]109 - UNSUPPORTED_MESSAGE
[C]110 - ENDED_VOICE_CHAT
[C]113 - EDITED_CHAT_DESCRIPTION
[C]114 - ENABLED_LIVE_MODE
[C]115 - DISABLED_LIVE_MODE
[C]116 - NEW_CHAT_HOST
[C]124 - INVITE_ONLY_CHANGED
[C]125 - ENABLED_VIEW_ONLY
[C]126 - DISABLED_VIEW_ONLY
""")

@client.command("text")
def say_text(data):
	data.subClient.send_message(data.chatId, message=data.message)

@client.command("profileinfo")
def profileinfo(data):
	repa = data.subClient.get_user_info(data.authorId).reputation
	lvl = data.subClient.get_user_info(data.authorId).level
	crttime = data.subClient.get_user_info(data.authorId).createdTime
	followers = data.subClient.get_user_achievements(data.authorId).numberOfFollowersCount
	profilchange = data.subClient.get_user_info(data.authorId).modifiedTime
	commentz = data.subClient.get_user_info(data.authorId).commentsCount
	posts = data.subClient.get_user_achievements(data.authorId).numberOfPostsCreated
	followed = data.subClient.get_user_info(data.authorId).followingCount
	sysrole = data.subClient.get_user_info(data.authorId).role
	data.subClient.send_message(data.chatId, message=f"""
[C]Nickname: {data.author}
[C]UserId: {data.authorId}
[C]Account created time: {crttime}
[C]Last time the profile was changed: {profilchange}
[C]Reputation number: {repa}
[C]Account level: {lvl}
[C]Number of posts created in the profile: {posts}
[C]Number of comments on the profile wall: {commentz}
[C]The number of people you follow: {followed}
[C]Account followers: {followers}
[C]Account number in system: {sysrole}
	""")

client.launch()
################################################commands/команды################################################
time.sleep(10)
print("Bot started")

#socket
def restart():
    while True:
        time.sleep(120)
        count = 0
        for i in threading.enumerate():
            if i.name == "restart_thread":
                count += 1
        if count <= 1:
            print("Restart")
            client.socket.close()
            client.socket.start()

restart()
