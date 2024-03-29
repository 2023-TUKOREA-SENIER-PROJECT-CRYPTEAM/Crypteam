from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# 헬퍼 클래스
class UserManager(BaseUserManager):
    def create_user(self, email, password, user_name='', birth=None, phone_number='', api_key='', sec_key='', **kwargs):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=email,
            user_name=user_name,
            birth=birth,
            phone_number=phone_number,
            api_key=api_key,
            sec_key=sec_key,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, user_name='', birth=None, phone_number='', api_key='', sec_key='', **extra_fields):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여
        """
        superuser = self.create_user(
            email=email,
            password=password,
            user_name=user_name,
            birth=birth,
            phone_number=phone_number,
            api_key=api_key,
            sec_key=sec_key,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        
        superuser.save(using=self._db)
        return superuser


# AbstractBaseUser를 상속해서 유저 커스텀
class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    user_name = models.CharField(max_length=30, null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    api_key = models.CharField(max_length=100, null=True, blank=True)
    sec_key = models.CharField(max_length=100, null=True, blank=True)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

	# 헬퍼 클래스 사용
    objects = UserManager()

	# 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = 'email'