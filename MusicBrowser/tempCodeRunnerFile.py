def requery(self):
        print(self.sql_select + self.sql_sort)  # TODO: Delete this line
        self.cursor.execute(self.sql_select + self.sql_sort)

        # clear the listbox contents before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])