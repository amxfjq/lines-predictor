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
                'q3': stats['q3'], 'gq3': stats['gq3'], 'q4': stats['q4'], 'gq4': stats['gq4'], 'opp': stats['opp'], 
                'ground': stats['ground'], })

        return stats_list
    
    def resolving_wins_and_losses(self, x):
        #this checks through the data read directly from the files and compare the half time scores both first and second between both teams to determine the winner of each half

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
        
        #the end of file detector that is used to get out of the input infinite open loop
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

    def mapping_user_requests_to_stats_keyword(self, x):
        #x[0] contains request_store from the user input, x[1] contains the number of past matches the user requested for

        stats_input = {}
        for i in x[0]:
            if i == 1:
                stats_input['win/loss'] = 'w/l'
            elif i == 2:
                stats_input['team full time points'] = 'ft'
            elif i == 3:
                stats_input['game full time points'] = 'gft'
            elif i == 4:
                stats_input['1st half win/loss'] = '1st ht'
            elif i == 5:
                stats_input['team 1st half points'] = '1ht'
            elif i == 6:
                stats_input['game 1st half points'] = 'g1ht'
            elif i == 7:
                stats_input['team 2nd half win/loss'] = '2nd ht'
            elif i == 8:
                stats_input['team 2nd half points'] = '2ht'
            elif i == 9:
                stats_input['game 2nd half points'] = 'g2ht'
            elif i == 10:
                stats_input['game 1st quarter points'] = 'gq1'
            elif i == 11:
                stats_input['game 2nd quarter points'] = 'gq2'
            elif i == 12:
                stats_input['game 3rd quarter points'] = 'gq3'
            elif i == 13:
                stats_input['game 4th quarter points'] = 'gq4'


        return stats_input, x[1]
    
    def mapping_user_requests_to_available_data(self, x, y):
        #x is the user input mapped to the key that holds the teams total data in y i.e y is the teams data
        
        output01 =[]

        #this is to arrange the output of the games from the latest/newest game played to the oldest one
        sorter = []
        placeholder =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for a in placeholder[10 - x[1]:]:
            sorter.append(a)
        sorter.sort(reverse=True)

        for j in sorter:
            output = {}
            for i in x[0]:
                output['vs'] = y[j]['opp']

                if i == 'win/loss':
                    output['win/loss'] = y[j]['w/l']

                elif i == 'team full time points':
                    output['team full time points'] = y[j]['ft']

                elif i == 'game full time points':
                    output['game full time points'] = y[j]['gft']

                elif i == '1st half win/loss':
                    output['1st half win/loss'] = y[j]['1st ht']

                elif i == 'team 1st half points':
                    output['team 1st half points'] = y[j]['1ht']

                elif i == 'game 1st half points':
                    output['game 1st half points'] = y[j]['g1ht']

                elif i == 'team 2nd half win/loss':
                    output['team 2nd half win/loss'] = y[j]['2nd ht']

                elif i == 'team 2nd half points':
                    output['team 2nd half points'] = y[j]['2ht']

                elif i == 'game 2nd half points':
                    output['game 2nd half points'] = y[j]['g2ht']

                elif i == 'game 1st quarter points':
                    output['game 1st quarter points'] = y[j]['gq1']

                elif i == 'game 2nd quarter points':
                    output['game 2nd quarter points'] = y[j]['gq2']

                elif i == 'game 3rd quarter points':
                    output['game 3rd quarter points'] = y[j]['gq3']

                elif i == 'game 4th quarter points':
                    output['game 4th quarter points'] = y[j]['gq4']

            output01.append(output)
        
        return output01


def main():
    league = input('league: ').lower().strip()
    team = input('team: ').lower().strip()
    rqt = retrieve(league, team)
    pr_user_request = rqt.mapping_user_requests_to_stats_keyword(rqt.user_request())
    full_stats = rqt.resolving_wins_and_losses(rqt.raw_results())
    final_result = rqt.mapping_user_requests_to_available_data(x=pr_user_request, y=full_stats)
    print(final_result)


if __name__ == '__main__':
    main()