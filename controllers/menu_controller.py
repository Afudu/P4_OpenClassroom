from views import main_view


class MakeMenu:
    """Show a given menu from the list of menus used in the application"""

    def __init__(self):

        self.main_menu = [('1', 'Player Menu'),
                          ('2', 'Tournament Menu'),
                          ('3', 'Quit')
                          ]

        self.player_menu = [('1', 'Add Player'),
                            ('2', 'Update Player Ranking'),
                            ('3', 'Player Report'),
                            ('4', 'Back to Main Menu')
                            ]

        self.tournament_menu = [('1', 'Create Tournament'),
                                ('2', 'Start Tournament'),
                                ('3', 'Resume Tournament'),
                                ('4', 'Tournament Report'),
                                ('5', 'Back to Main Menu')
                                ]

        self.time_control_menu = [('1', 'Bullet'),
                                  ('2', 'Blitz'),
                                  ('3', 'Rapid')
                                  ]

        self.players_report_menu = [('1', 'Players Alphabetically'),
                                    ('2', 'Players By Rating'),
                                    ('3', 'Back to Player Menu')
                                    ]

        self.tournaments_report_menu = [('1', 'Players'),
                                        ('2', 'Rounds'),
                                        ('3', 'Back to Tournament Menu')
                                        ]

        self.tournament_players_report_menu = [('1', 'Players Alphabetically'),
                                               ('2', 'Players By Rating'),
                                               ('3', 'Back to Tournament Report Menu')
                                               ]

        self.tournament_rounds_report_menu = [('1', 'All Rounds'),
                                              ('2', 'Matches by Round'),
                                              ('3', 'Back to Tournament Report Menu')
                                              ]

    def __call__(self, menu_to_show):
        """Display a menu and ask the user to choose"""
        self.table_view = main_view.TableView()
        self.menu_to_show = menu_to_show
        self.menu_headers = ['Option', 'Go To']
        self.table_view(self.menu_to_show, self.menu_headers)

        while True:
            entry = input('Choose an option:')
            for line in self.menu_to_show:
                if entry == line[0]:
                    return str(line[0])
            print('Please enter a valid menu item number \n')
