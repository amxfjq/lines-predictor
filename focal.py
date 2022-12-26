import csv
from pathlib import Path

class retrieve:
    def __init__(self, league, team):
        self.league = league
        self.team = team

    def raw_results(self):
        stats_list = []
        file_path = Path(f'{self.league}/{self.team}.csv')
        with open(file_path, 'r') as team_file:
            team_file01 = csv.DictReader(team_file)
            for stats in team_file01:
                stats_list.append({'w/l': stats['w/l'], 'ft': stats['ft'], 'gft': stats['gft'], 
                '1ht': stats['1ht'], 'g1ht': stats['g1ht'], '2ht': stats['2ht'], 'g2ht': stats['g2ht'], 
                'q1': stats['q1'], 'gq1': stats['gq1'], 'q2': stats['q2'], 'gq2': stats['gq2'], 
                'q3': stats['q3'], 'gq3': stats['gq3'], 'q4': stats['gq4'], 'opp': stats['opp'], 
                'ground': stats['ground'], })

        return stats_list
    
    def resolving_wins_and_losses(self, x):

        for i in x:
            if (2 * int(i['1ht'])) > int(i['g1ht']):
                i['1st ht'] = 'w'

            elif (2 * int(i['1ht'])) == int(i['g1ht']):
                i['1st ht'] = 'd'

            else:
                i['1st ht'] = 'l'

            if (2 * int(i['2ht'])) > int(i['g2ht']):
                i['2nd ht'] = 'w'

            elif (2 * int(i['2ht'])) == int(i['g2ht']):
                i['2nd ht'] = 'd'

            else:
                i['2nd ht'] = 'l'

        return x

    def user_request(self):

        print('''Input the number in front of the stats you will like to see: 
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
            - Game 4th Quarter Points (13) ''')

        request_store = []

        while True:
            try:
                x = int(input('- '))

            except EOFError:
                break

            else:
                if x !=0 and x < 14:
                    request_store.append(x)

                else:
                    print ('number does not represent an available stat')

        #this removes duplicate entries
        for i in request_store:
            if request_store.count(i) > 1:
                request_store.remove(i)

        while True:
            y = int(input('over the last? '))

            if y != 0 and y < 11:
                break

            elif y == 0:
                print('no of games must be greater than 0')

            else:
                print('max is 10 games')

        return request_store, y

    def mapping_stats_input_to_results(x, y):
        stats_input = {}
        for i in x:
            if i == 1:
                stats_input['win/loss'] = y
            elif i == 2:
                stats_input['team full time points'] = 'ft'
            elif i == 3:
                stats_input['game full time points'] = 'gft'
            elif i == 4:
                stats_input['1st half win/loss'] = ''

    def full():
        pass
    def half():
        pass
    def qtr():
        pass

def main():
    league = input('league: ')
    team = input('team: ')
    rqt = retrieve(league, team)
    y = rqt.resolving_wins_and_losses(rqt.raw_results())
    #user_request_return = user_request()
    #print (user_request_return)
    #stat_getter_return = stat_getter()
    #interpreter(stat_getter_return)
    #print(stat_getter(user_request_return))

def stat_getter(user_request_return):
    league, team, stats, past_games = user_request_return
    print(league)
    print(team)
    print(stats)
    print(past_games)

#    stats_list =[]
#    league = input('league: ')
#    team = input('team: ')
#    file_path = Path(f'{league}/{team}.csv')

#    with open(file_path,'r') as team_file:
#        team_file01 = csv.DictReader(team_file)
#        for stats in team_file01:
#            stats_list.append({'w/l': stats['w/l'], 'ft': stats['ft'], 
#            'gft': stats['gft']})
#
#    return stats_list
    pass
def interpreter(stat_getter_return):
    for i in stat_getter_return:
        print (i)


if __name__ == '__main__':
    main()