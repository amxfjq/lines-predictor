import csv
import re
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

class Deposit:
    def __init__(self, league, team):
        self.league = league
        self.team = team
    
    @staticmethod
    def user_input():
        stats = [
                    'win/loss',
                    'team full time points',
                    'game full time points',
                    'team 1st half points',
                    'game 1st half points',
                    'team 2nd half points',
                    'game 2nd half points',
                    'team 1st quarter points', 
                    'game 1st quarter points',
                    'team 2nd quarter points', 
                    'game 2nd quarter points',
                    'team 3rd quarter points', 
                    'game 3rd quarter points',
                    'team 4th quarter points', 
                    'game 4th quarter points',
                    'opponent', 
                    'home/away'
                ]

        input_store = {}

        for i in stats:
            if i == 'win/loss':
                while True:
                    x = input(f'{i}: ').lower().strip()
                    if matches := re.search(r'(w)(?:in)?|(?:(l)(?:oss)?)', x):
                        if matches.group(1):
                            input_store[i] = matches.group(1)
                            break
                        else:
                            input_store[i] = matches.group(2)
                            break
                    else:
                        print('win/loss takes win, loss, w or l as input')

            elif i == 'home/away':
                while True:
                    x = input(f'{i}: ').lower().strip()
                    if matches := re.search(r'(h)(?:ome)?|(?:(a)(?:way)?)', x):
                        if matches.group(1):
                            input_store[i] = matches.group(1)
                            break
                        else:
                            input_store[i] = matches.group(2)
                            break

            elif i == 'opponent':
                #if i not in ...:
                input_store[i] = input(f'{i}: ').lower().strip()

            else:
                while True:
                    try:
                        input_store[i] = int(input(f'{i}: '))
                    except ValueError:
                        print('input must be a number')
                    else:
                        break
        return input_store

    def create(self,x):
        file_path = Path(f'{self.league}/{self.team}.csv')
        with open(file_path,'w') as teamsheet:
            y = csv.writer(teamsheet)
            y.writerow(['w/l','ft','gft','1ht','g1ht','2ht','g2ht','q1','gq1',
            'q2','gq2','q3','gq3','q4','gq4','opp','ground'])
        
        with open(file_path, 'a') as teamsheet:
            y = csv.DictWriter(teamsheet, fieldnames=['w/l','ft','gft','1ht','g1ht','2ht','g2ht','q1','gq1','q2','gq2','q3','gq3','q4','gq4','opp','ground'])
            y.writerow(
                {
                    'w/l':x['win/loss'], 
                    'ft':x['team full time points'], 
                    'gft':x['game full time points'], 
                    '1ht':x['team 1st half points'], 
                    'g1ht':x['game 1st half points'], 
                    '2ht':x['team 2nd half points'], 
                    'g2ht':x['game 2nd half points'], 
                    'q1':x['team 1st quarter points'], 
                    'gq1':x['game 1st quarter points'], 
                    'q2':x['team 2nd quarter points'], 
                    'gq2':x['game 2nd quarter points'], 
                    'q3':x['team 3rd quarter points'], 
                    'gq3':x['game 3rd quarter points'], 
                    'q4':x['team 4th quarter points'], 
                    'gq4':x['game 4th quarter points'], 
                    'opp':x['opponent'], 
                    'ground':x['home/away']
                    }
                    )



def main():
    quest = input('input or retrieve? ').lower().strip()
    league = input('league: ').lower().strip()
    team = input('team: ').lower().strip()
    
    if quest == 'input':
        deposit = Deposit(league, team)
        user_input = deposit.user_input()
        deposit.create(user_input)

    elif quest == 'retrieve':
        rqt = Retrieve(league, team)
        full_stats = rqt.resolving_wins_and_losses(rqt.raw_results())
        user_request = rqt.user_request()
        final_result = rqt.mapping_user_requests_to_available_data(
            x=user_request, y=full_stats
        )
        print(final_result)


if __name__ == '__main__':
    main()
