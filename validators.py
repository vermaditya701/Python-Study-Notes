import re   #regex module 
#?regex module is used for string pattern matching and validation


def is_valid_email(email):
    """Basic email check: something@something.tld (tld >= 2 chars)."""
    return bool(re.match(r"[^@]+@[^@]+\.[^@]{2,}", str(email).strip()))


def is_valid_mobile(phone):
    """Exactly 10 digits (simple rule)."""     #?docstring(""" """) used to describe function & its purpose  . It is accesibleble at runtime
    phone = str(phone).strip()
    return len(phone) == 10 and phone.isdigit()


def is_strong_password(password):
    """>=8 chars, has upper, lower, digit, special."""
    pwd = str(password)
    return (
        len(pwd) >= 8
        and any(c.isupper() for c in pwd)
        and any(c.islower() for c in pwd)
        and any(c.isdigit() for c in pwd)
        and any(not c.isalnum() for c in pwd)
    )

