

PRIMARY = 'primary'
SECONDARY = 'secondary'
SUCCESS = 'success'
DANGER = 'danger'
INFO = 'info'
WARNING = 'warning'

def get_style():
    with open('./styleV2.css', 'r') as file:
        return file.read()


if __name__ == '__main__':
    # teste
    print(get_style())
