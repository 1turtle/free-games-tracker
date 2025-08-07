# FreeGamesTracker
## Overview
This "pretty" website shows free games from select markets. New video games
are updated every Thursday at 17:00 UTC except during special events.

## Markets
- [Steam](https://store.steampowered.com/) and [SteamDB](https://steamdb.info/)
- [Epic Games](https://store.epicgames.com/en-US)
- [GOG Games](https://www.gog.com/en/)
- [PlayStation Plus (Subscription)](https://store.playstation.com/en-us/view/25d9b52a-7dcf-11ea-acb6-06293b18fe04/bc428b4a-f1b7-11ea-aadc-062143ad1e8d)
- [Amazon Prime Gaming (Subscription)](https://gaming.amazon.com/home)

## Description
View the website [here](https://freegamestracker.netlify.app/).

Or you can view ```data.json``` located in ```./src/resources/``` to see the
data manually. ```test_data.json``` and ```empty.json``` are only used for
developmental purposes.

## Tools
- React
- Selenium
- GitHub Actions CI/CD
- [CheapShark API](https://apidocs.cheapshark.com/#intro)

## Notes
CheapShark API provides information like deals on video games at free of
cost and no sign up required. You will notice that Epic Games links redirect to
the Steam market because the web scraper method, which can directly get Epic
links, can get detected at times, so instead I resorted to the api. Therefore,
some links may be broken due to the fact that they were manually reconstructed.
Also, since the information was retrieved from various sources, image quality
and layout will defer. For the best viewing purposes, I recommend device size
of at least 1020px.

## Contribution
- Established on August 2025 by 1turtle
