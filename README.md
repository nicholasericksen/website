# nicholasericksen.com
Hello and welcome to my personal website! Well the repo at least.
You can find the acutal website [here](https://nicholasericksen.com).

The goal of this website is similar to my goals in life; "simplicty, simplicity, simplicity."
(Yes I took that quote from Thoreau)

And here is another one just for good measure...


```
...for a man is rich in proportion to the number of things which he can afford to let alone?
```

Well enough philosophizing for now.

## Design Goals
* No javascript
* Mobile and web friendly out of the box
* Respect light and dark mode (TODO)
* No frameworks
* Leverage HTML and native browser features
* Use markdown to write new blog posts
* Free to host 
* HTTPS (of course)


## Functionality
Add new markdown articles into the `articles` directory.
The title of the aritcle should be the directory name with a `-` will be replaced with spaces.
Inside the directory the acutally blog post is called `README.md`.

To build the article first run `python3 -m venv venv` in the root directory.
Then enable it with `source venv/bin/activate`.
In order to build and publish an article run `python3 build.py`.
You will be prompted to select which article to publish.
