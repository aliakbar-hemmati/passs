
from telegram.ext import Updater, CallbackContext, ConversationHandler, CommandHandler, MessageHandler, Filters, updater
from telegram import Update, message, replykeyboardmarkup, ReplyKeyboardRemove

import random

token = '1632732324:AAFa2heoBQnNUDigD_5LaViZBEf-L0B7wso'
setting = {'lower_alp': 'True', 'upper_alph': 'True',
           'symbols': 'True', 'numbers': 'True', 'lengh': 10}
account = {}
test_dict_name = {}
test_dict_user = {}
# '''-----------------------------------------------------------------------------------__________________________'''


def start(update: Update, context: CallbackContext):
    update.message.reply_text(reply_to_message_id=update.message.message_id, text='''سلام🤗
        من bitwarden هستم
        میتونم در مدیریت پسورد ها بهت کمک کنم
        با دستور /generate میتونم یه پسورد برات بسازم
        با دستور /setting میتونی تنظیمات تولید پسورد را تغییر دهی
        با دستور /add_account یک اکانت اضافه کن
        با دستور /account هم به حساب هایی که سیو کردی، دسترسی داری''')


def generate_pass(update: Update, context: CallbackContext):
    lower_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                  'v', 'w', 'x', 'y', 'z']
    upper_alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                  'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', ';',
               '<', '>', '.', '?', '/']

    def settingg():
        if setting['lower_alp'] == 'True' and setting['symbols'] == 'True' and setting['upper_alph'] == 'True' and setting[
                'numbers'] == 'True':
            return lower_alph + upper_alph + numbers + symbols

        if setting['lower_alp'] == 'False' and setting['symbols'] == 'True' and setting['upper_alph'] == 'True' and setting[
                'numbers'] == 'True':
            return upper_alph + numbers + symbols

        if setting['lower_alp'] == 'True' and setting['symbols'] == 'False' and setting['upper_alph'] == 'True' and setting[
                'numbers'] == 'True':
            return lower_alph + upper_alph + numbers

        if setting['lower_alp'] == 'True' and setting['symbols'] == 'True' and setting['upper_alph'] == 'False' and setting[
                'numbers'] == 'True':
            return lower_alph + numbers + symbols

        if setting['lower_alp'] == 'True' and setting['symbols'] == 'True' and setting['upper_alph'] == 'True' and setting[
                'numbers'] == 'False':
            return lower_alph + upper_alph + symbols

        if setting['lower_alp'] == 'False' and setting['symbols'] == 'False' and setting['upper_alph'] == 'True' and setting[
                'numbers'] == 'True':
            return upper_alph + numbers
        if setting['lower_alp'] == 'False' and setting['symbols'] == 'True' and setting['upper_alph'] == 'False' and setting[
                'numbers'] == 'True':
            return numbers + symbols
        if setting['lower_alp'] == 'False' and setting['symbols'] == 'True' and setting['upper_alph'] == 'True' and setting[
                'numbers'] == 'False':
            return upper_alph + symbols
        if setting['lower_alp'] == 'False' and setting['symbols'] == 'False' and setting['upper_alph'] == 'False' and setting[
                'numbers'] == 'True':
            return numbers
        if setting['lower_alp'] == 'False' and setting['symbols'] == 'False' and setting['upper_alph'] == 'True' and setting[
                'numbers'] == 'False':
            return upper_alph
        if setting['lower_alp'] == 'False' and setting['symbols'] == 'True' and setting['upper_alph'] == 'False' and setting[
                'numbers'] == 'False':
            return symbols
        if setting['lower_alp'] == 'True' and setting['symbols'] == 'False' and setting['upper_alph'] == 'False' and setting[
                'numbers'] == 'False':
            return lower_alph
        if setting['lower_alp'] == 'True' and setting['symbols'] == 'False' and setting['upper_alph'] == 'False' and setting[
                'numbers'] == 'True':
            return lower_alph + numbers
        if setting['lower_alp'] == 'True' and setting['symbols'] == 'False' and setting['upper_alph'] == 'True' and setting[
                'numbers'] == 'False':
            return lower_alph + upper_alph
        if setting['lower_alp'] == 'True' and setting['symbols'] == 'True' and setting['upper_alph'] == 'False' and setting[
                'numbers'] == 'False':
            return lower_alph + symbols
        if setting['lower_alp'] == 'False' and setting['symbols'] == 'False' and setting['upper_alph'] == 'False' and setting[
                'numbers'] == 'False':
            return None

    def final_dic_and_pass(dict):
        try:

            x = random.choices(dict, k=setting['lengh'])
            return ''.join(x)
        except:
            return 'can not generate pass word\n❌❌change the setting❌❌'
    update.message.reply_text(
        text=f'your password is ready\n{final_dic_and_pass(settingg())}')


def setting_command(update: Update, context: CallbackContext):
    update.message.reply_text(text=f'''the current setting is:
    use  Uppercase letters: A-Z = {setting['upper_alph']}
    use Lowercase letters: a-z = {setting['lower_alp']}
    use Numbers: 0-9 = {setting['numbers']}
    use Symbols: ~`! @#$%^&*()_-+=[]|\:;"'<,>.?/ = {setting['symbols']}
    length of generated password = {setting['lengh']} ''')
    update.message.reply_text(text='to change the setting use these buttoms', reply_markup=replykeyboardmarkup.ReplyKeyboardMarkup(keyboard=[
        ['Uppercase', 'Lowercase'],
        ['Numbers', 'Symbols'],
        ['Length']
    ], resize_keyboard=True, one_time_keyboard=True))


def lowercase(update: Update, context: CallbackContext):
    if setting['lower_alp'] == 'False':
        setting['lower_alp'] = 'True'
    elif setting['lower_alp'] == 'True':
        setting['lower_alp'] = 'False'

    update.message.reply_text(
        text=f'Done!\nuse Lowercase letters: a-z = {setting["lower_alp"]}\n\nyou can generate new password by /generate\nto change settings use /setting\nto add account /add_account and to view your saved accounts /account', reply_markup=ReplyKeyboardRemove())


def uppercase(update: Update, context: CallbackContext):
    if setting['upper_alph'] == 'False':
        setting['upper_alph'] = 'True'
    elif setting['upper_alph'] == 'True':
        setting['upper_alph'] = 'False'
    update.message.reply_text(
        text=f'Done!\nuse  Uppercase letters: A-Z = {setting["upper_alph"]}\n\nyou can generate new password by /generate\nto change settings use /setting\nto add account /add_account and to view your saved accounts /account', reply_markup=ReplyKeyboardRemove())


def symbols(update: Update, context: CallbackContext):
    if setting['symbols'] == 'False':
        setting['symbols'] = 'True'
    elif setting['symbols'] == 'True':
        setting['symbols'] = 'False'
    update.message.reply_text(
        text=f'Done!\nuse Symbols:{setting["symbols"]}\n\nyou can generate new password by /generate\nto change settings use /setting\nto add account /add_account and to view your saved accounts /account', reply_markup=ReplyKeyboardRemove())


def numbers(update: Update, context: CallbackContext):

    if setting['numbers'] == 'False':
        setting.update({'numbers': 'True'})
    elif setting['numbers'] == 'True':
        setting.update({'numbers': 'False'})

    update.message.reply_text(
        text=f'Done!\nuse Numbers: 0-9 = {setting["numbers"]}\n\nyou can generate new password by /generate\nto change settings use /setting\nto add account /add_account and to view your saved accounts /account', reply_markup=ReplyKeyboardRemove())

def len_pass(update: Update, context: CallbackContext):
    update.message.reply_text(text='enter the length of your generated password in numbers (1-256)')
    return 1
def done_len_pass(update: Update, context: CallbackContext):
    length = update.message.text
    
    if length.isdigit()==True:
        length=int(length)
        if length <=256:
            setting['lengh']=length
            update.message.reply_text(text=f'Done!\nthe new length of generated passwords is {setting["lengh"]}')
            return -1
        elif length >256:
            update.message.reply_text(text='enter the length between 1-256')
    elif length.isdigit()!=True:
        update.message.reply_text(text='unacceptable input\nenter length in digits (1-256)')
def show_accounts(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    try:
        for key in account[user_id]:
            update.message.reply_text(text=f'''account name: {key}
            username: {account[user_id][key][-2]}
            password: {account[user_id][key][-1]}''')
    except:
        update.message.reply_text(
            text="an error accured, or you have not set any password yet", reply_to_message_id=update.message.message_id)


def add_accounts(update: Update, context: CallbackContext):
    user_id = update.message.chat_id

    update.message.reply_text(
        text="add your accont's name", reply_to_message_id=update.message.message_id)
    return 1


def user(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    name = update.message.text
    test_dict_name.update({user_id: name})
    update.message.reply_text(text='`add your username`')
    return 2


def password(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    # print(test_dict[user_id]["name"] + '/n' + test_dict[user_id]["user"])
    userr = update.message.text
    test_dict_user.update({user_id: userr})
    update.message.reply_text(text='add your password')
    return 3


def done(update: Update, context: CallbackContext):
    user_id = update.message.chat_id

    passs = update.message.text
    account.update({user_id:
                    {test_dict_name[user_id]: [test_dict_user[user_id],
                                               passs]
                     }
                    })

    update.message.reply_text(text=f'''Done! the account {test_dict_name[user_id]}
    {test_dict_user[user_id]}:{passs}
has been added. you can see your saved accounts by using /account
you can add another account by /add_account ''')
    del test_dict_name[user_id]
    del test_dict_user[user_id]
    return -1


def cancel_acc(update: Update, context: CallbackContext) -> int:
    show_accounts(update, context)
    return -1


# '''------------------------------------------------------------------------------------------------------------------------------------------'''
# , request_kwargs={'proxy_url': 'socks5h://127.0.0.1:9150'}
updater = Updater(token='1632732324:AAFa2heoBQnNUDigD_5LaViZBEf-L0B7wso',
                  request_kwargs={'proxy_url': 'socks5h://127.0.0.1:9150'})

conver = ConversationHandler(
    entry_points=[CommandHandler('add_account', add_accounts)],
    states={
        1: [MessageHandler(Filters.text, user)],
        2: [MessageHandler(Filters.text, password)],
        3: [MessageHandler(Filters.text, done)]
    },
    fallbacks=[CommandHandler('account', cancel_acc)],
    run_async=True
)
conver_len = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex('^Length$'),len_pass)],
    states={
        1:[MessageHandler(Filters.text,done_len_pass)]
    },
    fallbacks=[]
)
updater.dispatcher.add_handler(CommandHandler('start', start, run_async=True))
updater.dispatcher.add_handler(CommandHandler(
    'generate', generate_pass, run_async=True))
updater.dispatcher.add_handler(CommandHandler(
    'setting', setting_command, run_async=True))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('^Uppercase$'), uppercase, run_async=True))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('^Lowercase$'), lowercase, run_async=True))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('^Numbers$'), numbers, run_async=True))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex('^Symbols$'), symbols, run_async=True))
updater.dispatcher.add_handler(CommandHandler(
    'account', show_accounts, run_async=True))
updater.dispatcher.add_handler(conver)
updater.dispatcher.add_handler(conver_len)

updater.start_polling()
print('Run')
updater.idle()
