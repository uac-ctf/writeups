
# NahamCon2021 Personnel Writeup

500 points - Mission - 23 Solves - easy

```
This is Stage 3 of Path 1 in The Mission. After solving this challenge, you may need to refresh the page to see the newly unlocked challenges.

The Constellations use this service to lookup personnel. Can you hack it?

```


## Solve

This took us some time, although the solution was simple and the challenge was easy. However, it only had 23 solves...

The challenge presented a page with a form to lookup personnel. It stated that there was no database, which excludes some paths.

![personnel](https://github.com/uac-ctf/nahamcon2021/raw/main/personnel/personnel.png)

When a query term was entered, it provided all entries matching that term. It worked for single characters and regular expressions.
The form also contained a field named ```setting``` which as always sent with the value ```0```.
Both the input field and the form provided a way of obtaining the flag.

![personnel](https://github.com/uac-ctf/nahamcon2021/raw/main/personnel/personnel-query.png)

According to our speculation, the backend was implemented in python and had an object with all entries, with the flag separated by a new line ```\n```. 
Regular expressions usually do not work for multiline matches, and the flag is "protected" from retrieval.

We solved it by changing the value of the ```setting``` field to ```16```. Actually, many values were supported as long as the last 3 bits are ```100```.
If the backend uses Python, this sets the ```re.DOTALL``` flag of something like a ```re.findall```, enabling the regular expression to search acroos the ```\n```.

![personnel](https://github.com/uac-ctf/nahamcon2021/raw/main/personnel/personnel-solved.png)

Another solution, probably much simpler was to issue ```[\s\S]+``` as the query term. This searches for one or more characters that are spaces, or that are not spaces.
It is similar to the ```.+``` query, but also includes the ```\n```.

We include a Proof of Concept of to test the queries.
