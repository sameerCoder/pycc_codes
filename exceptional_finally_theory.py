# Exceptional finaly theory.


For Handling exceptional in python , we use try , except,else & finally block .
The lines of code which we feel can give an excepitonal / error while run time,
are written inside try block & when the exceptional occur the message or the
handling way is written inside except block , we can have many except block
as per the exceptional cases like zerodivisionerror , valueerror etc &
we can even have a generic except block which can handle
any other exceptional cases.

The finally block will execute for sure no matter any exceptional occurs or not.
This finally block can be use for memory free purpose and
to do any necessary task.
For using finally we should use try block for sure, i.e finally will work only if
try block is present.

The else block in exception handling in getting active when there is no except block active.
i.e when we are having try,except,else & finally and we are  running our code from try block
1- and if any exceptional occur then block which will  get active are try , except & finally.
2- and if no exceptional occur then block which will get active are try,else & finally .


