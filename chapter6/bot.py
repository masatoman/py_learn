while True:
    command = input('あなた> ')
    print('pybot> {}'.format(command))
    if 'こんにちは' in command:
        print('コンニチワ')
    elif 'ありがとう' in command:
        print('ドウイタシマシテ')
    elif 'さようなら' in command:
        print('サヨウナラ')
        break
    else:
        print('何ヲ言ッテイルカ、ワカラナイ')

