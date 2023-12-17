import os
import sys
import markdown
from os import walk

from bs4 import BeautifulSoup


def publish(article):
  with open("template-article.html", "r") as f:
    template = f.read()
  
  #TODO replace with markdown.readFromFile or whatever...
  # this would allow for removing next two file open blocks
  with open(f"articles/{article}/README.md", "r") as f:
    md = f.read()
    html = markdown.markdown(md, extensions=['fenced_code'])
  
  template = template.replace("__article__", html)
  
  soup = BeautifulSoup(template, features="html.parser")
  print(f"Publishing: {article}")  
  with open(f"public/{article}.html", "w") as f:
    f.write(soup.prettify())
  os.system("git status")
  prompt = """
  WARNING: Any currently staged changes will also be pushed!
  Would you like to proceed to adding index.html to commit
  and pushing the commit to the master branch?
  """
  print(prompt)
  git_push = input("Answer [Y/n]: ")
  if git_push == "Y":
    os.system("git add public articles")
    os.system(f"git commit -m 'Publish {article} to public'")
    os.system("git push origin main")
  else:
    print("ABORTING Publication!")

def prompt_publish():
  articles = next(os.walk("./articles"))[1]

  print("===============================")
  print("Articles Available to Publish:")
  print("===============================\n")
  for index, article in enumerate(articles):
    print(f"[{index}] {article}")
  print("\n")
  selection = input("Specify article number to publish: ")
  article_to_publish = articles[int(selection)]
  print(f"Publishing...{article_to_publish}...")
  publish(article_to_publish)
  print("Done!")

def generate_index():

  f_names = []
  for (dirpath, dirnames, filenames) in walk("public"):
    f_names.extend(filenames)
    break

  with open("template.html", "r") as f:
    template = f.read()
  
  #TODO replace with markdown.readFromFile or whatever...
  # this would allow for removing next two file open blocks
  html = "<ol>"

  for name in f_names:
    html += f"<li><a href='/public/{name}'>{name.replace('-',' ').replace('.html', '')}</a></li>"

  html += "</ol>"
  
  template = template.replace("__article__", html)
  
  soup = BeautifulSoup(template, features="html.parser")
  #print(f"Publishing: {article}")  
  with open(f"blog.html", "w") as f:
    f.write(soup.prettify())
  


if __name__ == "__main__":
   try:
     # check if specific article is passed
     publish(sys.argv[1])
   except:
     # else list all available articles
     #publish("Case-Study_Heartbleed")
     prompt_publish()

  #if "--generate-index" in sys.argv[1]:
   print("Generating Index - blog.html")
   generate_index()
