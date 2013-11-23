from math import sqrt


def sim_distance(prefs,person1,person2):
    si={}
    for item in prefs[person1]:
    	if item in prefs[person2]:
       	   si[item]=1

    n=len(si)
    if len(si)==0: return 0

    sumSq1 = sum([pow(prefs[person1][item],2) for item in si])
    sumSq2 = sum([pow(prefs[person2][item],2) for item in si])

    sum1 = sum([prefs[person1][item] for item in si])
    sum2 = sum([prefs[person2][item] for item in si])

    pSum = sum([prefs[person1][item]*prefs[person2][item] for item in si])

    num = pSum-(sum1*sum2/n)
    den = sqrt((sumSq1-pow(sum1,2)/n)*(sumSq2-pow(sum2,2)/n))

    if den == 0: return 0
    
    r= num/den

    return r;
    

if __name__ =="__main__":

   critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0}, 'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 3.5}, 'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0}, 'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5}, 'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.0}, 'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5}, 'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}
   
   distance = sim_distance(critics,'Lisa Rose','Jack Matthews')
   print(distance)
