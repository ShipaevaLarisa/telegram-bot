from core.base import Event, IncomingMessage
from core import Pythogram


class Video(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        text = message.text.strip().lower()
        return text in ['вышивка']

    def action(self, message: IncomingMessage, *args, **kwargs):
        text = f'Вышивка бисеров: https://www.youtube.com/watch?v=Wa52msmmbmA\n' \
               f'Вышивка крестиком: https://www.youtube.com/watch?v=mudMX4xnn0E\n' \
               f'Вышивка гладью: https://www.youtube.com/watch?v=ZpW4zAjCw4s\n' \
               f'Вышивка лентами: https://www.youtube.com/watch?v=QdyOsGUC36w'
        self.__sender.message.send(
            text=text,
            chat=message.chat
        )
