from select import select


class Person:
    def __init__(self,person_name: str,year_of_birth: int,ht_inches: int): # Head
        self.__name = person_name
        self.__date_of_birth = year_of_birth
        self.__height = ht_inches

    def get_Name(self):
        return f"person Name : {self.__name}"

    def set_person_name(self,edt_name: str):
         self.__name = edt_name

    def __get_calculate_height(self):
        return self.__height

    def set_person_height(self,edt_height: int):
        self.__height = edt_height

    def _get_all_data(self):
        print(f"name : {self.__name} , birth year : {self.__date_of_birth} , height : {self.__height}")