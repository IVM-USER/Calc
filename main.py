from base.module import command, BaseModule
from pyrogram.types import Message



class Calc(BaseModule):
    @command("calc")
    async def calc(self, _, message: Message):
        """Calculator module"""   
        error = self.S["calc"]["err"]
        noreply = self.S["calc"]["not_reply"]
        question = message.text.split(maxsplit=1)[1] if len(message.command) > 1 else None
        reply = message.reply_to_message
        if not question:
            if not reply:
                await message.reply(noreply)
                return
            else:
                question = reply.text
        try:
            answer = eval(question)
            answer = f"{question}=<code>{answer}</code>"
        except Exception as e:
            answer = f"{error}"
        await message.reply(answer)
