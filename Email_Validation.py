def validate_email(email):
    email= email.strip()
    k = 0
    j = 0
    d = 0
    if len(email) >= 6:  # 1
        if email[0].isalpha():  # 2
            if "@" in email and (email.count("@") == 1):  # 3
                if email[-4] == "." or (email[-3] == "."):  # 4
                    for i in email:
                        if i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1

                    if k == 1 or j == 1 or d == 1:
                        return "❌ Invalid Email (5)"
                    else:
                        return "✅ Valid Email"
                else:
                    return "❌ Invalid Email (4)"
            else:
                return "❌ Invalid Email (3)"
        else:
            return "❌ Invalid Email (2)"
    else:
        return "❌ Invalid Email (1)"