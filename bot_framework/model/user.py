from typing import Union


class BotUser:
    """
    Bot's user

    :param id: Unique identifier for this user or bot. Any type

    :param first_name: User's or bot's first name
    :type first_name: :obj:`str`

    :param last_name: Optional. User's or bot's last name
    :type last_name: :obj:`str`

    :param username: Optional. User's or bot's username
    :type username: :obj:`str`
    """

    id: Union[int, str]
    first_name: str
    username: str
    last_name: str

    def __init__(self,
                 id,
                 first_name: str,
                 last_name: str = None,
                 username: str = None,
                 **kwargs):
        self.id = id
        self.first_name: str = first_name
        self.username: str = username
        self.last_name: str = last_name

    @property
    def full_name(self):
        """
        :return: User's full name
        """
        full_name = self.first_name
        if self.last_name:
            full_name += ' {0}'.format(self.last_name)
        return full_name
