def User_identefication ():
    x = input('user or a craft ?')
    y = ["user", "craft"]
    while x not in y:
        print('you may insert wrong choice: ')
        x = input("please enter your choice between user and craft )")
    return x

def governorate():
    x = input('please enter your governorate:(cairo_giza)')
    y = ['cairo', 'giza']
    while x not in y:
        print('you may insert unavailable governorate'
              ' or enter the governorate wrong please choose one of the appove governorate: ')
        x = input("please enter your governorate:(cairo_giza)")
    return x
def city():
    x = input("please enter your city:")
    x.strip(' ,')
    x.lower()
    y = ["alharam", "6th of october"]
    while x not in y:
        print('you may insert unavailable city or enter the city wrong please choose one of the appove city: ')
        x = input("please enter your governorate:(alharam _6th of october)")
    return x
def Residential_quarter():
    x = input("please enter your Residential_quarter:")
    x.strip(' ,')
    x.lower()
    y = ['الحي الاول', 'الحي الثاني', 'العريش', 'فاطمة رجدي']
    while x not in y:
        print('you may insert unavailable city or enter the city wrong please choose one of the appove city: ')
        x = input("please enter your governorate:(فاطمة رجدي _العريش)")
    return x
def craft():

    x = input("please enter the craft you need:(سباك_نجار_سمكري_كهربائي_ميكانيكي)")
    x.strip(' ,')
    x.lower()
    y = ['سباك', 'نجار','سمكري', 'ميكانيكي', 'كهربائي']
    while x not in y:
        print('you may insert unavailable craft or enterd the craft wrong please choose one of the appove craftes: ')
        x = input("please enter the craft you need:(سباك_نجار_سمكري_كهربائي_ميكانيكي)")
    return x
def file_name():
    s = [governorate(), city(),Residential_quarter(), craft()]
    for i in range (len(s)):
        s[i].strip(' .')
    y = '_'.join(s)
    y = y + '.txt'
    return y
def name_craft():
    x = input("please enter your name:")
    x.strip(' ,')
    x.lower()
    while x.isnumeric() == True:
        print('you may insert a wrong type of name : ')
        x = input("please enter your name)")
    return x
def cost_per_hour():
    x = input("please enter your cost per hour:")
    x.strip(' ,')
    x.lower()
    while x.isnumeric() == False:
        print('you may insert a wrong type of cost : ')
        x = input("please enter your cost per hour )")
    return x
def rating():
    x = input("please enter your rate out of 10:")
    x.strip(' ,')
    x.lower()
    while x.isnumeric() == False:
        print('you may insert a wrong type of rateing : ')
        x = input("please enter your rating)")
    return x
def tel():
    x = input("please enter your telephone number:")
    x.strip(' ,')
    x.lower()
    while x.isnumeric() == False:
        print('you may insert a wrong type of telephone number : ')
        x = input("please enter your telephone number)")
    return x
def add_craft_date(file_name):
    s = [name_craft(), ',', cost_per_hour(), ',', rating(), ',', tel(), ',', 0]
    file = open(file_name, 'a')
    file.write('\n')
    file.writelines(s)

def read_the_craft_date(file_name):
    file = open(file_name, 'r')
    for line in file:
        x = line.strip().split(',')
        for value in x:
            print(('%-15s' % (value)), end='')
        print('')
    file.close()

def dic_data(file_name,chossen_name):
    file = open(file_name, 'r')
    data = {}
    for line in file:
        vals = line.strip().split(',')
        for v in vals:
            data[vals[0]] = vals[1:]
    del data[chossen_name]
    return data

def edit_on_the_file_data(file_name, delet_data):
    file= open(file_name, 'w')
    for name in delet_data:
        Vales = [str(v) for v in delet_data[name]]
        vale_name= str(name)
        file.write('%s%s%s\n'%((vale_name), ',', ','.join(Vales)))
    file.close()

def dic_datat (file_name,chossen_name):
    file = open(file_name, 'r')
    data = {}
    for line in file:
        vals = line.strip().split(',')
        for v in vals:
            data[vals[0]] = vals[1:]
    return data[chossen_name]

def edit_rating(L):
    new_rating = float(input('rate the craft out of 10'))
    rate = ((float(L[3]) * float(L[1])) + new_rating)/(float((L[3]))+1)
    cost = ((new_rating) / 10 * 100)
    New_cost=(cost+float(L[0]))/2
    L[0]=New_cost
    L[1]=('%.2f' % (rate))
    L[3] = 1 + float(L[3])
    return L
def add_craft_date2(file_name,chossen_name,L):
    s=[chossen_name, ',', str(L[0]), ',', str(L[1]), ',', str(L[2]), ',', str(L[3])]
    file=open(file_name, 'a')
    file.writelines(s)
    file.write('\n')
def estimated_time():
    import time
    input('enter start when the craftsman arrive:')
    start_time = time.time()
    input('enter end when the craftsman finish working:')
    end_time = time.time()
    work_time = int(end_time - start_time)
    return work_time
def working_price(L):
    price = int(int((estimated_time()/(60*60)))*int(L[0]))
    print(price, "pounds")







