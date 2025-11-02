# Python Inheritance Exercise

This project demonstrates **inheritance, encapsulation, and protected methods** in Python using a parent class `Person` and three child classes: `Managers`, `Employees`, and `Apprentices`.

---

## 🧑‍💼 Person Class
- **Common fields:** `name`, `last_name`, `personnel_code`  
  - `personnel_code` is used for managers and employees; default empty for apprentices.  
- **Instance tracking:** Class variable `count` keeps track of the number of objects.  
- **Encapsulation:** `personnel_code` is private, accessible via `get_personnel_code` and `set_personnel_code`.  
- **Automatic formatting:** Names are converted to uppercase if needed (`caps_lock` method).

---

## 👔 Managers Class
- Inherits from `Person` using `super()` to initialize shared fields.  
- **Display info:** `show_info_manager` prints shared info first, then manager-specific details as both **string** and **list**.

---

## 🧑‍💻 Employees Class
- Similar structure to `Managers`.  
- **Grading system:** Accepts `[A, B, C, D]` grades; `input_grade` validates input and converts lowercase to uppercase.  
- **Display info:** `show_info_employee` prints shared and employee-specific info.

---

## 🧑‍🎓 Apprentices Class
- Inherits from `Person`.  
- **Training duration:** Fixed at 12 months.  
- **Display info:** `show_apprentice_info` prints shared and apprentice-specific info.

---



## **Usage Example**

```python
M1=Managers(1000,'Vahideh','Rajaeipour',200000000)
M1.show_info_manager()
print(M1.get_personnel_code())
M1.set_personnel_code(1001)
print(M1.get_personnel_code())
M1.show_info_manager()
M2=Managers(1002,'Saeideh','Rajaeipour',250000000)
M2.show_info_manager()
M3=Managers(1003,'Ghazaleh','Rajaeipour',700000000)
M3.show_info_manager()

E1=Employees(1004,'Mehri','Mousavi','a')
E1.show_info_employee()

A1=Apprentices('Ahmad','Radmanesh')
A1.show_apprentice_info()
