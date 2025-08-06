# FreeGamesTracker
## Overview
This website shows you free games from select markets.

## Markets
- Steam
- Epic Games
- GOG Games
- Playstation Plus
- Amazon Prime Gaming

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
CheapShark API is free and provides deals on video games. Epic Games free games
will redirect to Steam because the original web scraper is in CAPTCHA jail.
Some links to the market may be broken due to the fact that they were manually
reconstructed with the given information from CheapShark API. Also, since
information was retrieve from various sources, image quality and layout will
defer. There is a chance that the PlayStation and Prime Gaming scraper will be
blocked. Finally, I was unable to scrape the Prime games images due to the
fact that I would get a unable to find element error despite having the correct
XPATH and no iframe or shadow. For more details on how to fix Selenium errors
visit this article [here](https://dev.to/liviufromendtest/how-to-fix-the-element-not-found-error-in-selenium-28gj).

## Contribution
- Established on August 2025 by 1turtle
