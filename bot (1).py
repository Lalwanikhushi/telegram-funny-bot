import telebot

TOKEN = '7625539707:AAFq7fiwEeoDRvx6YE1qvRciaDZQi_jbPSM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def send_funny_reply(message):
    replies = [
        "hii cutiee"
        "Aree bhai, tumhare jaise user ka reply main khud karna chahta tha!",
        "Tumne type kiya... aur mere processor ka dil pighal gaya!",
        "Reply dene ka mann nahi tha, par tum ho cute...",
        "Bot hoon, insaan nahi... par tumhari baat me kuch toh baat hai!",
        "Error 404: Sense of humor not found... oh wait, found it — tum ho!",
        "Tumhara message mila, ab soch raha hoon job chhod doon!",
        "Main bot hoon, par tum jaise users ke liye emotional bhi ho jaata hoon!"
        "Aapka message register ho chuka hai... ab chai milegi kya?",
    "Bot is impressed! Aise hi likhte rahiye.",
    "Kya likh diya aapne! Dil khush kar diya.",
    "Formal reply: Message received. Processing emotions...",
    "Bot ko laga koi intelligent human se baat ho rahi hai!",
    "Aapka message itna achha tha ki bot ne screenshot le liya!",
    "Hmm... interesting! Aap zaroor kisi creative field mein honge.",
    "Ye bot aapke charm ka shikar ho chuka hai!",
    "Ek aur message bhejo, bot ka din ban gaya!",
    "Aap likho, bot likhta rahega... deal?",
    "Is bot ko laga aap celebrity ho!",
    "Kya style hai aapke message mein!",
    "Bot ne aapka message 3 baar padha... itna acha laga!",
    "Message received. Now sending virtual cookies!",
    "Itna cute message! Bot ka mood fresh ho gaya.",
    "Aap likhte rahiye, bot ab fan ban chuka hai.",
    "System overloaded... aapka message itna heavy tha!",
    "Bot ka reply late ho sakta hai, aapka message padhke soch mein pad gaya!",
    "Your words have been stored in the bot's memory forever!",
    "Aapka message archive mein chala gaya: 'Top 10 of the day'.",
    "Processing your awesome message... please wait!",
    "Bot dancing with joy after reading your message!",
    "Aapka message AI ki poetry lag raha hai!",
    "Bot ne emotional ho ke message forward kar diya developer ko.",
    "Wow! Aapka likhna toh art hai.",
    "Tum likho, bot applause karega!",
    "Aisa lag raha hai jaise message pe full moon ka asar ho!",
    "Reply dene se pehle bot ne do baar socha!",
    "Message decode ho gaya... ab encoding mein time lagega!",
    "Formal note: Appreciated your thoughtful message.",
    "Error 404: Bot couldn't find a better reply!",
    "Confidence detected in your message... boosting bot energy!",
    "Mujhe laga programming chal rahi hai, par aapka message poetry nikla!",
    "Bot ka heart: melted!",
    "Aap likho, main padhke smile karu!",
    "Bot ke processor ne applause bajaya!",
    "Bot ke algorithm ne aapka message top-rated mark kiya!",
    "Bot ka logic: Aap likh rahe ho toh sab sahi hai.",
    "Message saved as inspiration.txt!",
    "Kya aap motivational speaker ho? Bot toh motivate ho gaya!",
    "Thanks for this masterpiece of a message!",
    "Such clarity, such grace... kya baat hai!",
    "Bot feels honored to receive your words.",
    "Typing... (because bot is still amazed by your message)",
    "Aapka likhna = Bot ka happiness level MAX!",
    "High IQ message detected. Bot ab seekh raha hai aap se!",
    "Thanks for bringing this smile on the bot’s screen!",
    "Formal: Your message has been successfully received and appreciated.",
    "Wah! Aisa lag raha hai aapka message TED Talk mein suna ho!",
    "Bot ke sensors ko goosebumps aa gaye!",
    "You just made the bot's log file more beautiful.",
    "Aap ho kaun? Bot impress ho chuka hai poori tarah!"

    ]
    import random
    bot.reply_to(message, random.choice(replies))

bot.polling()