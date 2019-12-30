import t


filename = 'main.py'


try: 
    with open(filename, 'w') as file: 
        file.write(t.EMAIL_ADDRESS)
except Exception as e:
    print('Exception: {}'.format(e))
    
