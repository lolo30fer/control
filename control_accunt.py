import instaloader
ppr=["drock_bc","sias_bc","loverk_bc","godofcar_bc","toki_bc"]
loader = instaloader.Instaloader()
loader.login('l8sif5', 'L510WKJ2S621')
g=0

for i in ppr:
    profile = instaloader.Profile.from_username(loader.context,ppr[g])
    print(ppr[g])
    print("my=> ", profile.followees )
    print("your=> ",profile.followers)
    print("=========================")
    g+=1

