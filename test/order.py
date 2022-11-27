import random

#변수 초기화
menu = {1: '치킨 슬라이스', 2: '치킨 베이컨 아보카도', 3: '머쉬룸',
        4: '쉬림프', 5:'로티세리 바비큐 치킨', 6: '이탈리안 비엠티',
        7: '로스트 치킨', 8:'에그마요', 9: 'K-바비큐', 
        10: '풀드 포크 바비큐', 11: '비엘티', 12: '햄',
        13: '참치', 14: '써브웨이 클럽', 15: '베지',
        16: '스테이크 & 치즈', 17: '스파이시 이탈리안', 18: '치킨 데리야끼',
        19: '터키',20: '터키 베이컨 아보카도'}

bread = ['허니오트','하티','위트','파마산 오레가노','화이트','플랫브레드']

vegetable = ['양상추', '토마토', '오이', '피망', '양파', '피클',
                '올리브', '할라피뇨']
sauce = ['랜치', '마요네즈', '스위트 어니언', '허니 머스타드',
        '스위트 칠리', '핫 칠리', '사우스웨스트 치폴레', '머스타드',
        '홀스래디쉬','스모크 바비큐']

lst = []

def choose():
    r_menu = random.choice(list(menu.values())) #values() or items()?
    r_bread = random.choice(bread)
    r_vegetable = random.sample(vegetable, 3)
    r_sauce = random.sample(sauce, 3)

    lst = r_bread.append(r_sauce)
    # lst += r_menu
    # lst += r_bread
    # lst += r_vegetable
    # lst += r_sauce
    print(lst)

choose()

def order():
    print('order')