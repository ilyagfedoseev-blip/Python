emails = {'mgu.edu': ['andrei_serov', 'elena_belova', 'kirill_stepanov'],
'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
users = []
for key in emails:
    for name in emails[key]:
        users.append(name + '@' + key)

print(*sorted(users), sep='\n')