#Developer: https://t.me/ememyersSss

import tkinter as tk
from tkinter import *
import webbrowser

def icon_settings():
    root_1 = tk.Tk()
    root_1.title('Настройка значков')
    root_1.geometry('1920x1080')
    root_1.resizable(width=True, height=True)
    canvas_1 = Canvas(root_1, width=500, height=70)
    canvas_1.create_text(250, 25, text="Настройка значков", fill="black", font=("Times", 30))
    canvas_2 = Canvas(root_1, width=3000, height=1400)
    canvas_2.create_text(470, 50, text="Для настройки значков в Astra Linux необходимо выполнить следующие шаги:", fill="black", font=("Times", 20))
    canvas_2.create_text(370, 90, text="1. Откройте файловый менеджер (например, Nautilus).", fill="black", font=("Times", 20))
    canvas_2.create_text(370, 130, text="2. Найдите папку, значок которой вы хотите изменить.", fill="black", font=("Times", 20))
    canvas_2.create_text(737, 170, text="3. Щелкните правой кнопкой мыши на файле или папке, значок которого вы хотите изменить, и выберите “Свойства”.", fill="black", font=("Times", 20))
    canvas_2.create_text(420, 210, text="4. В открывшемся окне свойств перейдите на вкладку “Значок”.", fill="black", font=("Times", 20))
    canvas_2.create_text(600, 250, text="5. Нажмите кнопку “Выбрать значок” и выберите нужный вам значок из списка доступных или", fill="black", font=("Times", 20))
    canvas_2.create_text(450, 290, text="укажите путь к файлу значка, если он находится в другом месте.", fill="black", font=("Times", 20))
    canvas_2.create_text(430, 330, text="6. После выбора значка нажмите “Закрыть” и затем “Применить”.", fill="black", font=("Times", 20))
    canvas_2.create_text(195, 370, text="7. Значок будет изменен.", fill="black", font=("Times", 20))
    button11 = tk.Button(root_1, text="Подробнее", command=icon_settings_link, font="Times 20", width=20, height=1)
    button11.pack()
    canvas_1.pack()
    canvas_2.pack()

def window_settings():
    root_2 = tk.Tk()
    root_2.title('Настройки окон')
    root_2.geometry('1920x1080')
    root_2.resizable(width=True, height=True)
    canvas_3 = Canvas(root_2, width=500, height=70)
    canvas_3.create_text(250, 25, text="Настройки окон", fill="black", font=("Times", 30))
    canvas_4 = Canvas(root_2, width=3000, height=1400)
    canvas_4.create_text(660, 50, text="Astra Linux имеет оконный менеджер Fly, который позволяет пользователям настраивать вид и поведение окон:", fill="black", font=("Times", 20))
    canvas_4.create_text(840, 90, text="1. Запустить менеджер настроек Fly - откройте главное меню и введите “fly” в строке поиска. Затем выберите “Fly” из списка результатов.", fill="black", font=("Times", 20))
    canvas_4.create_text(865, 130, text="2. Настройка положения окна - кликните правой кнопкой мыши на окне, которое вы хотите настроить, и выберите “Свойства”. В открывшемся", fill="black", font=("Times", 20))
    canvas_4.create_text(740, 170, text="окне перейдите на вкладку “Размещение”. Здесь вы можете задать положение окна на экране, а также его размер.", fill="black", font=("Times", 20))
    canvas_4.create_text(750, 210, text="3. Настройка видимости заголовка окна - перейдите в “Настройки” > “Внешний вид” > “Заголовок окна”. Здесь вы сможете", fill="black", font=("Times", 20))
    canvas_4.create_text(380, 250, text="включить или отключить видимость заголовка окна.", fill="black", font=("Times", 20))
    canvas_4.create_text(730, 290, text="4. Настройка поведения при закрытии окна - перейдите в “Настройки” > “Поведение” > “Закрыть окно” Здесь вы можете", fill="black", font=("Times", 20))
    canvas_4.create_text(550, 330, text="выбрать действие, которое будет выполняться при нажатии кнопки закрытия окна.", fill="black", font=("Times", 20))
    canvas_4.create_text(710, 370, text="5. Управление размещением и группировкой окон - перейдите в “Настройки” > “Размещение” и “Группировка окон”.", fill="black", font=("Times", 20))
    canvas_4.create_text(580, 410, text="Здесь вы сможете настроить правила размещения и группировки окон на рабочем столе.", fill="black", font=("Times", 20))
    button12 = tk.Button(root_2, text="Подробнее", command=window_settings_link, font="Times 20", width=20, height=1)
    button12.pack()
    canvas_3.pack()
    canvas_4.pack()

def monitor_settings_v2():
    root_3 = tk.Tk()
    root_3.title('Настройка монитора')
    root_3.geometry('1920x1080')
    root_3.resizable(width=True, height=True)
    canvas_5 = Canvas(root_3, width=500, height=70)
    canvas_5.create_text(250, 25, text="Настройка монитора", fill="black", font=("Times", 30))
    canvas_6 = Canvas(root_3, width=3000, height=1400)
    canvas_6.create_text(480, 50, text="Для настройки монитора в Astra Linux, вам нужно выполнить следующие шаги:", fill="black", font=("Times", 20))
    canvas_6.create_text(650, 90, text="1. Откройте меню “Пуск” и найдите “Xserver” или “Диспетчер настроек дисплея”. Запустите приложение.", fill="black", font=("Times", 20))
    canvas_6.create_text(350, 130, text="2. В открывшемся окне выберите вкладку “Дисплей”.", fill="black", font=("Times", 20))
    canvas_6.create_text(780, 170, text="3. Здесь вы можете настроить параметры вашего монитора, такие как разрешение экрана, глубина цвета и частота обновления.", fill="black", font=("Times", 20))
    canvas_6.create_text(545, 210, text="Выберите подходящие параметры для вашего монитора и нажмите “Применить”.", fill="black", font=("Times", 20))
    canvas_6.create_text(860, 250, text="4. После этого ваш монитор должен автоматически настроиться с новыми параметрами. Если этого не произошло, перезагрузите компьютер.", fill="black", font=("Times", 20))
    canvas_6.create_text(715, 290, text="5. Если вы столкнулись с проблемами, попробуйте сбросить настройки монитора на заводские. Это можно сделать в", fill="black",font=("Times", 20))
    canvas_6.create_text(360, 330, text="настройках монитора или в операционной системе.", fill="black",font=("Times", 20))
    button13 = tk.Button(root_3, text="Подробнее", command=monitor_settings_v2_link, font="Times 20", width=20, height=1)
    button13.pack()
    canvas_5.pack()
    canvas_6.pack()

def control_panel():
    root_4 = tk.Tk()
    root_4.title('Панель управления')
    root_4.geometry('1920x1080')
    canvas_7 = Canvas(root_4, width=500, height=70)
    canvas_7.create_text(250, 25, text="Панель управления", fill="black", font=("Times", 30))
    canvas_8 = Canvas(root_4, width=3000, height=1400)
    canvas_8.create_text(430, 50, text="Чтобы открыть панель управления в Astra Linux, следуйте этим шагам:",fill="black", font=("Times", 20))
    canvas_8.create_text(350, 90, text="1. Откройте меню 'Пуск' и введите “Панель управления”.",fill="black", font=("Times", 20))
    canvas_8.create_text(350, 130, text="2. В результатах поиска выберите “Панель управления”.", fill="black",font=("Times", 20))
    canvas_8.create_text(770, 170, text="3. Панель управления откроется. Здесь вы можете настроить различные параметры системы, такие как параметры пользователя,",fill="black", font=("Times", 20))
    canvas_8.create_text(380, 210, text="настройки сети, системные службы и многое другое.",fill="black", font=("Times", 20))
    button14 = tk.Button(root_4, text="Подробнее", command=control_panel_link, font="Times 20", width=20, height=1)
    button14.pack()
    canvas_7.pack()
    canvas_8.pack()

def Sound():
    root_5 = tk.Tk()
    root_5.title('Звук')
    root_5.geometry('1920x1080')
    root_5.resizable(width=True, height=True)
    canvas_9 = Canvas(root_5, width=500, height=70)
    canvas_9.create_text(250, 25, text="Звук", fill="black", font=("Times", 30))
    canvas_10 = Canvas(root_5, width=3000, height=1400)
    canvas_10.create_text(460, 50, text="Чтобы включить звук в Astra Linux, нужно выполнить следующие действия:",fill="black", font=("Times", 20))
    canvas_10.create_text(370, 90, text="1. Откройте “Настройки звука” в системных настройках.", fill="black",font=("Times", 20))
    canvas_10.create_text(485, 130, text="2. Выберите устройство вывода звука (обычно это наушники или динамики).", fill="black",font=("Times", 20))
    canvas_10.create_text(309, 170, text="3. Установите громкость на желаемом уровне.",fill="black", font=("Times", 20))
    canvas_10.create_text(380, 210, text="4. Нажмите кнопку “Применить” для сохранения настроек.", fill="black",font=("Times", 20))
    canvas_10.create_text(760, 350, text="После этого звук должен работать нормально. Если проблема не решена, проверьте подключение наушников или динамиков", fill="black", font=("Times", 20))
    canvas_10.create_text(385, 390, text="и убедитесь, что они правильно подключены к компьютеру.", fill="black",font=("Times", 20))
    button15 = tk.Button(root_5, text="Подробнее", command=sound_link, font="Times 20", width=20, height=1)
    button15.pack()
    canvas_9.pack()
    canvas_10.pack()

def network():
    root_7 = tk.Tk()
    root_7.title("Сетевое соединение")
    root_7.geometry('1920x1080')
    root_7.resizable(width=True, height=True)
    canvas_12 = Canvas(root_7, width=500, height=70)
    canvas_12.create_text(250, 25, text="Сетевое соединение", fill="black", font=("Times", 30))
    canvas_13 = Canvas(root_7, width=3000, height=1400)
    canvas_13.create_text(480, 30, text="Для настройки сетевого соединения в Astra Linux выполните следующие шаги:",fill="black", font=("Times", 20))
    canvas_13.create_text(480, 70, text="1. Запустите модуль “Системные настройки” и перейдите на вкладку “Сеть”.",fill="black", font=("Times", 20))
    canvas_13.create_text(720, 110,text="2. В открывшемся окне выберите тип соединения (Ethernet, Wi-Fi, PPPoE, VPN и т. д.) и нажмите кнопку “Изменить”.", fill="black", font=("Times", 20))
    canvas_13.create_text(655, 150,text="3. Введите параметры вашего сетевого подключения (IP-адрес, маску подсети, шлюз, DNS-серверы и т.д.).",fill="black", font=("Times", 20))
    canvas_13.create_text(580, 190,text="эти параметры можно узнать у вашего интернет-провайдера или администратора сети.",fill="black", font=("Times", 20))
    canvas_13.create_text(536, 230,text="4. После ввода всех необходимых параметров нажмите “ОК” для сохранения настроек.",fill="black", font=("Times", 20))
    canvas_13.create_text(710, 270,text="5. Если вы используете DHCP (динамическое распределение IP-адресов), выберите соответствующий тип соединения",fill="black", font=("Times", 20))
    canvas_13.create_text(330, 310, text="и нажмите “Автоматически получать адрес”.", fill="black",font=("Times", 20))
    canvas_13.create_text(675, 350,text="6. Проверьте, что подключение к интернету работает, открыв браузер и попытавшись открыть какой-либо сайт.",fill="black", font=("Times", 20))
    canvas_13.create_text(717, 390,text="7. Если подключение не работает, проверьте правильность введенных параметров и убедитесь, что ваш маршрутизатор",fill="black", font=("Times", 20))
    canvas_13.create_text(313, 430, text="или модем включен и правильно настроен.", fill="black",                        font=("Times", 20))
    canvas_13.create_text(335, 470, text="8. Если все работает, закройте окно сетевых настроек.", fill="black",font=("Times", 20))
    button16 = tk.Button(root_7, text="Подробнее", command=network_link, font="Times 20", width=20, height=1)
    button16.pack()
    canvas_12.pack()
    canvas_13.pack()

def data_and_time():
    root_8 = tk.Tk()
    root_8.title("Дата и время")
    root_8.geometry('1920x1080')
    root_8.resizable(width=True, height=True)
    canvas_14 = Canvas(root_8, width=500, height=70)
    canvas_14.create_text(250, 25, text="Дата и время", fill="black", font=("Times", 30))
    canvas_15 = Canvas(root_8, width=3000, height=1400)
    canvas_15.create_text(550, 30, text="Для настройки даты и времени в Astra Linux необходимо выполнить следующие действия:", fill="black", font=("Times", 20))
    canvas_15.create_text(570, 70, text="1. Открыть модуль “Дата и время” (обычно находится в разделе “Система” главного меню).", fill="black", font=("Times", 20))
    canvas_15.create_text(475, 110, text="2. Выбрать часовой пояс, который соответствует вашему местоположению.", fill="black", font=("Times", 20))
    canvas_15.create_text(605, 150, text="3. Настроить формат даты и времени, а также формат отображения времени в системной консоли.", fill="black", font=("Times", 20))
    canvas_15.create_text(453, 190, text="4. Если компьютер подключен к сети, можно включить автоматическую", fill="black", font=("Times", 20))
    canvas_15.create_text(455, 230, text="синхронизацию даты и времени с сервером времени в интернете.", fill="black", font=("Times", 20))
    canvas_15.create_text(520, 270, text="5. Сохранить изменения и перезапустить систему, чтобы изменения вступили в силу.", fill="black", font=("Times", 20))
    button17 = tk.Button(root_8, text="Подробнее", command=data_and_time_link, font="Times 20", width=20, height=1)
    button17.pack()
    canvas_14.pack()
    canvas_15.pack()

def start_menu():
    root_9 = tk.Tk()
    root_9.title("Меню пуск")
    root_9.geometry('1920x1080')
    root_9.resizable(width=True, height=True)
    canvas_16 = Canvas(root_9, width=500, height=70)
    canvas_16.create_text(250, 25, text="Меню пуск", fill="black", font=("Times", 30))
    canvas_17 = Canvas(root_9, width=3000, height=1400)
    canvas_17.create_text(220, 30, text="Для взаимодействия с меню пуск:", fill="black", font=("Times", 20))
    canvas_17.create_text(370, 70, text="1. Нажмите на значок “Astra” в нижнем левом углу экрана.", fill="black", font=("Times", 20))
    canvas_17.create_text(385, 110, text="2. В открывшемся меню найдите и кликните на пункт “Пуск”.", fill="black", font=("Times", 20))
    canvas_17.create_text(488, 150, text="3. Откроется окно со списком установленных приложений и системных утилит.", fill="black", font=("Times", 20))
    canvas_17.create_text(653, 190, text="4. Для поиска нужного приложения или утилиты введите название в поисковой строке в верхней части окна.", fill="black", font=("Times", 20))
    canvas_17.create_text(533, 230, text="5. Для запуска приложения или утилиты дважды кликните на нем левой кнопкой мыши.", fill="black", font=("Times", 20))
    canvas_17.create_text(850, 270, text="6. Если нужно закрепить приложение на панели задач, нажмите правой кнопкой мыши на его названии и выберите “Добавить в панель задач”.", fill="black", font=("Times", 20))
    button17 = tk.Button(root_9, text="Подробнее", command=start_menu_link, font="Times 20", width=20, height=1)
    button17.pack()
    canvas_16.pack()
    canvas_17.pack()

def file_manager():
    root_10 = tk.Tk()
    root_10.title("Менеджер файлов")
    root_10.geometry('1920x1080')
    root_10.resizable(width=True, height=True)
    canvas_18 = Canvas(root_10, width=500, height=70)
    canvas_18.create_text(250, 30, text="Менеджер файлов", fill="black", font=("Times", 30))
    canvas_19 = Canvas(root_10, width=3000, height=1400)
    canvas_19.create_text(560, 30, text="В операционной системе Astra Linux файловый менеджер открывается следующим образом:", fill="black", font=("Times", 20))
    canvas_19.create_text(370, 70, text="1. Нажмите на значок “Astra” в нижнем левом углу экрана.", fill="black", font=("Times", 20))
    canvas_19.create_text(310, 110, text="2. В открывшемся меню выберите пункт “Пуск”.", fill="black", font=("Times", 20))
    canvas_19.create_text(413, 150, text="3. В окне со списком приложений найдите “Файловый менеджер”.", fill="black", font=("Times", 20))
    canvas_19.create_text(530, 190, text="4. Нажмите на нужном приложении дважды левой кнопкой мыши, чтобы открыть его.", fill="black", font=("Times", 20))
    button18 = tk.Button(root_10, text="Подробнее", command=file_manager_link, font="Times 20", width=20, height=1)
    button18.pack()
    canvas_18.pack()
    canvas_19.pack()

def properties():
    root_11 = tk.Tk()
    root_11.title("Свойства")
    root_11.geometry('1920x1080')
    root_11.resizable(width=True, height=True)
    canvas_20 = Canvas(root_11, width=500, height=70)
    canvas_21 = Canvas(root_11, width=3000, height=1400)
    canvas_20.create_text(250, 30, text="Свойства", fill="black", font=("Times", 30))
    canvas_21.create_text(730, 70, text="В операционной системе Astra Linux для просмотра свойств файла или папки необходимо выполнить следующие действия:", fill="black", font=("Times", 20))
    canvas_21.create_text(220, 110, text="1. Откройте файловый менеджер.", fill="black", font=("Times", 20))
    canvas_21.create_text(535, 150, text="2. Перейдите в папку, содержащую файл или папку, свойства которых вы хотите узнать.", fill="black", font=("Times", 20))
    canvas_21.create_text(485, 190, text="3. Найдите нужный файл или папку и щелкните по нему правой кнопкой мыши.", fill="black", font=("Times", 20))
    canvas_21.create_text(290, 230, text="4. В контекстном меню выберите “Свойства”.", fill="black", font=("Times", 20))
    canvas_21.create_text(507, 270, text="5. В открывшемся окне будут отображаться свойства выбранного файла или папки.", fill="black", font=("Times", 20))
    button19 = tk.Button(root_11, text="Подробнее", command=properties_link, font="Times 20", width=20, height=1)
    button19.pack()
    canvas_20.pack()
    canvas_21.pack()


#О программе------------------------------------------------------------------------------------------------------------

def about_programm():
    root_6 = tk.Tk()
    root_6.title("О программе")
    root_6.geometry('600x600')
    canvas_11 = Canvas(root_6, width=600, height=600)
    canvas_11.create_text(300, 30, text="Важная информация", fill="black", font=("Times", 30))
    canvas_11.create_text(290, 80, text="Данная программа создана для пользователей, имеющих базовые", fill="black", font=("Times", 15))
    canvas_11.create_text(290, 100, text="знания в работе компьютера, но не имеющих понимания работы", fill="black", font=("Times", 15))
    canvas_11.create_text(290, 120, text="на ОС Astra Linux!", fill="black", font=("Times", 15))
    canvas_11.pack()

#Дополнительные функции-------------------------------------------------------------------------------------------------

def icon_settings_link():
    webbrowser.open("https://tour.astralinux.ru/help/setup/fly-admin-theme.html")

def window_settings_link():
    webbrowser.open("https://tour.astralinux.ru/help/setup/fly-admin-winprops.html")

def monitor_settings_v2_link():
    webbrowser.open("https://tour.astralinux.ru/help/setup/fly-admin-screen.html")

def control_panel_link():
    webbrowser.open("https://tour.astralinux.ru/help/setup/fly-admin-center.html")

def sound_link():
    webbrowser.open("https://wiki.astralinux.ru/pages/viewpage.action?pageId=1212485")

def network_link():
    webbrowser.open("https://wiki.astralinux.ru/pages/viewpage.action?pageId=3277370")

def data_and_time_link():
    webbrowser.open("https://tour.astralinux.ru/help/setup/fly-admin-date.html")

def start_menu_link():
    webbrowser.open("https://tour.astralinux.ru/help/other/fly-start-panel.html")

def file_manager_link():
    webbrowser.open("https://tour.astralinux.ru/help/system/fly-fm.html")

def properties_link():
    webbrowser.open("https://uchet-jkh.ru/i/failovaya-sistema-astra-linux-osobennosti-i-preimushhestva/")
#Главная страница-------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title('Программа - помощник')
root.geometry('1920x1080')
root.resizable(width=True, height=True)

canvas = Canvas(root, width=500, height=70)
canvas.pack()
canvas.create_text(250, 25, text="Что вас интересует?", fill='black', font=("Times", 30))

button1 = tk.Button(root, text="Настройка значков", command=icon_settings, font="Times 20", width=20, height=1)
button1.pack()
button2 = tk.Button(root, text="Настройки окон", command=window_settings, font="Times 20", width=20, height=1)
button2.pack()
button3 = tk.Button(root, text="Настройка монитора", command=monitor_settings_v2, font="Times 20", width=20, height=1)
button3.pack()
button4 = tk.Button(root, text="Панель управления", command=control_panel, font="Times 20", width=20, height=1)
button4.pack()
button5 = tk.Button(root, text="Звук", command=Sound, font="Times 20", width=20, height=1)
button5.pack()
button6 = tk.Button(root, text="Сетевое соединение", command=network, font="Times 20", width=20, height=1)
button6.pack()
button7 = tk.Button(root, text="Дата и время", command=data_and_time, font="Times 20", width=20, height=1)
button7.pack()
button8 = tk.Button(root, text="Меню пуск", command=start_menu, font="Times 20", width=20, height=1)
button8.pack()
button9 = tk.Button(root, text="Менеджер файлов", command=file_manager, font="Times 20", width=20, height=1)
button9.pack()
button10 = tk.Button(root, text="Свойства", command=properties, font="Times 20", width=20, height=1)
button10.pack()

#-----------------------------------------------------------------------------------------------------------------------

about_programm()
root.mainloop()