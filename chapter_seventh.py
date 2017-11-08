import re

def check_pw(password):
    mo1 = re.compile(r'[A-Z]')
    mo2 = re.compile(r'[a-z]')
    mo3 = re.compile(r'\d')
    if len(password) >= 8 and all([mo1.search(password),
                mo2.search(password), mo2.search(password)]):
        return True
    return False

print(check_pw('Pass1234'))
print(check_pw('124314212'))


def strip_other(str1, replace=None):
    if not replace:
        mo = re.compile(r'^\s*|\s*$|^\s*.*\s*$')
        return str(mo.sub('', str1))
    else:
        mo = re.compile(replace)
        return str(mo.sub('', str1))

print(strip_other('  strww  '))
print(strip_other('  strww'))
print(strip_other('strww  '))
print(strip_other('you are alway on my mind!', 'you'))