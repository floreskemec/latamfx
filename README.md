# LatAmFX 💸 by Gonzalo Flores Kemec

LatAmFX is a RESTful API built with Python's FastAPI framework that provides currency exchange rates, interest rates, and earnings for Latin American currencies, as well as the euro and US dollar. The API connects to real-world financial APIs to retrieve the latest currency and interest rate data.

In addition to the API, LatAmFX includes a simple web front-end that allows users to easily perform currency conversions, view interest rates, and calculate earnings based on investment amounts.
Features

### LatAmFX provides the following features:

__/currencies__ endpoint: returns a list of Latin American currencies, as well as the euro and US dollar.

__/best_investments__ endpoint: This endpoint returns the best possible combination of currencies bought in USD dollars for a day. To calculate this, we can use a variation of the [knapsack problem called the currency arbitrage problem](https://walkccc.me/CLRS/Chap24/Problems/24-3/). The goal is to find the combination of currencies that maximizes the return on investment.

This function uses the [__itertools__](https://docs.python.org/3/library/itertools.html) module to generate all possible combinations of 3 currencies from the API data. It then calculates the return on investment for each combination and updates the best_investment dictionary if the current combination has a higher return than the previous best combination. Finally, it returns the best_investment dictionary with the combination and return on investment for the best possible investment.

__Web front-end__: allows users to perform currency conversions, view interest rates, and calculate earnings.

### Technical Details

In LatAmFX, we use the requests library to make HTTP requests to external APIs and retrieve JSON response objects. We also use the fastapi framework to define request and response objects for our own API endpoints. For example, the GET /currencies endpoint might return a response object like this:

### Data contract

`.json`
```Python
{
    "currencies": [
        "ARS",
        "BRL",
        "CLP",
        "COP",
        "CRC",
        "EUR",
        "MXN",
        "PEN",
        "USD",
        "UYU"
    ]
}
```

### RESTful Architecture
LatAmFX follows REST archtectural principles.

REST (Representational State Transfer) is an architectural style for designing networked applications. RESTful APIs are designed around a set of principles that emphasize simplicity, scalability, and modifiability. Some key principles of RESTful architecture include:

* __Resources__: RESTful APIs are organized around resources, which are identified by unique URIs (Uniform Resource Identifiers). Each resource can be accessed using a small set of standardized operations (HTTP methods) such as GET, POST, PUT, and DELETE.

* __Stateless__: RESTful APIs are stateless, meaning that each request contains all the information necessary to process the request. There is no need for the server to store session information or other context between requests.

* __Cacheable__: Responses from RESTful APIs can be cached by clients to improve performance and reduce server load.

* __Uniform Interface__: RESTful APIs use a uniform interface that separates the concerns of client and server. This allows clients to be developed independently of the server, and vice versa.

### Getting Started

To get started with LatAmFX, follow these steps:

1. Clone the LatAmFX repository from Github:
    
```Bash
git clone https://github.com/floreskemec/LatAmFX.git
```

2. Install the necessary Python packages using pip:

```Bash
pip install -r requirements.txt
```

3. Create an API key for the [Open Exchange Rates](https://openexchangerates.org/) API and add it to your .env file (see below for details).

4. Run the API and web front-end using uvicorn:

```Bash
uvicorn app.main:app --reload
```

5. Access the web front-end by navigating to http://localhost:8000 in your web browser.

### Environment Variables

LatAmFX uses environment variables to store sensitive information like API keys. To set up your environment variables, create a new file called .env in the root directory of the project and add the following lines:

```
OPENEXCHANGERATES_API_KEY=your-api-key-here
```

Replace your-api-key-here with your actual Open Exchange Rates API key.

### Contributors

Gonzalo Flores Kemec. You can find me at:
floreskemec@gmail.com

### Acknowledgements

LatAmFX was built using the following tools and technologies:

    Python
    FastAPI
    Requests
    Jinja2
    Bootstrap
    Font Awesome
    Open Exchange Rates API