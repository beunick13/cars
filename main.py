# Программа, которая определяет марку автомобиля

q1 = input('Автомобиль из Европы? ')
if q1.lower() == 'да':
    q2 = input('Автомобиль из Германии? ')
    if q2.lower() == 'да':
        q3 = input('У автомобиля цветной логотип? ')
        if q3.lower() == 'да':
            print('BMW')
        else:
            q4 = input('Логотип автомобиля состоит из четырех колец? ')
            if q4.lower() == 'да':
                print('Audi')
            else:
                print('Mercedes')
    else:
        q6 = input('На логотипе автомобиля лошадь? ')
        if q6.lower() == 'да':
            print('Ferrari')
        else:
            print('Lamborghini')
else:
    q2 = input('Автомобиль из Америки? ')
    if q2.lower() == 'да':
        q5 = input('Логотип этого автомобиля похож на крест? ')
        if q5.lower() == 'да':
            print('Chevrolet')
        else:
            print('Ford')
    else:
        q4 = input('Автомоболь из Японии? ')
        if q4.lower() == 'да':
            q7 = input('Логотип автомобиля похож на букву "H"? ')
            if q7.lower() == 'да':
                print('Honda')
            else:
                print('Toyota')
        else:
            q9 = input('Автомобиль из Кореи? ')
            if q9.lower() == 'да':
                print('Hyundai')
