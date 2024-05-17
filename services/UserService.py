from typing import List
from fastapi import Depends
from models.UserModel import UserModel
from repositories.UserRepository import UserRepository

class UserService:
    userRepository: UserRepository

    def __init__(
        self, userRepository: UserRepository = Depends()
    ) -> None:
        self.userRepository = userRepository
    
    def get(self, user_id: int):
        return self.userRepository.get(user_id)
    
    def getNameByUserId(self, user_id: int):
        user = self.userRepository.get(user_id)
        if not user:

            return []
        
        return getattr(user, "name")
    
    def getSubscriptionByUserId(self, user_id: int):
        user = self.userRepository.get(user_id)
        if not user:

            return []
        
        return getattr(user, "subscription")
    
    def list(self) -> List[UserModel]:
        return self.userRepository.list()
