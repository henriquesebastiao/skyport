# Skyport

[![Test](https://github.com/henriquesebastiao/skyport/actions/workflows/test.yml/badge.svg)](https://github.com/henriquesebastiao/skyport/actions/workflows/test.yml)
[![Coverage](https://coverage-badge.samuelcolvin.workers.dev/henriquesebastiao/skyport.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/henriquesebastiao/skyport)
![GitHub License](https://img.shields.io/github/license/henriquesebastiao/skyport)

An interface for consuming space agency APIs programmatically.

## Features ✨

Below are briefly listed the APIs that Skyport is able to obtain data from, and what information each of them provides.

### NASA

- [Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html) (APOD).
- NeoWs (Near Earth Object Web Service) is a service for information on near earth asteroids. With NeoWs a user can: search for Asteroids based on their closest approach date to Earth, lookup a specific Asteroid with its [NASA JPL small body id](https://ssd.jpl.nasa.gov/tools/sbdb_query.html), as well as browse the overall data-set.

> [!TIP]
> For more information about NASA APIs, visit: [https://api.nasa.gov](https://api.nasa.gov)

## Usage

You just need to instantiate a data source and interact with its available methods. In this example we instantiate a NASA data source with the API key `DEMO_KEY`.

> [!TIP]
> You can get your NASA API key at: [https://api.nasa.gov](https://api.nasa.gov)

Now we look for the Astronomy Picture of the Day for April 5, 2005 and print the title and URL of the resource.

```python
from skyport import Nasa

source = Nasa('DEMO_KEY')
apod = source.apod('2005-04-05')

print(apod.title)
print(apod.url)
```

The result:

```txt
Light From A Distant Planet
https://apod.nasa.gov/apod/image/0504/planeteclipse_spitzer.jpg
```