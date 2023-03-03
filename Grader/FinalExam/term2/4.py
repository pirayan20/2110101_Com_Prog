
uefa = [(2020,('Chelsea','ENG'),('Man City','ENG')),
(2019,('Bayern','GER'),('Paris','FRA')),
(2018,('Liverpool','ENG'),('Tottenham','ENG')),
(2017,('Real Madrid','ESP'),('Liverpool','ENG')),
(2016,('Real Madrid','ESP'),('Juventus','ITA')),
(2015,('Real Madrid','ESP'),('Atletico','ESP')),
(2014,('Barcelona','ESP'),('Juventus','ITA')),
(2013,('Real Madrid','ESP'),('Atletico','ESP')),
(2012,('Bayern','GER'),('Dortmund','GER')),
(2011,('Chelsea','ENG'),('Bayern','GER')),
(2010,('Barcelona','ESP'),('Man United','ENG')),
(2009,('Inter','ITA'),('Bayern','GER')),
(2008,('Barcelona','ESP'),('Man United','ENG')),
(2007,('Man United','ENG'),('Chelsea','ENG')),
(2006,('Milan','ITA'),('Liverpool','ENG')),
(2005,('Barcelona','ESP'),('Arsenal','ENG')),
(2004,('Liverpool','ENG'),('Milan','ITA')),
(2003,('Porto','POR'),('Monaco','FRA')),
(2002,('Milan','ITA'),('Juventus','ITA')),
(2001,('Real Madrid','ESP'),('Leverkusen','GER')),
(2000,('Bayern','GER'),('Valencia','ESP'))]

def get_champion_sets(uefa) :
    winner,loser = set(),set() 
    for s in uefa:
        winner.add(s[1][0])
        loser.add(s[2][0])
    return (winner,loser)

def win_and_lose(winners, runner_ups):
    return winners.intersection(runner_ups)

def is_runner_up(winners, runner_ups, team):
    return team in runner_ups

def get_finalists(uefa) :
    d = {}
    for x in uefa:
        if x[1][1] not in d:
            d[x[1][1]] = set()
        d[x[1][1]].add((x[0],x[1][0]))
        if x[2][1] not in d:
            d[x[2][1]] = set()
        d[x[2][1]].add((x[0],x[2][0]))
    return d

def same_country(finalists):
    ans = []
    for country in finalists:
        s = set()
        for tupe in finalists[country]:
            if tupe[0] not in s:
                s.add(tupe[0])
            else:
                ans.append(tupe[0])
    return sorted(ans)


# print(win_and_lose(get_champion_sets(uefa)[0],get_champion_sets(uefa)[1]))
print(same_country(get_finalists(uefa)))