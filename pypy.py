from email import policy
import requests
import sys
import json

name = sys.argv[1]
surname = sys.argv[2]
domains = ["gmail.com"]

for domain in sys.argv[3:]:
    domains.append(domain)

def routine(permut,nom,prenom,domain):
    permut.append(nom+prenom+"@"+domain)
    permut.append(nom+'.'+prenom+"@"+domain)
    permut.append(nom+'-'+prenom+"@"+domain)
    permut.append(nom+'_'+prenom+"@"+domain)
    permut.append(nom[0]+prenom+"@"+domain)
    permut.append(nom[0]+'.'+prenom+"@"+domain)
    permut.append(nom[0]+'-'+prenom+"@"+domain)
    permut.append(nom[0]+'_'+prenom+"@"+domain)
    permut.append(nom+prenom[0]+"@"+domain)
    permut.append(nom+'.'+prenom[0]+"@"+domain)
    permut.append(nom+'-'+prenom[0]+"@"+domain)
    permut.append(nom+'_'+prenom[0]+"@"+domain)
    permut.append(nom[0]+prenom[0]+"@"+domain)
    permut.append(nom[0]+'.'+prenom[0]+"@"+domain)
    permut.append(nom[0]+'-'+prenom[0]+"@"+domain)
    permut.append(nom[0]+'_'+prenom[0]+"@"+domain)

def condition(res):
    return(res["valid_syntax"] and not res["disposable"] and res["deliverable"] and res["webmail"])

permut = []

for i in domains:
    permut.append(name+"@"+i)
    permut.append(surname+"@"+i)
    routine(permut,name,surname,i)
    routine(permut,surname,name,i)

def testMail(email):
    r = requests.get("https://api.eva.pingutil.com/email?email="+email)
    res = json.loads(r.text)['data']
    print(res)
    if condition(res):
        print('Found ', email ,'!!!!')

#for i in permut:
#    testMail(i)

testMail("oiuzpvpvp@gmail.com")

#r= s.get("https://email-checker.net/")
#csrft = r.text[12217+13:12217+13+43]#recuperation du token csrf dans la page
#cookie = ".AspNetCore.Antiforgery.38G8fUVOpE4=CfDJ8DWBGBoRs2VHiaYRt_Pxc0c07LPjwkiRbvLHWO8Fci7jjMcU7eYeA9R85bFoLwpN6vC-dx1LVXREbonLgWXz0jwmmJE5cpeuB0uVccqFsRooQ_imJ6o3Dc0HRWZ7yyyQiZ2lC8zit-h4LKSJcUnwh3w; .EmailHippo.Session=CfDJ8DWBGBoRs2VHiaYRt%2FPxc0fFQXyfadNwqkNC6%2F4rnYU8VI8HRdxBEaOld3GGk7uuq7wVQV%2BgMd6nJPHov3UahAkrnMDq%2BLagEZp4r3e0FcGmZJvu3imSwNq0%2FlvKtw9B3A4cANzrmAcO78%2F4IAiCjcYeFH7MufL08P2kFfgYv2tN; _gcl_au=1.1.2062692024.1665495961; _ga=GA1.1.1904131943.1665495961; messagesUtk=45375b62dd6c480a9b40e6cf062ca939; _ga_NS6FVYCC8M=GS1.1.1665495961.1.1.1665496562.0.0.0; __atuvc=5%7C41"
#email = "qlacoux@gmaiol.com"
#r= s.get("https://api.eva.pingutil.com/email?email="+email)
#res = json.loads(r.text)['data']



