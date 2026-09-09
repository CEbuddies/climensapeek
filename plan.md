## Mensa peeker
This app with whatever frontend can look into the University of Freiburg mensa plans for today and fetch what is on for that day.

### Action
First layer, we need some way to reliably fetch the data. That is, potential captchas etc. and what is if the website is JS actually not pure html.

### Frontend
The frontend can really be as simple as dumping formatted into the terminal so we do not need extensive frontend libs that clutter everything.

### Correctness
- Must determine the current weekday and fetch/display that day's plan specifically (not just "today's page" blindly).
- Must show lunch only, not dinner ("Abendessen"), which sometimes appears alongside it.
