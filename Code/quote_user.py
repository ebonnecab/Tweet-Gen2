import python_quote

#this function tests whether i am able to import the random_python_quote module
def import_quote():
    quotes = python_quote.random_python_quote()
    return quotes


if __name__ == '__main__':
    quote = import_quote()
    print(quote)