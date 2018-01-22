import telebot, config, os, random, time, calendar, datetime


bot = telebot.TeleBot(config.token)
currentdates = {}

def wait(seconds):
    time.sleep(seconds)

def log(message,answer):

    def logfile():
        logtofile = '{} \n {}  \n {}  \n {}'.format(l, o, g, s)
        logishere = os.path.isfile('log.log')
        if logishere == False:
            logfile = open('log.log', 'w')
            logfile.write(str(logtofile))
            logfile.close()
        else:
             # log file size check
            logfilesize = os.path.getsize('log.log')
            if logfilesize >= 52428800:
                logfile = open('log.log', 'w')
                logfile.write(str(logtofile))
                logfile.close
            else:
                logfile = open('log.log', 'a')
                logfile.write(str(logtofile))
                logfile.close

    l = '*-' * 30
    o = datetime.datetime.now()
    g = 'Message from {0} {1} (user id - {2}) \nText of message: {3} \n ---END---'.format(message.from_user.first_name,
                                                                                 message.from_user.last_name,
                                                                                 message.from_user.id,
                                                                                 message.text)
    s = answer
    print(l,'\n',o, '\n',g, '\n',s)
    logfile()

# defining user markup menu
usrmarkup = telebot.types.ReplyKeyboardMarkup()
usrmarkup.row(config.menubuttons[0], config.menubuttons[1])
usrmarkup.row(config.menubuttons[2], config.menubuttons[3])
usrmarkup.row(config.menubuttons[6])

# Random photo from directory listed in config.py

def showphoto(message):
    portdir = os.listdir(config.portraitdir)
    rndfile = random.choice(portdir)
    img = open(config.portraitdir + '/' + rndfile, 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)
    img.close()
    wait(0.5)

def calendarcreation(y,m):
    calendarmarkup = telebot.types.InlineKeyboardMarkup()
    data = []
    data.append(telebot.types.InlineKeyboardButton(calendar.month_name[m]+" "+str(y), callback_data="nope"))
    calendarmarkup.row(*data)
    daysoftheweek = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    data = []
    for day in daysoftheweek:
        data.append(telebot.types.InlineKeyboardButton(day, callback_data="nope"))
    calendarmarkup.row(*data)
    newcalendar = calendar.monthcalendar(y,m)
    for week in newcalendar:
        data = []
        for day in week:
            if day == 0:
                data.append(telebot.types.InlineKeyboardButton(config.calendarsbuttons[1], callback_data="nope"))
            else:
                data.append(telebot.types.InlineKeyboardButton(str(day), callback_data="calday-" + str(day)))
        calendarmarkup.row(*data)
    data = []
    data.append(telebot.types.InlineKeyboardButton(config.calendarsbuttons[0], callback_data="prevmon"))
    data.append(telebot.types.InlineKeyboardButton(config.calendarsbuttons[1], callback_data="nope"))
    data.append(telebot.types.InlineKeyboardButton(config.calendarsbuttons[2], callback_data="nextmon"))
    calendarmarkup.row(*data)
    return calendarmarkup


@bot.message_handler(commands=["start"])
def handle_commands(message):
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
    elif message.text.lower() in config.sendmessagemessages:
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
        bot.send_message(message.from_user.id, config.constantmessages[0], reply_markup=portfoliomarkup)
        wait(3)
        #log(message,answer)
    elif message.text.lower() in config.photosessiongsighup:
        nowdate = datetime.datetime.now()
        date = (nowdate.year, nowdate.month)
        currentdates[message.from_user.id] = date
        calmarkup = calendarcreation(nowdate.year, nowdate.month)
        bot.send_chat_action(message.from_user.id, 'typing')
        wait(1)
        answer = config.photosessiongsighupwarning
        bot.send_message(message.from_user.id, answer, parse_mode='HTML')
        wait(3)
        answer = random.choice(config.photosessiongsighupanswers)
        bot.send_chat_action(message.from_user.id, 'typing')
        bot.send_message(message.from_user.id, answer, reply_markup=calmarkup)
    elif message.text.lower() in config.adminrequests and str(message.from_user.id) == config.adminid:
        answer = random.choice(config.adminmessage)
        adminmarkup = telebot.types.InlineKeyboardMarkup()
        recievelog = telebot.types.InlineKeyboardButton(config.admininlinebuttons[0], callback_data="recievelog")
        admin_quit = telebot.types.InlineKeyboardButton(config.admininlinebuttons[1], callback_data="admin_quit")
        adminmarkup.add(recievelog,admin_quit)
        wait(1)
        bot.send_message(message.from_user.id, answer, reply_markup=adminmarkup)
    elif message.text.lower() in config.adminrequests:
        answer = random.choice(config.nonadminmessage)
        if answer == config.nonadminmessage[4]:
            stickerrnd = random.choice(config.randomizestickers)
            bot.send_chat_action(message.from_user.id, 'typing')
            wait(1)
            bot.send_message(message.from_user.id, answer)
            wait(1)
            bot.send_chat_action(message.from_user.id, 'typing')
            bot.send_sticker(message.from_user.id, stickerrnd)
        else:
            bot.send_chat_action(message.from_user.id, 'typing')
            wait(1)
            bot.send_message(message.from_user.id, answer)

    else:
        answer = random.choice(config.ownerssendmessageanswers)
        wait(0.5)
        bot.send_chat_action(message.from_user.id, 'typing')
        wait(1)
        bot.send_message(message.from_user.id, answer)
        bot.forward_message(config.forwardid, message.from_user.id, message.message_id)
        #log(message, answer)

    @bot.callback_query_handler(func=lambda call: call.data[0:7] == "calday-")
    def calday(call):
        svdt = currentdates[call.message.chat.id]
        answer = config.constantmessages[1]
        if svdt is not None:
            day = call.data[7:]
            date = datetime.date(int(svdt[0]), int(svdt[1]), int(day))
            bot.send_chat_action(call.message.chat.id, 'typing')
            wait(1)
            bot.answer_callback_query(call.id, text=answer + str(date))
            bot.send_chat_action(call.message.chat.id, 'typing')
            wait(1)
            bot.send_message(call.message.chat.id, config.constantmessages[2], parse_mode="HTML")
            bot.forward_message(config.forwardid, call.message.chat.id, message.message_id, disable_notification=True)
            bot.send_message(config.forwardid, config.constantmessages[3] + str(date), disable_notification=True)
        else:
            pass

    @bot.callback_query_handler(func=lambda call: True)
    def inlinequery(call):
        if call.data == "more":
            portfoliomarkup = telebot.types.InlineKeyboardMarkup()
            portraits = telebot.types.InlineKeyboardButton(text=config.menubuttons[4], callback_data="more")
            enoughportraits = telebot.types.InlineKeyboardButton(text=config.menubuttons[5], callback_data="out")
            portfoliomarkup.add(portraits)
            portfoliomarkup.add(enoughportraits)
            txtmore = random.choice(config.callbackquerymoremessages)
            showphoto(message)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=txtmore)
            bot.send_message(call.message.chat.id, config.constantmessages[0], reply_markup=portfoliomarkup)
        elif call.data == "out":
            txtmore = random.choice(config.callbackqueryoutmessages)
            msgout = random.choice(config.inlinequeryanswers)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=txtmore)
            bot.send_message(call.message.chat.id, msgout)
        elif call.data == "nextmon":
            svdt = currentdates[call.message.chat.id]
            if svdt is not None:
                y, m = svdt
                m += 1
                if m > 12:
                    m = 1
                    y += 1
                date = (y, m)
                currentdates[call.message.chat.id] = date
                calmarkup = calendarcreation(y, m)
                answer = random.choice(config.photosessiongsighupanswers)
                bot.edit_message_text(answer, call.from_user.id, call.message.message_id, reply_markup=calmarkup)
                bot.answer_callback_query(call.id, text="")
            else:
                pass
        elif call.data == "prevmon":
            svdt = currentdates[call.message.chat.id]
            if svdt is not None:
                y, m = svdt
                m -= 1
                if m < 1:
                    m = 12
                    y -= 1
                date = (y, m)
                currentdates[call.message.chat.id] = date
                calmarkup = calendarcreation(y, m)
                answer = random.choice(config.photosessiongsighupanswers)
                bot.edit_message_text(answer, call.from_user.id, call.message.message_id, reply_markup=calmarkup)
                bot.answer_callback_query(call.id, text="")
            else:
                pass
        elif call.data == "nope":
            bot.answer_callback_query(call.id, text="")
        elif call.data == "recievelog" and str(message.from_user.id) == config.adminid:
            txt = config.adminanswers[0]
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
            logfile = open('log.log', 'rb')
            bot.send_message(call.message.chat.id, txt)
            bot.send_chat_action(call.message.chat.id, 'upload_document')
            wait(2)
            bot.send_document(call.message.chat.id, logfile)
            logfile.close
            bot.answer_callback_query(call.id, text="")
        elif call.data == "admin_quit" and str(message.from_user.id) == config.adminid:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
            bot.send_message(call.message.chat.id, 'Пока', reply_markup=usrmarkup)
            bot.answer_callback_query(call.id, text="")
        else:
            pass

    # будет вести лог всех сообщений
    log(message,answer)

bot.polling(none_stop = True, interval=0)