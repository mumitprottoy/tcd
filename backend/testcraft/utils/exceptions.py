from . import messages as msg


class DelimiterError(Exception):
    
    def __init__(self, msg: str=msg.INVALID_DELIMITER) -> None:
        super().__init__(msg)


class NotMemberError(Exception):
    
    def __init__(self, msg: str=msg.NOT_MEMBER) -> None:
        super().__init__(msg)


class AlreadyMemberError(Exception):
    
    def __init__(self, msg: str=msg.NOT_MEMBER) -> None:
        super().__init__(msg)


class NotAdminError(Exception):
    
    def __init__(self, msg: str=msg.NOT_ADMIN) -> None:
        super().__init__(msg)