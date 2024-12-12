import random

class Student:
    def __init__(self, name, knowledge=0, happiness=100, money=50):
        self.name = name
        self.knowledge = knowledge
        self.happiness = happiness
        self.money = money

    def study(self):
        print(f"{self.name} вчиться.")
        self.knowledge += random.randint(1, 5)  # Знання зростають
        self.happiness -= random.randint(1, 3)  # Щастя зменшується
        self.check_status()

    def work(self):
        print(f"{self.name} працює.")
        self.money += random.randint(10, 30)  # Заробляє гроші
        self.happiness -= random.randint(2, 5)  # Щастя зменшується
        self.check_status()

    def rest(self):
        print(f"{self.name} відпочиває.")
        self.happiness += random.randint(3, 7)  # Щастя зростає
        self.money -= random.randint(5, 15)  # Витрачаються гроші
        self.check_status()

    def check_status(self):
        if self.money <= 0:
            print(f"{self.name} не має грошей і змушений йти на роботу.")
            self.work()
        if self.happiness <= 20:
            print(f"{self.name} почувається нещасним і вирішує відпочити.")
            self.rest()
        if self.knowledge <= 30:
            print(f"{self.name} відчуває, що має вчитися більше.")
            self.study()

        # Обмежуємо значення атрибутів у межах 0-100
        self.knowledge = max(0, min(100, self.knowledge))
        self.happiness = max(0, min(100, self.happiness))
        self.money = max(0, self.money)  # Гроші можуть бути тільки >= 0

    def live_a_day(self):
        print(f"\nДень із життя {self.name}.")
        action = random.choice(['study', 'work', 'rest'])
        if action == 'study':
            self.study()
        elif action == 'work':
            self.work()
        elif action == 'rest':
            self.rest()

    def live_a_year(self):
        for day in range(1, 366):  # 365 днів у році
            print(f"\nДень {day}")
            self.live_a_day()

        print(f"\nРік закінчився для {self.name}.")
        print(f"Підсумкові результати: знання = {self.knowledge}, щастя = {self.happiness}, гроші = {self.money}")

# Приклад створення студента та проживання року
if __name__ == "__main__":
    student = Student(name="Олександр")
    student.live_a_year()
