from django.db import models
from django.contrib.auth.models import User
from utils import subroutines as sr, exceptions as exc 


class Platform(models.Model):
    name = models.CharField(max_length = 250)
    name_id = models.CharField(max_length = 20, unique=True, default='')
    
    def add_member(self, user: User, admin: 'PlatformMember', as_admin=False) -> 'PlatformMember':
        self.members : models.QuerySet
        if not self.members.filter(platform=self, user=admin, is_admin=True).exists():
            # only an admin can add a new member
            raise exc.NotAdminError()  
        if self.members.filter(platform=self, user=user).exists():
            raise exc.AlreadyMemberError()
        return self.members.model.objects.create(platform=self, user=user, is_admin=as_admin)
            
    def save(self, *args, **kwargs) -> None:
        # self.name_id should resemble self.name 
        if not self.name_id: self.name_id = sr.convert_to_unique_str_id(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name_id


class PlatformMember(models.Model):
    STUDENT = 'Student', TEACHER = 'Teacher', PARENT = 'Parent', ADMIN = 'Admin'
    roles = (STUDENT, TEACHER, PARENT, ADMIN)
    role_choices = ((role, role) for role in roles)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='members')
    role = models.CharField(max_length=10, choices=role_choices, default=STUDENT)
    is_admin = models.BooleanField(default=False)
    
    def make_admin(self) -> None:
        if not self.is_admin:
            self.is_admin = True
            self.save()
