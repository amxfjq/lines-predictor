import csv
from pathlib import Path


class Retrieve:
    def __init__(self, league, team):
        self.league = league
        self.team = team

    def raw_results(self):
        stats_list = []
        file_path = Path(f'{self.league}/{self.team}.csv')
        with open(file_path, 'r') as team_file:
            team_file01 = csv.DictReader(team_file)
            for stats in team_file01:
                stats_list.append(
                    {
                        'win/loss': stats['w/l'],
                        'team full time points': stats['ft'],
                        'game full time points': stats['gft'],
                        'team 1st half points': stats['1ht'],
                        'game 1st half points': stats['g1ht'],
                        'team 2nd half points': stats['2ht'],
                        'game 2nd half points': stats['g2ht'],
                        'q1': stats['q1'],
                        'game 1st quarter points': stats['gq1'],
                        'q2': stats['q2'],
                        'game 2nd quarter points': stats['gq2'],
                        'q3': stats['q3'],
                        'game 3rd quarter points': stats['gq3'],
                        'q4': stats['q4'],
                        'game 4th quarter points': stats['gq4'],
                        'opp': stats['opp'],
                        'ground': stats['ground'],
                    }
                )

        return stats_list

    @staticmethod
    def resolving_wins_and_losses(x):
        # this checks through the data read directly from the files and compare the half time scores both first and second between both teams to determine the winner of each half

        for i in x:
            if (2 * int(i['team 1st half points'])) > int(i['game 1st half points']):
                i['team 1st half win/loss'] = 'w'

            elif (2 * int(i['team 1st half points'])) == int(i['game 1st half points']):
                i['team 1st half win/loss'] = 'd'

            else:
                i['team 1st half win/loss'] = 'l'

            if (2 * int(i['team 2nd half points'])) > int(i['game 2nd half points']):
                i['team 2nd half win/loss'] = 'w'

            elif (2 * int(i['team 2nd half points'])) == int(i['game 2nd half points']):
                i['team 2nd half win/loss'] = 'd'

            else:
                i['team 2nd half win/loss'] = 'l'

        return x

    @staticmethod
    def user_request():

        print(
            '''Input the number in front of the stats you will like to see: 
            - Win/Loss (1)
            - Team Full Time Points (2)
            - Game Full Time Points (3)
            - Team 1st Half Win/Loss (4)
            - Team 1st Half Points (5)
            - Game 1st Half Points (6)
            - Team 2nd Half Win/Loss (7)
            - Team 2nd Half Points (8)
            - Game 2nd Half Points (9)
            - Game 1st Quarter Points (10)
            - Game 2nd Quarter Points (11)
            - Game 3rd Quarter Points (12)
            - Game 4th Quarter Points (13) '''
        )

        available_stats = [
            'win/loss',
            'team full time points',
            'game full time points',
            'team 1st half win/loss',
            'team 1st half points',
            'game 1st half points',
            'team 2nd half win/loss',
            'team 2nd half points',
            'game 2nd half points',
            'game 1st quarter points',
            'game 2nd quarter points',
            'game 3rd quarter points',
            'game 4th quarter points',
        ]

        holder = {}

        while True:
            try:
                x = int(input('- '))

            # the end of file detector that is used to get out of the input infinite open loop
            except EOFError:
                break

            else:
                if 0 < x < 14:
                    holder[x] = available_stats[x - 1]

                else:
                    print('number does not represent an available stat')

        # this removes duplicate entries
        request_store = set()
        for i in holder:
            request_store.add(holder[i])

        while True:
            y = int(input('over the last? '))

            if y != 0 and y < 11:
                break

            elif y == 0:
                print('no of games must be greater than 0')

            else:
                print('max is 10 games')

        return request_store, y

    @staticmethod
    def mapping_user_requests_to_available_data(x, y):
        # x is a tupple of the user input which includes stats and number of games to iterate over, while y is total data of the team

        output01 = []

        # this is to arrange the output of the games from the latest/newest game played to the oldest one
        sorter = []
        placeholder = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for a in placeholder[10 - x[1] :]:
            sorter.append(a)
        sorter.sort(reverse=True)

        for j in sorter:
            output = {'vs': y[j]['opp']}
            for i in x[0]:
                output[i] = y[j][i]

            output01.append(output)

        return output01


def main():
    league = input('league: ').lower().strip()
    team = input('team: ').lower().strip()
    rqt = Retrieve(league, team)
    full_stats = rqt.resolving_wins_and_losses(rqt.raw_results())
    user_request = rqt.user_request()
    final_result = rqt.mapping_user_requests_to_available_data(
        x=user_request, y=full_stats
    )
    print(final_result)


if __name__ == '__main__':
    main()
