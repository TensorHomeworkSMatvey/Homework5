def password(s):
    try:
        if len(s) < 6: return False
        elif not any(map(str.isdigit, s)): return False
        elif s.isdigit(): return False
        elif 'password' in s.lower(): return False
        else: return True
    except: return "Ошибка! Введите строку"

t = "PasSworD145rdrt53"
print("Результат программы:", password(t))