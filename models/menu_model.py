
class MenuList:
    """the list of menus used in the application"""

    def __init__(self):

        self.main_menu = [('1', 'Player Menu'),
                          ('2', 'Tournament Menu'),
                          ('3', 'Quit')
                          ]

        self.player_menu = [('1', 'Add Player'),
                            ('2', 'Update Player Rating'),
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
                                               ('3', 'Back to Report Menu')
                                               ]

        self.tournament_rounds_report_menu = [('1', 'All Rounds'),
                                              ('2', 'Matches by Round'),
                                              ('3', 'Back to Report Menu')
                                              ]
