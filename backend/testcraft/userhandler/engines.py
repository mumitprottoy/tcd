from . import models


class PlatformMaker:
    
    def __init__(self, user: models.User, name: str) -> None:
        self.user = user
        self.name = name
    
    def __create_platform(self) -> models.Platform:
        return models.Platform.objects.create(name=self.name)
    
    def __create_member(self) -> models.PlatformMember:
        platform = self.__create_platform()
        return models.PlatformMember.objects.create(
            user=self.user, platform=platform, is_admin=True)
    
    def make(self) -> tuple[models.Platform, models.PlatformMember]:
        platform = self.__create_platform()
        member = self.__create_member()
        return platform, member 

