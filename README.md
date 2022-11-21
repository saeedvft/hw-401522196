# main.py

a python code to check the algorithm of an iranian card number and generating new random card number.

## Usage

```python
from main import Card
# Keep an eye on directory settings for  importing the code:)

sample = Card(6037991479850970)
print(sample.valid, sample.bank)
print(sample.generator(this_bank=636214))

# there's an algorithm or a pattern for finding the name of banks using first 6 digit.
# we track that pattern using BS4 and Web Scraping.
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)