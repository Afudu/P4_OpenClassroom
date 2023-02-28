from views.main_view import TableView


class MakeMenu:
    """Displays a given menu from the list of menus used in the application
    and asks the user to choose and option"""

    def __call__(self, menu_to_show):

        self.table_view = TableView()
        self.menu_to_show = menu_to_show
        self.menu_headers = ['Option', 'Go To']
        self.table_view(self.menu_to_show, self.menu_headers)

        while True:
            entry = input('Choose an option:')
            for line in self.menu_to_show:
                if entry == line[0]:
                    return str(line[0])
            print('Please enter a valid menu item number \n')
