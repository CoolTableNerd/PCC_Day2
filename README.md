# Python Crash Course: Day 2
Tuesday January 28, 2025 

grateful for how Day 1 turned out as there were some challenges in how i want to structure my learning/practice as well as technical difficulties (of course) that are now ironed out. my repositories were not committing to my Github giving me error messages, believe it or not my own notes were somewhat unreadable, but i survived and moving forward should be much smoother! 

Today i'm starting Chapter 3: Introducing Lists!

as always, thanks for joining me 

### Python Lists (Chapter 3)

#### **1. Introduction to Lists**
- **Definition**: Ordered collections of items (strings, numbers, etc.) stored in square brackets `[]`.
- **Naming Convention**: Use plural names for lists (e.g., `teams`, `movies`).
- **Example**:
  ```python
  favorite_teams = ["Los Angeles Rams", "Los Angeles Lakers", "Los Angeles Dodgers"]
  print(favorite_teams)  # Output: ["Los Angeles Rams", "Los Angeles Lakers", "Los Angeles Dodgers"]
  ```

---

#### **2. Accessing List Elements**
- **Indexing**: Starts at `0` for the first element. Use `[-1]` for the last element.
  ```python
  print(favorite_teams[0])   # Output: Los Angeles Rams
  print(favorite_teams[-1])  # Output: Los Angeles Dodgers
  ```
- **String Methods on Elements**:
  ```python
  print(favorite_teams[0].upper())  # Output: LOS ANGELES RAMS
  ```

---

#### **3. Modifying Lists**
- **Changing Elements**:
  ```python
  gaming_systems = ["Atari", "Sega", "Xbox"]
  gaming_systems[2] = "Gameboy"  # Replaces "Xbox" with "Gameboy"
  ```
- **Adding Elements**:
  - `append()`: Adds to the end.
    ```python
    movies = []
    movies.append("Good Will Hunting")  # ["Good Will Hunting"]
    ```
  - `insert()`: Adds at a specific index.
    ```python
    movies.insert(1, "Dead Poet Society")  # ["Good Will Hunting", "Dead Poet Society"]
    ```
- **Removing Elements**:
  - `del`: Remove by index.
    ```python
    del movies[0]  # Removes "Good Will Hunting"
    ```
  - `pop()`: Remove and return the last element (or by index).
    ```python
    popped_movie = movies.pop(1)  # Removes "Dead Poet Society"
    ```
  - `remove()`: Delete by value (first occurrence).
    ```python
    movies.remove("Inception")  # Removes "Inception"
    ```

---

#### **4. Sorting Lists**
- **Permanent Sorting**:
  ```python
  goats = ["Kobe", "Michael", "Lebron"]
  goats.sort()  # Sorts alphabetically: ["Kobe", "Lebron", "Michael"]
  goats.sort(reverse=True)  # Reverse-alphabetical: ["Michael", "Lebron", "Kobe"]
  ```
- **Temporary Sorting**:
  ```python
  print(sorted(goats))  # Original list unchanged
  ```
- **Reversing Order**:
  ```python
  goats.reverse()  # Reverses list permanently: ["Michael", "Lebron", "Kobe"] → ["Kobe", "Lebron", "Michael"]
  ```

### Small Project: Task List Manager

#### **Objective**  
Create a program to manage a dynamic to-do list. Users can add, remove, and organize tasks.

#### **Requirements**
1. **Task Operations**:
   - Start with an empty list: `tasks = []`.
   - Add tasks using `append()` or `insert()`.
   - Remove tasks using `del`, `pop()`, or `remove()`.
   - Allow users to sort tasks alphabetically (permanently or temporarily) and reverse the order.

2. **User Interaction**:
   - Print the current task list after each action.
   - Include a menu for actions:  
     ```
     1. Add Task
     2. Remove Task by Index
     3. Remove Task by Name
     4. Sort Tasks (A-Z)
     5. Reverse Task Order
     6. Exit
     ```
#### **Steps**
1. Initialize an empty list `tasks`.
2. Use a `while` loop to display the menu and process user input.
3. Implement functions for each operation (e.g., `add_task()`, `remove_task_by_index()`).
4. Handle edge cases (e.g., invalid indexes, empty lists).

---

This project reinforces list manipulation (adding, removing, sorting) and provides hands-on practice with loops, conditionals, and user interaction! 🐍