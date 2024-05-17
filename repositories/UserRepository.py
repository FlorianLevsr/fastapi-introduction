from typing import List, Union
from models.UserModel import UserModel
from data.users_db import users_db

class UserRepository:

    def __init__(self) -> None:
        self.data = users_db

    def get(self, user_id: int) -> Union[UserModel, List]:
        user = next((item for item in self.data if item["id"] == user_id), None)

        if not user:
            return []

        return UserModel(
            user["id"],
            user["name"],
            user["subscription"]
        )
    
    def list(self) -> List[UserModel]:
        list = []
        for user in self.data:
            print(user)
            list.append(
                UserModel(
                    user["id"],
                    user["name"],
                    user["subscription"]
                )
            )

        return list
