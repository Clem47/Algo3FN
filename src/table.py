class Table :

    def __init__(self, name : str ,key: set, value: set, fk: set) -> None:
        """
        This function init the table.

        Arguments :
            self : The table.
            name (str) : The name of the table.
            key (set) : A set of key.
            value (set) : A set of value.
            fk (set) : A set of foreign key. 

        Returns :
            None.
        """
        self.name = str.upper(name)
        self.key = ""
        self.value = ""
        self.fk = ""
        i = 0
        for atrr in key :
            self.key = self.key + atrr 
            if i < len(key)-1 :
                 self.key = self.key + " "
            i =i +1
        i = 0
        for atrr in value :
            self.value = self.value + atrr 
            if i < len(value)-1 :
                self.value = self.value + ", "
            i =i +1
        for atrr in fk :
            self.fk = self.fk + atrr
    
    def get_key(self) -> set:
        """
        This function get the set of key of the table.

        Arguments :
            self : The table.

        Returns :
            set : the set of key of the table.
        """
        return self.key

    def get_value(self) -> set:
        """
        This function get the set of value of the table.

        Arguments :
            self : The table.

        Returns :
            set : the set of value of the table.
        """
        return self.value
    
    def get_fk(self) -> set:
        """
        This function get the set of foreign key of the table.

        Arguments :
            self : The table.

        Returns :
            set : the set of foreign key of the table.
        """
        return self.fk
    
    def get_name(self) -> str :
        """
        This function get the name of the table.

        Arguments :
            self : The table.

        Returns :
            set : the name of the table.
        """
        return self.name
