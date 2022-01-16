import requests
print("welcome to IsItDown.py")

again = True
while(again):
  urls = input("please write a URLs you want to check.\n")
  url_list = urls.split(",")
  for i in url_list:
    try:
      i = "http://" + i.strip(" ").strip("http://")
      url_resul = requests.get(i.strip(" "))
      print(i + " is up!")
    except:
      print(i + "is down!")
  end_question = input("Do you Want to start over? y/n")
  if(end_question == "y"):
    again = False
    print("k. bye")
  else:
    pass