from aiogram import types 

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('rules', 'Show the rules'),
        types.BotCommand('write_down', 'Write in the death note'),
        types.BotCommand('death_list', 'Show death note'),
    ])