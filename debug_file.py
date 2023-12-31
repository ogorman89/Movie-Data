## this has one json dict for conveinent testing and debugging

import logging

logging.basicConfig(filename='error.log', filemode='w')

jsonSoup = {
  "@context": "https://schema.org",
  "@type": "Movie",
  "url": "https://www.imdb.com/title/tt0468569/",
  "name": "The Dark Knight",
  "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg",
  "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
  "review": {
    "@type": "Review",
    "itemReviewed": {
      "@type": "Movie",
      "url": "https://www.imdb.com/title/tt0468569/"
    },
    "author": { "@type": "Person", "name": "filmquestint" },
    "dateCreated": "2008-07-20",
    "inLanguage": "English",
    "name": "Heath Ledger&apos;s Dark and Brilliant Swan Song",
    "reviewBody": "I couldn&apos;t believe &quot;The Dark knight&quot; could live up to the hype. That&apos;s perhaps the biggest surprise. The secret, I believe, is a stunning, mature, intelligent script. That makes it the best superhero movie ever made. As if that wasn&apos;t enough, Heath Ledger. He, the newest of the tragic modern icons present us with a preview of something we&apos;ll never see. A fearless, extraordinary actor capable to fill up with humanity even the most grotesque of villains. His performance is a master class. Fortunately, Christian Bale&apos;s Batman is almost a supporting character. Bale is good but there is something around his mouth that stops him from being great. &quot;The Dark Knight&quot; is visually stunning, powerful and moving. What else could anyone want.",
    "reviewRating": {
      "@type": "Rating",
      "worstRating": 1,
      "bestRating": 10,
      "ratingValue": 10
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingCount": 2728903,
    "bestRating": 10,
    "worstRating": 1,
    "ratingValue": 9
  },
  "contentRating": "PG-13",
  "genre": ["Action", "Crime", "Drama"],
  "datePublished": "2008-07-18",
  "keywords": "dc comics,psychopath,moral dilemma,superhero,clown",
  "trailer": {
    "@type": "VideoObject",
    "name": "DVD Trailer",
    "embedUrl": "https://www.imdb.com/video/imdb/vi324468761",
    "thumbnail": {
      "@type": "ImageObject",
      "contentUrl": "https://m.media-amazon.com/images/M/MV5BNWJkYWJlOWMtY2ZhZi00YWM0LTliZDktYmRiMGYwNzczMTZhXkEyXkFqcGdeQXVyNzU1NzE3NTg@._V1_.jpg"
    },
    "thumbnailUrl": "https://m.media-amazon.com/images/M/MV5BNWJkYWJlOWMtY2ZhZi00YWM0LTliZDktYmRiMGYwNzczMTZhXkEyXkFqcGdeQXVyNzU1NzE3NTg@._V1_.jpg",
    "url": "https://www.imdb.com/video/vi324468761/",
    "description": "Trailer for Blu-ray/DVD release of most recent Batman installment",
    "duration": "PT33S",
    "uploadDate": "2008-11-05T06:59:18Z"
  },
  "actor": [
    {
      "@type": "Person",
      "url": "https://www.imdb.com/name/nm0000288/",
      "name": "Christian Bale"
    },
    {
      "@type": "Person",
      "url": "https://www.imdb.com/name/nm0005132/",
      "name": "Heath Ledger"
    },
    {
      "@type": "Person",
      "url": "https://www.imdb.com/name/nm0001173/",
      "name": "Aaron Eckhart"
    }
  ],
  "director": [
    {
      "@type": "Person",
      "url": "https://www.imdb.com/name/nm0634240/",
      "name": "Christopher Nolan"
    }
  ],
  "creator": [
    {
      "@type": "Organization",
      "url": "https://www.imdb.com/company/co0002663/"
    },
    {
      "@type": "Organization",
      "url": "https://www.imdb.com/company/co0159111/"
    },
    {
      "@type": "Organization",
      "url": "https://www.imdb.com/company/co0147954/"
    },
    {
      "@type": "Person",
      "url": "https://www.imdb.com/name/nm0634300/",
      "name": "Jonathan Nolan"
    },
    {
      "@type": "Person",
      "url": "https://www.imdb.com/name/nm0634240/",
      "name": "Christopher Nolan"
    },
    {
      "@type": "Person",
      "url": "https://www.imdb.com/name/nm0275286/",
      "name": "David S. Goyer"
    }
  ],
  "duration": "PT2H32M"
}

title = 'The Dark Knight'

def getElement(jsonObj,prop,subProp=''):
    '''
    Accepts json in dict format an property
      and optional sub-property, 
      returns the matched jsonObj[prop][?subProp]
    '''
    try:
      if subProp == '':
        return jsonObj[prop]
      else:
        return jsonObj[prop][subProp]
    except Exception as e:
        props = prop + ' ' + subProp
        msg = '%s for %s on %s' % (e, title, props)
        logging.exception(msg,exc_info=True)
        return 'Unknown'

aggregateRating = getElement(jsonSoup,"aggregateRating","ratingValue")
description = getElement(jsonSoup,"description")
numRatings = getElement(jsonSoup,"aggregateRating","ratingCount")
duration = getElement(jsonSoup,"duration")
contentRating = getElement(jsonSoup,"contentRating")
datePublished = getElement(jsonSoup,"datePublished")

print(aggregateRating)
print(description)
print(numRatings)
print(duration)
print(contentRating)
print(datePublished)
