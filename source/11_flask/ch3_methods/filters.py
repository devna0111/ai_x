def mask_password(password) :
    return "*" * len(password)

if __name__ == "__main__" :
    password = input('패스워드 입력 :')
    print(mask_password(password))