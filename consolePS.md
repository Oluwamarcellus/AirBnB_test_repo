# PseudoCode
## import all modules because we will use them

### check if the line empty
    * print(....)
### check if the line doesn't exist in class
    print(...)
### check the line input, if it is equal to the name of one of our classess
    * Create and obj and call the class
    * print id
    * storage.save()

# do_show

### input qwill be show (class name), so we need to divie it
### args = line.split()
### Checking if line is empty
 	* print("** class name missing **)
### checking if the class doesn't exist
    * if arg[0](classs name) not in comd.classess:
    * print("** class doesn't exist **")
### check if the arg less than two, if true
    *print("** instance id missing **)
### else:
    * save the arg[0], class name inside a vairable
    * save arg[1] the id in another variable
    * key variable to save both of them 
### try:
    * print(all)
### except keyError:
    * print("** no instance found **)
### if the instance of the class doesn't exist

### def do_destroy(self, line):
    * split the line
### checking if the line is empty
    * print('** class name missing **')
### checkfing if the class not in classess
    * if arg[0] not in cmd.classes
        * print("** class doesn't exist ** ")
### checking for the classname, arg < 2
     * print("'** instance id missing **')
### else:
    * save the classname in a var, id in a var, and var for both
### try:
    * delete them
### except:
    * print(** no instance found **)

### def do_update(self, line):

### split the line
### check if the line empty
    * print("** class name missing **")
### check if the class is not in classes
    * print("** class doesn\'t exist **)
### check if the leng less then 2
    * if true
    * print("** instance id missing **")
### else:
### if len less than 3
    * print("** attribute name missing **")
### if len less than 4
    * print("** value missing **")
### save, class name, id, attribute name, attr val in variables
### list of id, created_at, updated_at => can't be update
### for loop to check if it is in one of them so
    * print("** attribute can\'t be updated **")
    * return;

### On the attr value, here is the checking of the first, last letter in attr val
    * check if there is any "", or ''
### if it not exist
    * print("** A string argument must be between \ double quotes **")
	
### value = from 1:-1, hold "" or ''
### try:
###    loop over the valie
    * checking for the .
### if it is exist it's mean it's a float number
        * value = float(value)
### if it doesn't exist
    * value = int(value)
### except
###    ValueError:	
        * print(:"** A string argument must \ be between double quote **")

### for the attr name itself
    * checking if the first and last letter is "" or '' 
    * if they aren't equal to "" or '
    * print("** A string argument must be between \ double quotes **")
    * return;
### attr = attr[1:-1]
### """String validity is end"""

### save the classname, ".", id in one var

### try:
	* Update
### except keyError:
    * print('** no instance found **')
