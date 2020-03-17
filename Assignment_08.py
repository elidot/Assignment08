#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Eliana A-Dotson, 2020-March-13, Recycled old code, refactoring 
# Eliana A-Dotson, 2020-March-14. Generation of Constructors, Attributes 
# Eliana A-Dotson, 2020-March-14. Editing after email from Mr Kloss - Defined class CD data about a CD
# Eliana A-Dotson, 2020-March-16. Implementing Load and Save File codes 
#                               . Testing/cleaning and documenting 
#------------------------------------------#
# TO-DOne Add Code to the CD class  # No methods at this time?????
class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods: 
        TBI
    """
    
    #Constructor
    def __init__(self, cd_id,cd_title,cd_artist):
        #----Protected Attributes----#
        self.__cd_id = int(cd_id)
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
   #Properties 
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self,value):
        try:
            self.__cd_id = int(value)
        except ValueError:
            raise ValueError("CD ID must be an integer")

    @property
    def cd_title(self):
        return self.__cd_title

    @property
    def cd_artist(self):
        return self.__cd_artist
    
    def __str__(self):
        return int(self.__cd_id)+'/'+str(self.__cd_title) +'/'+str(self.__artist)

#Validating: 
newcd= CD(1,"Reik","Ojos Negros") 
#print(newcd.cd_id,newcd.cd_artist,newcd.cd_title)
#print(newcd.cd_id)
print('{}\t{} (by:{})'.format(newcd.cd_id, newcd.cd_title, newcd.cd_artist))

               
#METHODS
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TO-DOne Add code to process data from a file - READ
    # TO-DOne Add code to process data to a file - WRITE
    #pass

    @staticmethod
    def load_inventory(file_name,lst_Inventory):   
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from

        Returns:
            lst_Inventory (list of dict): a list of CD objects
        """
        try:
            objFile = open(file_name, 'r')
            #lst_Inventory.clear()  # this clears existing data and allows to load data from file
            for attr in objFile:
                cd_attr=(attr.cd_id, attr.cd_title,attr.cd_artist)
                lst_Inventory.append(cd_attr)
            objFile.close()
        except FileNotFoundError as err:
            print(err, "The file {} could not be loaded".format(file_name))
        finally:
            return lst_Inventory


# TO-DOne Add code to process data to a file - WRITE
 ### 
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        
        """Function to write data to file from list

        Opens the data file with option to write, loops through the new row added to list 
        and adds the new entry to file
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        Retsaviurns:
            None, Write to file 
        """
        with open(file_name, 'w') as objFile:
            for row in lst_Inventory:
                newcd=(str(row.cd_id),row.cd_artist,row.cd_title)
                objFile.write(','.join(newcd) + '\n')
              
# -- PRESENTATION (Input/Output) -- #
class IO:
    # TO-DOne add docstring - 
    """Handling Input / Output"""
    # TO-DOne add code to show menu to user - def print_menu
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    # TO-DOne add code to captures user's choice - def menu_choice
    #
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        try:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
            while choice not in ['l', 'a', 'i', 'd', 's', 'x']: 
                raise ValueError('That is not a valid choice!') 
        except ValueError as e:
            print(type(e))
            print('Please enter one of the offered options from menu') 
        else:   
            print("Thank you for entering a valid choise, please continue:")
            return choice

    # TO-DOne add code to display the current data on screen - def show_inventory
    @staticmethod
    def show_inventory(lst_Inventory):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst_Inventory:
            # Using the f-string notation/ by Mr Klos
            #print(f"{row.cd_id} - {row.cd_title} - {row.cd_artist}")
            print('{}\t{} (by:{})'.format(row.cd_id, row.cd_title, row.cd_artist))
    
        print('======================================')


    # TODO-ne add code to get CD data from user  
    @staticmethod
    def get_CDUserInput():
       """Function to accept User input

       Gets input from user for ID, Title and Artist to be save in table

       Args:
           None

       Returns:
           ID (string): ID representing the ID of the new CD
           Title (string): Title of the new CD
           Artist (string): Artist of the new CD
       """
       ValidID =False
       while not ValidID:
           try:
               ID = int(input('Enter ID: ').strip())
               if ID <=0:
                   raise ValueError('That is not a positive integer number!') 
           except ValueError:
               print('Please enter ID using positive integers')
           else:
               ValidID=True
       Title = input('What is the CD\'s title? ').strip()
       Artist = input('What is the Artist\'s name? ').strip()
       return ID, Title, Artist


class DataProcessor():
   """A set of functions to load, add and delete data from Magic Inventory"""
   @staticmethod 
   def add_new(lst_Inventory,cd_id, cd_artist, cd_title):
       """Function to add new data to list.
       
       Args:
            cd_id (int): ID representing the ID of the new CD
            cd_title (string): Title of the new CD
            cd_artist (string): Artist of the new CD
            lst_inventory(list of list): 2D data structure (list of dicts) that holds the data during runtime
      Returns:
            lst_inventory (list of list): 2D data structure (list of dicts) that holds the data during runtime
        """
       new_cd = CD(cd_id, cd_title, cd_artist)
       lst_Inventory.append(new_cd)
       return lst_Inventory

# -- Main Body of Script -- #
# TO-DOne Add Code to the main body
def main():   
    
    # -- DATA -- #
    strFileName = 'cdInventory.txt'
    lstOfCDObjects = []
    strChoice = '' # User input

# Load data from file into a list of CD objects on script start
# 1. When program starts, read in the currently saved Inventory
    lstOfCDObjects = FileIO.load_inventory(strFileName,lstOfCDObjects)   
# Display menu to user
    # show user current inventory
        # 2. start main loop
    while True:
        # 2.1 Display Menu to user and get choice
        IO.print_menu()
        strChoice = IO.menu_choice()
    
# let user add data to the inventory
        if strChoice == 'a':
            # 3.3.1 Ask user for new ID, CD Title and Artist
            strID, strTitle, strArtist = IO.get_CDUserInput()
            # 3.3.2 Add item to the table
            DataProcessor.add_new(lstOfCDObjects, strID, strTitle, strArtist)
            IO.show_inventory(lstOfCDObjects)
            continue # start loop back at top.

# let user save inventory to file

        elif strChoice == 's':
            # 3.6.1 Display current inventory and ask user for confirmation to save
            IO.show_inventory(lstOfCDObjects)
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
            # 3.6.2 Process choice
            if strYesNo == 'y':
                # 3.6.2.1 save data
                FileIO.save_inventory(strFileName, lstOfCDObjects)
            else:
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
            continue  # start loop back at top.

# let user load inventory from file
        elif strChoice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled. ')
            if strYesNo.lower() == 'yes':
                print('reloading...')
                lstOfCDObjects = FileIO.load_inventory(strFileName,lstOfCDObjects)
                IO.show_inventory(lstOfCDObjects)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstOfCDObjects)
            continue  # start loop back at top.
            
 # process display current inventory         
        elif strChoice == 'i':
            IO.show_inventory(lstOfCDObjects)
            continue  # start loop back at top.

# let user exit program
        elif strChoice == 'x':
            break
        else:
            print('General Error')

main()
("\n\nPress the enter key to exit.")        

