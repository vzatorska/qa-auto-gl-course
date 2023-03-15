class Config:
    """Exception - is an error. Expected or unexpected
    1. Контрольована помилка, яка виникає під час перевірки. Catched. Runtime(?)
    2. Неконтрольована помилка. Uncatched
    Має бути виконаний одразу ж. Дуже бажано.
    Конфіг файл має проініціалізувати все, що потрібно для тестів.Також заборонити те, що не проініціалізовано.

    """

    def register(self,name):
        """
        Register name of the key which is used
        in tests
        """

    def set(self, key, value):     #Set ініціалізує.
        """
        Set key to value
        """
        pass

    def get(self):
        """
        Return eisting value
        """
        pass