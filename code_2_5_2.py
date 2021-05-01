names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt',
         'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt',
         'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt',
         'fhjhafhdfa.txt']
random_name = random.choice(names)
f = open(f'{random_name}', 'w')
f.close()


def func(list_1):
    for name in list_1:
        try:
            f = open(f'{name}', 'r+')
            f.write('My name is Sultan!')
            f.close()
            print(f'Your name is written in the file {name}')
        except FileNotFoundError:
            print(f'There is no file with this name: {name}')
        continue
func(names)
