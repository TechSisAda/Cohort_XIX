************** 1ST CLASS ***************

Zero division Error, file not found error, type error, syntaxt error, indentation errors are all examples of errors.
Adding the keyword "TRY " with the follow up "EXCERPT" followed by the expected error to be able to customize the erro message
Another way to do that is to add the error in the print statement (line 6-10)
So when you dont handle the error, it comes out normally, while if youre expecting it, you can use TRY function to drop a custom ERROR message.
So Exception is the message to handle errors.
Introducing the ELSE Block is for just incase the code encounters no error, it would run successfully AND drop the custom ELSE NO-ERROR message (32-35)
Handling 2 different errors can be used with differnt EXCEPT statements and then an else statement message to conclude(56-60)
Adding the FINALLY Block, just prints the statemt in it whether or not any of the EXCEPT or ELSE statement occurs. it is not imprtant like that but good to know.
RAISE ERROR is to bring up an error statement for an exception to a particular condition set
ASSERTION ERROR acts like a checker, for a particular condition. it is usually followed by a conditional statement. it gives the error if the conditionis 
disobeyed else it runs the code.