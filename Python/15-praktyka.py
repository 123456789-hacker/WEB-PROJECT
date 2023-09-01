
unser_choice = -1

tasks = []
tasks.append("Wynieść śmieci")
tasks.append("Posprzątać biurko")
tasks.append("Nauka pythona")

def show_tasks():
      task_index = 0
      for task in tasks:
       print(task + "[" + str(task_index) + "]")
      task_index += 1
 
def add_task():
      task = input("Wpisz treść zadania: ")
      tasks.append(tasks)
      print("Dodano zadanie!")

def delete_task():
      task_index = int(input("Podaj index zadania do usunięcia: "))

      if task_index < 0 or  task_index > len(tasks) -1:
            print("Zadanie o tym indexie nie istnieje! ")
            return
      
      tasks.pop(task_index)
      print("Usunięto zadanie! ")

def save_tasks_to_file():
      file = open("takst.txt", "w")
      for task in tasks:
            file. write(task+ "\n")
      file.close





while unser_choice != 5:
      if unser_choice == 1:
            show_tasks()
      
      print(tasks)
          
      
      if unser_choice == 2:
            add_task()
            
      if unser_choice == 3:
            delete_task(1)

      if unser_choice == 4:
            save_tasks_to_file()

      def load_tasks_from_file():
            file = open("tasks.txt")

            for line in file.readlines():
                  tasks.append(line.strip())
            
            file.close
      

      
      print()
      print("1. Pokaż zadania")
      print("2. Dodaj zadania")
      print("3. Usuń zadania")
      print("4. Zapisz zmiany w pliku")
      print("5. Wyjdź")

      unser_choice = int(input("Wybierz liczbę: "))
      print()