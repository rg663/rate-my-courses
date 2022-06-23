#Check UBitName
import requests
def finder(personname):
  text=requests.get("https://www.buffalo.edu/search/search.html?searchUrl=https://www.buffalo.edu/search/search.html&query="+personname+"%40buffalo.edu&collection=meta-search&f.Tabs%7Cdb-people=People")
  with open("data.txt","w") as f:
    f.write(text.text)
  with open("data.txt","r") as f:
    for m in f.readlines():
      if('              <a href="mailto:'+personname+'@buffalo.edu">'+personname+'@buffalo.edu</a>'in m):
        
        return True
    else:
      return False

      