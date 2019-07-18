def heisei_command(command):
    heisei, year_str = command.split()
    year = int(year_str)
    if year >= 1989:
        heisei_year = year - 1988
        response = '西暦{}ハ、平成{}年デス'.format(year, heisei_year)
    else:
        response = '西暦{}ハ、平成ではありません'.format(year)
    return response


def length_command(command):
    cmd, text = command.split()
    length = len(text)
    response = '文字列ノ長サハ {} 文字デス'.format(length)
    return response


text_file = open('pybot.txt', encoding='utf-8')
raw_data= text_file.read()
text_file.close()
lines = raw_data.splitlines()
print(lines)

bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response


while True:
    command = input('pybot > ')
    response = ''
    for key in bot_dict:
        if key in command:
            response = bot_dict[key]
            break
    if '平成' in command:
        response = heisei_command(command)
    if '長さ' in command:
        response = length_command(command)
    
    if not response:
        response = '何ヲイッテルカ、ワカラナイ'
    print(response)

    if 'さようなら' in command:
        break
