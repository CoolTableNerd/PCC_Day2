"""
3-1. Names: Store the names of a few of your friends in a list called names. 
Print each person’s name by accessing each element in the list, one at a time.

"""
names = ["Demetrius", "Kiana", "Diana",]
print(names[0])
print(names[1])
print(names[2])

print("\n")

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
The text of each message should be the same, but each message should be personalized with the person’s name.

"""
print(f"hey, {names[0].title()}! love you!")
print(f"hey, {names[1].title()}! love you!")
print(f"hey {names[2].title()}! love you!\n")

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

"""
cars = ["Honda", "Saturn", "Lamborghini","Bentley"]
print(f"so far i have owned three calls with two of them being {cars[0].title()}, Accord and Clarity! i love that car brand")
print(f"my first car was a {cars[1].title()} and i believe it was a lemon. i was just exited to drive around")
print(f"a {cars[2].title()} is my dream car.")
print(f"i always loved the dashboard and steering wheel of {cars[3].title()}!\n")

"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
Make a list that includes at least three people you’d like to invite to dinner. 
Then use your list to print a message to each person, inviting them to dinner.

"""
guestList = ["Kobe Bryant", "Leonardo Dicaprio","Kanye West", "Steve Jobs"]

print(f"Good morning, {guestList[0].title()}! You're invited to dinner!")
print(f"Good morning, {guestList[1].title()}! You're invited to dinner!")
print(f"Good morning, {guestList[2].title()}! You're invited to dinner!")
print(f"Good morning, {guestList[3].title()}! You're invited to dinner!\n")

"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
     You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.

"""
uninvited = guestList.pop(-1)
print(f"unfortunately, {uninvited} can not attend the dinner\n") 
replacementGuest = guestList.insert(3,"Bill Gates")
print(f"{guestList[3].title()} will fill in for {uninvited} who couldn't make the dinner.\n")

print(f"Good morning, {guestList[0].title()}! You're invited to dinner!")
print(f"Good morning, {guestList[1].title()}! You're invited to dinner!")
print(f"Good morning, {guestList[2].title()}! You're invited to dinner!")
print(f"Good morning, {guestList[3].title()}! You're invited to dinner!\n")

"""
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.

"""
print(f"Good morning, {guestList[0].title()}! scoot over, we have more guest arriving.")
print(f"Good morning, {guestList[1].title()}! scoot over, we have more guest arriving.")
print(f"Good morning, {guestList[2].title()}! scoot over, we have more guest arriving.")
print(f"Good morning, {guestList[3].title()}! scoot over, we have more guest arriving.\n")

guestList.insert(0,"Sandra")
guestList.insert(2, "Demetrius")
guestList.append("Marshall Faulk")

print(f"Good morning, {guestList[0].title()}! You're invited to dinner!")
print(f"Good morning, {guestList[1].title()}! You're invited to dinner!")
print(f"Good morning, {guestList[2].title()}! You're invited to dinner!")
print(f"Good morning, {guestList[3].title()}! You're invited to dinner!")
print(f"Good morning, {guestList[4].title()}! You're invited to dinner!")
print(f"Good morning, {guestList[5].title()}! You're invited to dinner!")
print(f"Good morning, {guestList[6].title()}! You're invited to dinner!\n")

"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

"""

print("Due to the ordered table not being able to arrive on time, we'll have to un-invite some guest. hope you understand.\n")

removedGuest = guestList.pop()
print(f"sorry, {removedGuest}")

removedGuest = guestList.pop()
print(f"sorry, {removedGuest}")

removedGuest = guestList.pop()
print(f"sorry, {removedGuest}")

removedGuest = guestList.pop()
print(f"sorry, {removedGuest}")

removedGuest = guestList.pop()
print(f"sorry, {removedGuest}")

guestList.remove("Kobe Bryant")
del guestList[0]
print(guestList)

print("\n")

"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.

"""
destinations = ["Tokyo", "Mexico", "Indiana","Texas","Brazil"] #bullet 0
print(destinations) #bullet 1
print(sorted(destinations)) #bullet 2
print(destinations) #bullet 3
print(sorted(destinations, reverse = True)) #bullet 4
print(destinations)

destinations.sort()
print(destinations)

destinations.reverse()
print(destinations)

destinations.sort()
print(destinations)

destinations.sort(reverse=True)
print(destinations)

"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7
use len() to print a message indicating the number of people you’re inviting to dinner.

"""

print(f"total invites: {len(guestList)}\n")
