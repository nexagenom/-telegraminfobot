import telebot, config, os, random, time

bot = telebot.TeleBot(config.token)

def wait(seconds):
    time.sleep(seconds)

def log(message,answer):
    from datetime import datetime
    l = '*-' * 30
    o = datetime.now()
    g = 'Message from {0} {1} (user id - {2}) \nText of message: {3} \n ---END---'.format(message.from_user.first_name,
                                                                                 message.from_user.last_name,
                                                                                 message.from_user.id,
                                                                                 message.text)
    s = answer
    print(l,'\n',o, '\n',g, '\n',s)
    logtofile = '{} \n {}  \n {}  \n {}'.format(l,o,g,s)
    logfile = open('log.log', 'a')
    logfile.write(str(logtofile))
    logfile.close

# Random photo from directory

def showphoto(message):
    portdir = os.listdir(config.portraitdir)
    rndfile = random.choice(portdir)
    img = open(config.portraitdir + '/' + rndfile, 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)
    img.close()
    wait(0.5)

@bot.message_handler(commands=["start"])
def handle_commands(message):
    usrmarkup = telebot.types.ReplyKeyboardMarkup()
    usrmarkup.row(config.menubuttons[0], config.menubuttons[1])
    usrmarkup.row(config.menubuttons[2], config.menubuttons[3])
    bot.send_sticker(message.from_user.id, config.constantstrickers[0])
    wait(2)
    bot.send_message(message.from_user.id, random.choice(config.startmessagesanswers), reply_markup=usrmarkup)
    wait(1)
    bot.send_sticker(message.from_user.id, config.constantstrickers[1])

@bot.message_handler(commands=["help"])
def handle_commands(message):
    bot.send_sticker(message.from_user.id, config.constantstrickers[2])
    wait(0.5)
    bot.send_message(message.from_user.id, config.helpcommandanswers)

@bot.message_handler(content_types=["sticker"])
def handle_message(message):
    stickerrnd = random.choice(config.randomizestickers)
    bot.send_chat_action(message.from_user.id, 'typing')
    wait(2)
    answer = random.choice(config.stickersanswers)
    bot.send_message(message.from_user.id, answer)
    bot.send_chat_action(message.from_user.id, 'typing')
    wait(3)
    bot.send_sticker(message.from_user.id, stickerrnd)
    answer = random.choice(config.stickersanswers2)
    bot.send_message(message.from_user.id, answer)
    log(message, answer)

@bot.message_handler(content_types=["text"])
def handle_message(message):
    if message.text.lower() in config.hellomessages and str(message.from_user.id) == config.forwardid:
        answer = random.choice(config.ownershelloanswers)
        wait(0.5)
        bot.send_chat_action(message.from_user.id, 'typing')
        wait(1)
        bot.send_message(message.from_user.id, answer)
        #log(message,answer)
    elif message.text.lower() in config.hellomessages:
        answer = random.choice(config.helloanswers)
        wait(0.5)
        bot.send_chat_action(message.from_user.id, 'typing')
        wait(1)
        bot.send_message(message.from_user.id, answer)
        #log(message,answer)
    elif message.text.lower() in config.byemessages:
        answer = random.choice(config.byeanswers)
        wait(0.5)
        bot.send_chat_action(message.from_user.id, 'typing')
        wait(1)
        bot.send_message(message.from_user.id, answer)
        #log(message,answer)
    elif message.text.lower() in config.helpmessages:
        answer = config.helpcommandanswers
        bot.send_sticker(message.from_user.id, config.constantstrickers[3])
        wait(0.5)
        bot.send_message(message.from_user.id, answer)
        #log(message,answer)
    elif message.text.lower() in config.sendmessagemessages
        answer = random.choice(config.sendmessageanswers)
        bot.send_chat_action(message.from_user.id, 'typing')
        wait(2)
        bot.send_message(message.from_user.id, answer)
        wait(0.8)
        bot.send_chat_action(message.from_user.id, 'typing')
        wait(0.5)
        bot.send_sticker(message.from_user.id, config.constantstrickers[4])
        #log(message,answer)
    elif message.text.lower() in config.contactmessages:
        answer = random.choice(config.contactsanswers)
        bot.send_chat_action(message.from_user.id, 'typing')
        wait(2)
        socmarkup = telebot.types.InlineKeyboardMarkup()
        vkontakte = telebot.types.InlineKeyboardButton(text=config.vktext, url=config.vkurl)
        instagram = telebot.types.InlineKeyboardButton(text=config.instatext, url=config.instaurl)
        socmarkup.add(vkontakte,instagram)
        bot.send_message(message.from_user.id, answer, reply_markup=socmarkup)
        #log(message,answer)
    elif message.text.lower() in config.portfoliomessages:
        answer = config.portfolioanswer
        wait(0.2)
        bot.send_message(message.from_user.id, answer)
        wait(1)
        portfoliomarkup = telebot.types.InlineKeyboardMarkup()
        portraits = telebot.types.InlineKeyboardButton(text=config.menubuttons[4], callback_data="more")
        enoughportraits = telebot.types.InlineKeyboardButton(text=config.menubuttons[5], callback_data="out")
        portfoliomarkup.add(portraits)
        portfoliomarkup.add(enoughportraits)
        showphoto(message)
        bot.send_message(message.from_user.id, config.constantmessages, reply_markup=portfoliomarkup)
        wait(3)
        #log(message,answer)

    else:
        answer = random.choice(config.ownerssendmessageanswers)
        wait(0.5)
        bot.send_chat_action(message.from_user.id, 'typing')
        wait(1)
        bot.send_message(message.from_user.id, answer)
        bot.forward_message(config.forwardid, message.from_user.id, message.message_id)
        #log(message, answer)

    @bot.callback_query_handler(func=lambda call: True)
    def inlinequery(call):
        if call.data == "more":
            txtmore = random.choice(config.callbackquerymoremessages)
            showphoto(message)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=txtmore)
            bot.send_message(message.from_user.id, config.constantmessages, reply_markup=portfoliomarkup)
        elif call.data == "out":
            txtmore = random.choice(config.callbackqueryoutmessages)
            msgout = random.choice(config.inlinequeryanswers)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=txtmore)
            bot.send_message(message.from_user.id, msgout)
        else:
            pass

    # будет вести лог всех сообщений
    log(message,answer)

bot.polling(none_stop = True, interval=0)