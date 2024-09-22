from oop.person import Person

if __name__ == '__main__':
    person_1 = Person("Shimanta",2001,60)
    person_2 = Person("Shimanta_2",2001,60)
    person_3 = Person("Shimanta_3",2001,60)
    person_4 = Person("Shimanta_4",2001,60)

    person_1._get_all_data()
    person_2._get_all_data()
    person_3._get_all_data()
    person_4._get_all_data()

    print(">>>>>>>>>>>>>>>>>>>>>")
    person_1.set_person_name("demo")

    person_1._get_all_data()


