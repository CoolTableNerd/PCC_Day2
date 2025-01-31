# Python Crash Course: Day 2
Tuesday January 28, 2025 

grateful for how Day 1 turned out as there were some challenges in how i want to structure my learning/practice as well as technical difficulties (of course) that are now ironed out. my repositories were not committing to my Github giving me error messages, believe it or not my own notes were somewhat unreadable, but i survived and moving forward should be much smoother! 

Today i'm starting Chapter 3: Introducing Lists!

as always, thanks for joining me 

# Chapter 3: Notes
List allow you to store information in one play (few items or millions)
* a collection of items in a particular order
* letters, numbers, strings can be put into a list
* square brackets indicate a list with each element separated by a comma
* good practice for the name (variable) of the list is to be plural `cars = []`

favoriteTeams = ["Los Angeles Rams", "Los Angeles Lakers", "Los Angeles Dodgers"] <br/>
print(favoriteTeams) `["Los Angeles Rams", "Los Angeles Lakers", "Los Angeles Dodgers"]`
* printing list would result in all elements of that list along with square brackets being displayed. `[] <br/>

### Accessing elements inside a List
List are ordered collections, so elements inside a list can be accessed by its index
* indexing starts with 0 meaning the first index
* the index follows the variable enclosed in square brackets
* a single element is returned without square brackets

`print(favoriteTeam[0])` result: `Los Angeles Rams `(first element in list)<br/>
`print(favoriteTeam[1])` result: `Los Angeles Lakers` (second element in list)<br/>
`print(favoriteTeam[2])` result: `Los Angeles Dodgers` (third element in list)

* string methods can be used on an index <br/>
`print(favoriteTeam[0].uppercase())`

the last element inside a list can be found with a special Python syntax
* `[-1]` as an index would print the last element inside the list <br/>
`print(favoriteTeam[-1])` result: Los Angeles Dodgers 

list elements can be used like any other variable <br/>
`print(f"my first favorite sports team was {favoriteTeam[0].title()}")` result: my first first favorite sports team was Los Angeles Rams

### Modifying Elements
Modifying Elements inside of a list allows control to change an elements value, add/remove/insert an element inside a list.

gamingSystems = ["Atari", "Sega","Xbox","Dream Cast", "PS1", "PS2","PS3","PS4"]

* changing value: elements of a list can be modified by its index <br/>
    `gamingSystems[2] = "Gameboy"` <br/>
    `print(gamingSystems[2])` – what was previously "Xbox" at the 2 index is now "Gameboy" 

adding an element into list: adding an element is called append
* when appending an element into a list, the newly added element would go to the end of the list <br/>
* to append an element, append is attached to the list variable as a method with new element in parenthesis: <br/>
    `gamingSystems.append("PsP)` – PsP is added to the end of the list <br/>
    `print(gamingSystems)`– ["Atari", "Sega","Gameboy","Dream Cast", "PS1", "PS2","PS3","PS4","PsP]

* list can start off empty and items can be appended inside
movies = [] <br/>
`movies.append("Good Will Hunting") `- adds "Good Will Hunting" at the 0 index <br/>
`movies.append("Inception")` - add "Inception" at the 1 index <br/>
`movies.append("Titanic")` - adds "Titanic" at the 2 index <br/>
`print(movies)` - prints full list: ["Good Will Hunting", "Inception", "Titanic"]<br/>

inserting an element into list: putting a new element at a specific index
* to insert an element into a list, insert is attached to the list variable as a method with the index position and new element in parenthesis (separated by comma)<br/>
    `movies.insert(1, "Dead Poet Society")` - Dead Poet Society is inserted into the index position 1
* when an element is inserted into a list, the every other element of the list is shifted to the right 1 position <br/>
    `print(movies)` - result: `["Good Will Hunting", "Dead Poet Society", "Inception", "Titanic",]`

removing an element from a list: elements that no longer serve a purpose can be removed from a list in a few ways, delete, pop and remove
* if the index (position) of the element needing removal is known, <u>delete</u> can be used - `del` goes in front of variable with the idex attached to the variable <br/>
    `del movies[3]` - movie at the 3 position (Titanic) will be deleted <br/>
    `print(movies)` - result: `["Good Will Hunting","Dead Poet Society", "Inception"]`
* the <u>pop() method</u> removes the last item inside a list and allows the option to work with the removed element. - `pop()` is attached to list variable <br/>
    `popped_movie = movies.pop()` - a new variable can be created to be used somewhere else in the program <br/>
    `print(popped_movie)` - result: `Inception` (since that was the last element inside the list) <br/>
    `print(movies)` - result: ["Good Will Hunting", "Dead Poet Society]
* the <u>pop() method</u> allows an index to be inserted inside the parenthesis to pop an element from any position <br/>
    `firstMovie = movies.pop(0)` - pops out the the movie that sits at the first index of the list <br/>
    `print(firstMovie)` - result: `Good Will Hunting ` <br/>
    `print(movies)` - `Dead Poet Society `
* if the index (position) of an element is not known, but know the value , <u>remove() method</u> is used to handle removal by value - `remove()` is attached to list variable
    * like pop, the removed element can be used throughout the program <br/>
    * remove() only removes the first occurrence of the valuable. if there are multiple, a loop is required <br/>
    `lastMovie = movies.remove("Dead Poet Society)` - result: `Dead Poet Society` would be the value of lastMovie <br/>
    `print(f"The last movie inside our list is {lastMovie.title()})` result: `The last movie inside our list is Dead Poet Society` 

list can be organized alphabetically to present information in a particular order either permanently or temporarily with methods `sort()` or `sorted`
`sort()` changes the list permanently 
* `sort()` organizes the list alphabetically - sort() is used at the end of the list variable. <br/>
    goats = ["Kobe", "Michael, "Lebron"] - original list <br/>
    `goats.sort()` - telling Python to put the list in alphabetical and will do so permanently <br/>
    `print(goats)` - results: ["Kobe", "Lebron","Michael"]

* sort() can also organize list in reverse-alphabetical order by passing the argument reverse = True into sort() method. <br/>
    `goats.sort(reverse=True) `- no spaces between <br/>
    `print(goats)` - results: ["Michael", "Lebron","Kobe"]

`sorted()` maintains the original order of a list, but allows the list to be displayed alphabetically
* sorted() goes inside a print statement with the list passed in as an argument <br/>
    `print(sorted(goats))` - results: temporarily displays the list alphabetically

printing list in reverse order using the `reverse()` method
* the list is ordered from back to front not alphabetically 
* reverse() changes the list permanently <br/>
`goats.reverse()` - flips the order of the goats list <br/>
`print(goats)` - results: ["Michel Jordan", "Lebron James", "Kobe Bryant"]
