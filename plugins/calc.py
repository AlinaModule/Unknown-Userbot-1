from pyrogram import types
from utils import (
    code, Cmd, get_group, PREFIX,
    helplist, Module, Argument as Arg, Command
)

cmd = Cmd(get_group())

calc_module = Module(
    "calc",
    version='1.0.0',
    author='@Coder_Hikka',
    description="Калькулятор",
).add_command(
    Command(
        ['к'],
        [Arg("(пример)")],
        "- решить пример"
    )
)

helplist.add_module(calc_module)

@cmd(['к'])
async def calc(_, msg: types.Message):
    if len(msg.command) < 2:
        await msg.edit(f"<emoji id=5465665476971471368>❌</emoji> <b>Пожалуйста, введите выражение, которое хотите посчитать</b>")
        return
    
    _, equations = msg.text.split(maxsplit=1)
    
    i = (equations
        .replace('^', '**')
        .replace('x', '*')
        .replace('х', '*')
        .replace('•', '*')
        .replace('·', '*')
        .replace('∙', '*')
        .replace(':', '/')
        .replace('÷', '/')
        .replace('√', 'math.sqrt')
    )
    try:
        import math
        
        def root(n: int | float, k: int | float = 2) -> float:
            return n ** (1 / k)

        e = eval(i, globals(), locals())

        try:
            pe = int(e) if int(e) == e else e
        except:
            pe = e
        
        await msg.edit(f"<emoji id=5472164874886846699>✨</emoji> <code>{equations}</code>: <code>{code(pe)}</code>")
    except Exception as ex:
        print(ex)
        import traceback
        traceback.print_tb(ex.__traceback__)
        await msg.edit(f"<emoji id=5465665476971471368>❌</emoji> <b>Ошибка!\n\nДля исправления</b>: <code>{code(f'{PREFIX}{msg.command[0]} {equations}')}</code>")