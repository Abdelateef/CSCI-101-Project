from CS_Project_Fuctions_Craft_Business_Services import *
User_choies =User_identefication()
if User_choies == 'craft':
    file_name = file_name()
    add_craft_date(file_name)
else:
    file_name = file_name()
    read_the_craft_date(file_name)
    chossen_name = input('please enter the craft name you need ')
    L = dic_datat(file_name,chossen_name)
    dic_new_date_to_append = (dic_data(file_name,chossen_name))
    edit_on_the_file_data(file_name,dic_new_date_to_append)
    working_price(L)
    LL = edit_rating(L)
    add_craft_date2(file_name,chossen_name,LL)