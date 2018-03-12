import.praw

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
print ('Gaming News')

print ('Xbox')

GET [/r/XboxOne]/new
    clamp(n, 1, 5)

print ('Playstation')

GET [/r/PS4]/new
    clamp(n, 1, 5)

print ('Nintendo')

GET [/r/nintendo]/new
    clamp(n, 1, 5)
    
print ('Uncategorized Gaming News')

GET [/r/gamingnews]/new
    clamp(n, 1, 5)

