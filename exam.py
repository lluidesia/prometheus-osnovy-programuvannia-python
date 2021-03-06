'''
ІНДІАНА ДЖОНС ТА ПЕРСТЕНЬ ЦЗУНЬ-СИ

На одному східному ринку до рук Індіани Джонса потрапив цікавий документ. У ньому згадувався загадковий перстень, 
який належав славетному військовому стратегу стародавності Цзунь-Си і, за словами автора, деяким чином увібрав частку його мудрості.
Ймовірно, далі перстень передавався від одного імператора Китаю до іншого і врешті-решт був похований разом з одним із них. 

Для того, щоб перевірити цю інформацію, необхідно навідатися в імператорські усипальні, які являють собою лабіринт з кімнат і переходів. 
Влада Китаю не дозволяє проводити там жодних досліджень. Але через знайомого в міністерстві культури доктор Джонс отримав дозвіл на запуск 
робота-дослідника для пошуку артефакта.

  

Вам необхідно скласти функцію maze_controller() для керування роботом. Відомо, що лабіринт є квадратним, десь в ньому має знаходитися 
перстень Цзунь-Си і все. План лабіринту та його точні розміри, як і точне місцезнаходження входу та шуканого артефакту, невідомі.

На жаль, замість новітнього ВОЛЛІ-3000 доктору Джонсу продали більш дешевий БАЛЛІ-3000, недоліками якого є дуже обмежений радіус дії 
сенсорів і відсутність вбудованої функції складання карт. Тому наявний робот "бачить" лише те, що знаходиться лише безпосередньо перед 
ним і визначає наявність перешкод на дорозі лише при безпосередньому контакті з ними.

У робота є об'єктно-орієнтований інтерфейс управління із наступними методами:

    go() -- проїхати на поле вперед, повертає True або False в залежності від того, чи вдалося проїхати (наприклад, перед роботом може 
    знаходитися стіна). Якщо проїхати неможливо, робот залишається на місці.
    turn_left() -- повернути на 90 градусів проти годинникової стрілки.
    turn_right() -- повернути на 90 градусів за годинниковою стрілкою.
    found() -- перевіряє, чи знаходиться перстень у зоні видимості робота.
В якості єдиного аргументу при виклику функції maze_controller() передається ініціалізований об'єкт класу MazeRunner для управління 
роботом. Функція maze_controller нічого не повертає за допомогою оператора return. Але в результаті її роботи робот має бути переведений 
у поле лабіринту, в якому знаходиться шуканий артефакт (вважати, що артефакт завжди наявний в лабіринті). 
Тобто після виклику maze_controller(maze_runner), метод об'єкту maze_runner.found() повинен повертати True. 
Прямий доступ до зображення лабіринту заборонено.

І ще раз:

1. Написати функцію maze_controller(mr), єдиним аргументом якої є вже ініціалізований (перевіряльником) об'єкт класу MazeRunner. Функція нічого не повертає, але в результаті її виконання робот має бути переведений в поле лабіринту, де знаходиться артефакт -- тобто після виклику функції maze_controller(maze_runner), метод об'єкту maze_runner.found() повинен повертати True.
2. Прямий доступ до зображення лабіринту заборонено.
3. Ваш розв'язок повинен містити лише функцію maze_controller і нічого крім неї. Жодного введення або виведення даних крім взаємодії з переданим об'єктом бути не повинно. Об'єкт керування роботом створюється та ініціалізується автоматичним перевіряльником поза межами вашої функції.
4. Як завжди, для коректної роботи тестувальника ваш код не повинен містити коментарів, кирилиці, перевірок на те, чи є програма головним модулем, підключення нестандартних модулів, функції exit().
(9/30 балів)
'''

def maze_controller(robot):
    i = 0
    while(robot.found() == False):
        print(i)
        i=i+1
        robot.go()
        robot.turn_left()
        if robot.go() == False:
            robot.turn_right()
        if robot.go() == False:
            robot.turn_right()
        if robot.found() == True:
            break
        if i>1000000:
            break


