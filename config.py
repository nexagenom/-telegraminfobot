# токен бота (Bot Token)
token = "yourtoken"

# ID кому пересылаем и ID администратора (ID for forwarding, and admin's ID)
forwardid = "1234567"
adminid = "1234567"

# ссылки на социальные сети (social networks links and names)
vktext = "Вконтакте"
vkurl = "https://vk.com/"

instatext = "Инстраграм"
instaurl = "https://www.instagram.com/"

# смайлы (smiles)
whaticansmile = u"\u2699"
portfoliosmile = u"\U0001F307"
contactssmile = u"\U0001F4F1"
sendmessagesmile = u"\U0001F4E8"
photosessiongsighupsmile = u"\U0001F4BE"

# директории файлов (files directory)
portraitdir = "/portfolio/portraits"

# стикеры (Stickers ID)
constantstrickers = ('CAADAgADfwIAAkcVaAlrb-N3pbZeOwI', 'CAADAgADggIAAkcVaAkz8MlCdxISCgI', 'CAADAgADdwIAAkcVaAl1NliBo9TnOgI', 'CAADAgADdwIAAkcVaAl1NliBo9TnOgI', 'CAADAgADcQIAAkcVaAkjbdIaeQN9NwI')
randomizestickers = ('CAADAgADdwIAAkcVaAl1NliBo9TnOgI', 'CAADAgADfAIAAkcVaAnjWmqifO_ULgI', 'CAADAgADYwIAAkcVaAnOTJQ1wirBbQI', 'CAADAgADaQIAAkcVaAn0xZGL37fCiQI', 'CAADAgADbAIAAkcVaAnx7Y1W5UYCgAI')

# надписи кнопок (buttons text)
menubuttons = (whaticansmile + ' Что я умею?', portfoliosmile + ' Портфолио', contactssmile + ' Контакты', sendmessagesmile + ' Отправить сообщение', 'Еще одну?', 'Хватит!', photosessiongsighupsmile + ' Записаться на фотосет')
constantmessages = ('Примеры работ', 'Выбранная дата: ', '<b>Выбранная дата отправлена, мы свяжется с вами в ближайшее время, спасибо</b>', 'Желаемая дата: ')
calendarsbuttons = ('\u2b05\ufe0f', ' ', '\u27a1\ufe0f')

# админка (admin section)
adminrequests = ('админка', 'admin')
adminanswers = ('Получай свой лог', '')
nonadminmessage = ('Такой команды не существует', 'Прости, я не понял тебя', 'Упс, что-то пошло не так', 'Как дела?', 'Хочешь стикер?')
adminmessage = ('Привет, админушка', 'Здравствуй, начальник', 'Админка включена', 'Хэллоу, админ', 'Хей, админ')
admininlinebuttons = ('Получить лог', 'Выйти из админки')
adminmenuresponses = ('выход', 'добавить новый ответ')
noadmincommandmessage = ('У меня не такой команды', 'А у меня такого нет', 'Я это не умею')

# надпись с callback (callback text)
callbackquerymoremessages = ('Ну, держи!', 'А как тебе эта?', 'Фоточка!', 'Еще фотка')
callbackqueryoutmessages = ('Окей', 'Ну, хорошо', 'А я хотел тебе показать', 'Эх, ну ладно')

# списки сообщений на который реагирует бот, используйте нижний регистр,
# так как бот преобразует все посланные ему сообщения в нижний регистр (List of the messages, use lower case,
# because bot will convert user message into lower case)
hellomessages = ('привет', 'hello', 'hi', 'при', 'ку', 'здравствуйте', 'хай', 'приветули')
byemessages = ('досвидания', 'пока', 'до свидания', 'bye', 'досвидули', 'пакеда', 'я ухожу')
helpmessages = (whaticansmile + ' что я умею?', 'help', 'рудз', 'помощь', 'памагите', 'че умеешь?', 'что я умею?', 'что умеешь?')
contactmessages = (contactssmile + ' контакты', 'контакты', 'contacts', 'как связаться?', 'как связаться', 'куда писать?', 'куда писать')
portfoliomessages = (portfoliosmile + ' портфолио', 'портфолио', 'фотки', 'работы', 'примеры', 'примеры работ', 'фото', 'примеры фото')
sendmessagemessages = (sendmessagesmile + ' отправить сообщение', 'отправить сообщение', 'связаться', 'хочу пообщаться')
photosessiongsighup = (photosessiongsighupsmile + ' записаться на фотосет', 'записаться на фотосет', 'записаться на фотосессию', 'фотосет', 'хочу на фотосессию', 'хочу на фотосет')

# списки ответов бота на сообщения. (Bot answers)

startmessagesanswers = ('Ну что-ж приступим?!', 'Ну что начнем?!', 'Давай начнем скорее мною пользоваться!', 'Приветик, ну как там дела?')
helpcommandanswers = 'Здесь вы можете получить информацию о фотосессиях, просмотреть портфолио, задать свой вопрос.'
stickersanswers = ('У меня тоже есть стикеры \nПосмотри', 'У меня такой же стикер есть :)', 'О - стикер! Лови ответочку', 'Ух-ты, стикер!')
stickersanswers2 = ('Вот - нашел :)', 'Пошуршал и нашел тебе такой', 'А вот и мой стикер!', 'Смотри какой у меня стикер')
helloanswers = ('Ну приветики коли не шутишь', 'И тебе приветики', 'Ух ты, привет, я тебя ждал', 'Хи-хи, ну, здравствуй', 'Привет и тебе тут :)')
byeanswers = ('До свидания :)', 'Пока и тебе :(', 'Так быстро уходишь?', 'Надеюсь скоро снова встретимся', 'Ну вооот, ну, что-ж, пока')
ownershelloanswers = ('Привет, хозяин', 'Привет, хозяин мой, как твои делишки?', 'Привет, мой начальник!', 'Хи-хи как денек? :)' ,'Привет, насяльнике :)')
sendmessageanswers = ('Просто напиши мне сообщение и я перешлю его', 'Очень просто - напиши мне одно сообщения, и я сразу перешлю его', 'Напиши любое сообщение и я перешлю его', 'Просто пиши в чат, а я позобочусь о том, чтобы сообщение пришло куда нужно ;)')
contactsanswers = ('Пожалуйста выберите социальную сеть для связи:', 'Социалочки для связи:', 'А вот и социальный сети:', 'Социальные сети:')
portfolioanswer = "Я буду присылать по одной фотографии, чтобы получить другую - жми на кнопку \"Еще одну?\" "
ownerssendmessageanswers = ('Сообщение передано создателю, спасибо за ваше сообщение.', 'Я отправил создателю сообщение, надеюсь он скоро ответит :)', 'Я переслал сообщение, я сделяль!', 'Отправлено создателю, спасибо')
inlinequeryanswers = ('Ты знаешь как просмотреть снова, если что ;)', ' Ну вооот, я думал ты поглядишь еще', 'Если захочешь снова посмотреть - ты знаешь как это сделать')
photosessiongsighupanswers = ('Выбирай удобнуб для себя дату:', 'Пора выбрать дату:', 'Вот и подошел момент выбора даты', 'Выбирай скорее дату:')
photosessiongsighupwarning = """<pre>ВНИМАНИЕ \nВы выбираете ЖЕЛАЕМУЮ дату для фотосессии, окончательная дата будет определена лично при общении с нами \nЯ перешлю вашу желаемую дату. Спасибо!</pre>"""
