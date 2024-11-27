#!/usr/bin/env python3

if __name__ == "__main__":
    from api.v1.auth.basic_auth import BasicAuth
    from  models.user import User

    ba = BasicAuth()
    res = ba.user_object_from_credentials("ul@gmaail.com", "pwd")
    if res is not None:
        print("user_object_from_credentials must return None if 'user_email is not linked to nay user")
        exit(1)
    print("OK", end="")
    
