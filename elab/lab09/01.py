import json


def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data


# specifying the zip file name
filename = "IMDB_movies_merged.json"

data = read_json(filename)
data = sorted(data, key=lambda x: float(x['ratingValue']) if x['ratingValue'] else 0, reverse=True )

def q1():
    ans = []
    seen = []
    for row in data:
        if 'director' in row.keys() and 'cast' in row.keys() and row['ratingValue']:
            if ( 'Steven Spielberg' not in row['director']['name']):
                actors = list(map(lambda x: x['name'], row['cast']))
                if ("Harrison Ford" in actors ):
                    if (len(seen) > 5):
                        ans.pop()
                        break
                    else:
                        rating = float(row['ratingValue'])
                        if ( rating not in seen ):
                            seen.append(rating)
                            ans.append( row['director']['name'])
                        else :
                            ans.append( row['director']['name'])
    print("\n".join(sorted(ans)))

def q2():
    for row in data:
        if ( 'director' in row.keys() and 'cast' in row.keys( ) ):
            if ( row['director']['name'] != 'Steven Spielberg' and row['director']['name'] != 'George Lucas' ):
                actors = list(map(lambda x: x['name'], row['cast']))
                if ("Harrison Ford" in actors and "Tommy Lee Jones" in actors):
                    print(row['name'])
                    break

print('(1) Answer of Q1')
print('(2) Answer of Q2')
ans = input('or just press (Enter): ')
if ans == '1':
  q1()
elif ans == '2':
  q2()
else:
    print('Nothing to do..')