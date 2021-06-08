from app import bot, dp, admin_id, getUserLogsFromMessage
from aiogram.types import Message
from keyboards import kb_donate, kb_menu, kb_resource, kb_leadershipCourse


async def send_to_admin_start(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


# Первое приветствие пользователя
@dp.message_handler(commands=['start'])
async def startsMessage(message: Message):
    await message.answer("Выбери необходимый пункт в меню", reply_markup=kb_menu.menu_kb)
    print(await getUserLogsFromMessage(message))

# Выдача конспектов
@dp.message_handler(text='Конспекты')
async def getNotes(message: Message):
    await message.answer("Выбери таблицу", reply_markup=kb_resource.notes_menu_kb)
    print(await getUserLogsFromMessage(message))

# Возвращение к меню
@dp.message_handler(text='Вернуться в меню')
async def getMenu(message: Message):
    await message.answer("Выбери необходимый пункт в меню", reply_markup=kb_menu.menu_kb)
    print(await getUserLogsFromMessage(message))

# Выдача расписания
@dp.message_handler(text='Расписание')
async def getSchedule(message: Message):
    await message.answer("Расписание ближайших мероприятий церкви в Москве")
    print(await getUserLogsFromMessage(message))


# Выдача материалов лидерского курса
@dp.message_handler(text='Лидерские курсы')
async def getLeadershipCourse(message: Message):
    await message.answer("Здесь ты найдешь материалы для лидеров домашних групп:",
                         reply_markup=kb_leadershipCourse.leadershipCourse_kb)
    print(await getUserLogsFromMessage(message))


# Переход в раздел "Пожертвование"
@dp.message_handler(text='Пожертвование')
async def getDonate(message: Message):
    await message.answer("Благодаря твоей поддержке мы можем" +
                         "\nпродолжать насаждать церкви и распространять Евангелие!", reply_markup=kb_donate.donate_kb)
    print(await getUserLogsFromMessage(message))
