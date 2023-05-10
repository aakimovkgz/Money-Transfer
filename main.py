from service import transfer

def main():
    while True:
        user_action = input('Enter 1 to transfer\nEnter 2 to exit\n')
        if user_action == '1':
            transfer()
        elif user_action == '2':
            print('Goodbye!')
            break
        else:
            print('Inccorect command!')

if __name__ == '__main__':
    main()
