
## Commerce - CS50W Project 2 

Note: This project was completed as an assignment for CS50W Lecture 2.

### General Info

An eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist". The highest bidder wins the listed item. 



## Technologies

- python 3.12.3
- django 5.0.6
- HTML 5
- CSS 3
- Sqlite
## Features

- List any item and sell it online
- Buy any listed item by bidding highest
- Filter listing by categories, add item to watchlist and more
## Run locally

Clone the project

```bash
  git clone https://github.com/Aerish369/CS50W-Project2-Commerce
```

Go to the project directory

```bash
  cd CS50W-Project2-Commerce
```

Install dependencies

```bash
  pip install -r requirements.txt

```

Mirgrate the database

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```


## Screenshots

### Active Listing Page

![image](https://github.com/Aerish369/CS50W-Project2-Commerce/assets/107682299/f9cf12c9-1575-4440-89a7-92d4af426314)

### Individual Listing Page 

![image](https://github.com/Aerish369/CS50W-Project2-Commerce/assets/107682299/4ef29c48-d637-4396-ae24-e460b66152c5)

### Categories Page

![image](https://github.com/Aerish369/CS50W-Project2-Commerce/assets/107682299/50077515-ff1e-4bf1-8032-586c6d592ff9)


### Listing won by higgest bidder

![image](https://github.com/Aerish369/CS50W-Project2-Commerce/assets/107682299/c3d98cb3-f989-42be-9af2-81ea96aaa619)

