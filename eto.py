year_str = input('あなたの生まれの年を西暦で入力してください: ')
# タプル型・変更できない
eto_tuple = ("子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥")
year = int(year_str)
num_of_eto = (year + 8) % 12
# print('あなたの干支は', eto_tuple[num_of_eto], 'です。', sep='===')
eto_name = eto_tuple[num_of_eto]
print('あなたの干支は{}です。'.format(eto_name))
