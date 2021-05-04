import re


def email_parse(email):
    RE_EMAIL = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    RE_USERNAME = re.compile(r'^[a-zA-Z0-9_.+-]+')
    RE_DOMAIN = re.compile(r'@(\b[a-zA-Z0-9-]+\b)')
    if RE_EMAIL.match(email) is None:
        raise ValueError(f'wrong email: {email}')
    else:
        for username, domain in zip(RE_USERNAME.findall(email), RE_DOMAIN.findall(email)):
            email_dict = {'username': f'{username}', 'domain': f'{domain}'}
    return email_dict


print(email_parse('someone@geekbrains.ru'))
