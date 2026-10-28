import os
import shutil

def env_setup():
    if os.path.isfile('.env'):
        if os.path.isfile('.env.example'):
            os.remove('.env.example')
        return
    
    if os.path.isfile('.env.example'):
        shutil.copy('.env.example', '.env')
        os.remove('.env.example')
    else:
        with open('.env', 'w') as file:
            file.write("example=1234")

env_setup()