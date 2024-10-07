import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


API_TOKEN = "7745534482:AAHFq4WIThjPXVjhZwrjRgzHXPUb9qdBsbA"
bot = telebot.TeleBot(API_TOKEN)

departments = {
    "📘 ASGE (Applied Science and General Engineering)": {
        "Head of Department": {
            "Dr. Ganesh Mundhe": {"email": "gmundhe@aitpune.edu.in", "phone": "9579408564"}
        },
        "Teaching": {
            "Dr (Mrs) Suwati Kulkarni": {"email": "skulkarni@aitpune.edu.in", "phone": "9405012782"},
            "Mr V. Hivrale": {"email": "vhivrale@aitpune.edu.in", "phone": "9665582369"},
            "Mr S K Misal": {"email": "smisal@aitpune.edu.in", "phone": "9423547900"}
        },
        "Non-Teaching": {
            "Mr Raghu Babar": {"email": "rbabar@aitpune.edu.in", "phone": "9763607929"},
            "Ms Swati Salunkhe": {"email": "ssalunkhe@aitpune.edu.in", "phone": "9604870370"}
        }
    },
    "💻 COMPUTER": {
        "Head of Department": {
            "Prof (Dr) S R Dhore": {"email": "hodcomp@aitpune.edu.in", "phone": "9890809251"}
        },
        "Teaching": {
            "Mr Kuldeep Hule": {"email": "kuldeephule@aitpune.edu.in", "phone": "8668277166"},
            "Mrs Asha Sathe": {"email": "asathe@aitpune.edu.in", "phone": "7888034146"},
            "Dr Yogesh Sangle": {"email": "ysangle@aitpune.edu.in", "phone": "8788042514"},
            "Mr Mangesh Tawari": {"email": "mtawari@aitpune.edu.in", "phone": "9876342952"}
        },
        "Non-Teaching": {
            "Mr Ravindrinda Desai": {"email": "rdesai@aitpune.edu.in", "phone": "7820958840"},
            "Ms Priyanka Holkar": {"email": "priyankeholkar@aitpune.edu.in", "phone": "9561190391"}
        }
    },
    "🌐 IT (Information Technology)": {
        "Head of Department": {
            "Dr (Mrs) Sangeeta Jadhav": {"email": "hodit@aitpune.edu.in", "phone": "9923011211"}
        },
        "Teaching": {
            "Dr Rahul Desai": {"email": "rahuldesai@aitpune.edu.in", "phone": "9403357088"},
            "Dr Ashwini Sapkal": {"email": "asapkal@aitpune.edu.in", "phone": "9881776565"},
            "Mr Amit Gokhale": {"email": "agokhale@aitpune.edu.in", "phone": "9422541165"}
        },
        "Non-Teaching": {
            "Ms Jyoti Taralkar": {"email": "jyotitaralkar@aitpune.edu.in", "phone": "9172802015"},
            "Mr Suryakant Kenjale": {"email": "suryakantkenjale@aitpune.edu.in", "phone": "9881158998"}
        }
    },
    "📡 ENTC (Electronics and Telecommunication)": {
        "Head of Department": {
            "Dr G R Patti": {"email": "hodetc@aitpune.edu.in", "phone": "9422356483"}
        },
        "Teaching": {
            "Dr P K Karandikar": {"email": "pkarandikar@aitpune.edu.in", "phone": "9420427741"},
            "Dr Shraddha Oza": {"email": "sdoza@aitpune.edu.in", "phone": "9890276477"},
            "Mrs Kavita Tawari": {"email": "ktawari@aitpune.edu.in", "phone": "9812346475"}
        },
        "Non-Teaching": {
            "Ms Sujata Kadam": {"email": "skadam@aitpune.edu.in", "phone": "9423047541"},
            "Mr Bhikaji Gaidekar": {"email": "bhikajigaidekar@aitpune.edu.in", "phone": "9284854108"}
        }
    },
    "🔧 MECHANICAL": {
        "Head of Department": {
            "Prof (Dr) U V Avasarmol": {"email": "hodmech@aitpune.edu.in", "phone": "8007976763"}
        },
        "Teaching": {
            "Mr V Kulkarni": {"email": "virkulkarni@aitpune.edu.in", "phone": "9673694499"},
            "Dr J D Patil": {"email": "jdpatil@aitpune.edu.in", "phone": "9923287262"},
            "Mr P H Pujari": {"email": "phpujari@aitpune.edu.in", "phone": "9765428827"}
        },
        "Non-Teaching": {
            "Mr S H Karande": {"email": "shkarande@aitpune.edu.in", "phone": "8087905342"},
            "Mr A J Gaigole": {"email": "ajgaigole@aitpune.edu.in", "phone": "9850022286"}
        }
    }
}


user_data = {}
theme_data = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_data[message.chat.id] = {}
    theme_data[message.chat.id] = "day" 

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🌞 Day Mode", callback_data="theme_day"))
    markup.add(InlineKeyboardButton("🌙 Night Mode", callback_data="theme_night"))

    welcome_message = (
        f"👋 *Hello, {message.from_user.first_name}!* \n\n"
        "🎉 Welcome to the *AIT Faculty Information Bot*! \n\n"
        "I'm here to help you quickly find the contact information of faculty members across various departments.\n\n"
        "But first, let's make this experience visually comfortable for you. "
        "Please choose your preferred theme: \n\n"
        "🌞 *Day Mode* for a bright and clear view \n"
        "🌙 *Night Mode* for a cool, dark interface"
    )

    bot.send_message(message.chat.id, welcome_message, reply_markup=markup, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data.startswith("theme_"))
def set_theme(call):
    theme = call.data.split("_")[1]
    theme_data[call.message.chat.id] = theme

    markup = InlineKeyboardMarkup()
    for dept in departments.keys():
        markup.add(InlineKeyboardButton(dept, callback_data=f"dept_{dept}"))

    theme_msg = "☀️ *Day Mode* activated!" if theme == "day" else "🌙 *Night Mode* activated!"

    
    bot.edit_message_text(f"{theme_msg}\nPlease choose a department:", 
                          chat_id=call.message.chat.id, 
                          message_id=call.message.message_id, 
                          reply_markup=markup, 
                          parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith("dept_"))
def ask_faculty_type(call):
    department = call.data.split("_", 1)[1]
    user_data[call.message.chat.id]["department"] = department

    markup = InlineKeyboardMarkup()
    for faculty_type in departments[department].keys():
        markup.add(InlineKeyboardButton(faculty_type, callback_data=f"faculty_{faculty_type}"))

    bot.edit_message_text(f"You selected *{department}* department. Please choose the type of faculty:", 
                          chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data.startswith("faculty_"))
def ask_faculty_member(call):
    faculty_type = call.data.split("_", 1)[1]
    department = user_data[call.message.chat.id]["department"]
    user_data[call.message.chat.id]["faculty_type"] = faculty_type

    markup = InlineKeyboardMarkup()
    for member in departments[department][faculty_type].keys():
        markup.add(InlineKeyboardButton(member, callback_data=f"member_{member}"))

    bot.edit_message_text(f"You selected *{faculty_type}* faculty. Please select a faculty member:", 
                          chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.startswith("member_"))
def provide_contact(call):
    member = call.data.split("_", 1)[1]
    department = user_data[call.message.chat.id]["department"]
    faculty_type = user_data[call.message.chat.id]["faculty_type"]

    contact_info = departments[department][faculty_type][member]
    bot.edit_message_text(f"Contact details for *{member}*:\nEmail: {contact_info['email']}\nPhone: {contact_info['phone']}",
                          chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown")


bot.polling(none_stop=True)
