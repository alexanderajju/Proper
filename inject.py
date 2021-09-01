import hashlib
import requests

from cmd import Cmd

url = 'http://10.10.10.231'

class Term(Cmd):
    prompt = 'please Subscribe =>'

    def __init__(self):
        self.s = requests.Session()
        self.auth()
        super().__init__()

    def auth(self):
        self.s.get(url)
        creds = {
                'username':'vikki.solomon@throwaway.mail',
                'password': 'password1'
                }
        self.s.post(url + '/licenses/', data = creds)

    def default(self, args):
        salt = (secure_parm(args))
        r = self.s.get(url + f'/licenses/licenses.php?theme={args}&h={salt}')
        print(r.text)


    def do_exit(self, args):
        return True


def secure_parm(arg):
    hash = hashlib.md5()
    salt = 'hie0shah6ooNoim'
    hash.update((salt + arg).encode())
    return (hash.hexdigest())




term = Term()
term.cmdloop()
