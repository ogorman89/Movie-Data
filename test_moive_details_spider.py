import pytest
import movie_details_spider as mds


@pytest.fixture
def mock_people():
    people = []
    return people


@pytest.fixture
def mock_titleId():
    titleId = "tt0499549"
    return titleId


@pytest.fixture
def mock_json():
    json = {
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
                "url": "https://www.imdb.com/title/tt0468569/",
            },
            "author": {"@type": "Person", "name": "filmquestint"},
            "dateCreated": "2008-07-20",
            "inLanguage": "English",
            "name": "Heath Ledger&apos;s Dark and Brilliant Swan Song",
            "reviewBody": "I couldn&apos;t believe &quot;The Dark knight&quot; could live up to the hype. That&apos;s perhaps the biggest surprise. The secret, I believe, is a stunning, mature, intelligent script. That makes it the best superhero movie ever made. As if that wasn&apos;t enough, Heath Ledger. He, the newest of the tragic modern icons present us with a preview of something we&apos;ll never see. A fearless, extraordinary actor capable to fill up with humanity even the most grotesque of villains. His performance is a master class. Fortunately, Christian Bale&apos;s Batman is almost a supporting character. Bale is good but there is something around his mouth that stops him from being great. &quot;The Dark Knight&quot; is visually stunning, powerful and moving. What else could anyone want.",
            "reviewRating": {
                "@type": "Rating",
                "worstRating": 1,
                "bestRating": 10,
                "ratingValue": 10,
            },
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingCount": 2728903,
            "bestRating": 10,
            "worstRating": 1,
            "ratingValue": 9,
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
                "contentUrl": "https://m.media-amazon.com/images/M/MV5BNWJkYWJlOWMtY2ZhZi00YWM0LTliZDktYmRiMGYwNzczMTZhXkEyXkFqcGdeQXVyNzU1NzE3NTg@._V1_.jpg",
            },
            "thumbnailUrl": "https://m.media-amazon.com/images/M/MV5BNWJkYWJlOWMtY2ZhZi00YWM0LTliZDktYmRiMGYwNzczMTZhXkEyXkFqcGdeQXVyNzU1NzE3NTg@._V1_.jpg",
            "url": "https://www.imdb.com/video/vi324468761/",
            "description": "Trailer for Blu-ray/DVD release of most recent Batman installment",
            "duration": "PT33S",
            "uploadDate": "2008-11-05T06:59:18Z",
        },
        "actor": [
            {
                "@type": "Person",
                "url": "https://www.imdb.com/name/nm0000288/",
                "name": "Christian Bale",
            },
            {
                "@type": "Person",
                "url": "https://www.imdb.com/name/nm0005132/",
                "name": "Heath Ledger",
            },
            {
                "@type": "Person",
                "url": "https://www.imdb.com/name/nm0001173/",
                "name": "Aaron Eckhart",
            },
        ],
        "director": [
            {
                "@type": "Person",
                "url": "https://www.imdb.com/name/nm0634240/",
                "name": "Christopher Nolan",
            }
        ],
        "creator": [
            {"@type": "Organization", "url": "https://www.imdb.com/company/co0002663/"},
            {"@type": "Organization", "url": "https://www.imdb.com/company/co0159111/"},
            {"@type": "Organization", "url": "https://www.imdb.com/company/co0147954/"},
            {
                "@type": "Person",
                "url": "https://www.imdb.com/name/nm0634300/",
                "name": "Jonathan Nolan",
            },
            {
                "@type": "Person",
                "url": "https://www.imdb.com/name/nm0634240/",
                "name": "Christopher Nolan",
            },
            {
                "@type": "Person",
                "url": "https://www.imdb.com/name/nm0275286/",
                "name": "David S. Goyer",
            },
        ],
        "duration": "PT2H32M",
    }
    return json


def test_parseId():
    # test a person
    assert mds.parseId("https://www.imdb.com/name/nm0000288/") == "nm0000288"
    # test a title
    assert (
        mds.parseId(
            "https://www.imdb.com/title/tt0111161/?bunch_of_extra_garbage1555666"
        )
        == "tt0111161"
    )
    # test a different length title
    assert mds.parseId("https://www.imdb.com/title/tt11448076/") == "tt11448076"


def test_createList():
    # test a simple list
    assert mds.createList([{"name": "bob"}, {"name": "pam"}], "name") == ["bob", "pam"]
    # test a more complicated list and a different key
    assert mds.createList(
        [
            {
                "@type": "Person",
                "url": "https://www.imdb.com/name/nm0941777/",
                "name": "Sam Worthington",
            },
            {
                "@type": "Person",
                "url": "https://www.imdb.com/name/nm0757855/",
                "name": "Zoe Saldana",
            },
            {
                "@type": "Person",
                "url": "https://www.imdb.com/name/nm0000244/",
                "name": "Sigourney Weaver",
            },
        ],
        "url",
    ) == [
        "https://www.imdb.com/name/nm0941777/",
        "https://www.imdb.com/name/nm0757855/",
        "https://www.imdb.com/name/nm0000244/",
    ]


def test_addPerson(mock_people, mock_titleId):
    # FIXME this test is broken it yields people is undefined
    people = mock_people
    titleId = mock_titleId
    mds.addPerson("Sigourney Weaver", "https://www.imdb.com/name/nm0000244/", "actor")
    assert people == [["nm0000244", "Sigourney Weaver", "actor", "tt0499549"]]


# def test_writeCsv():
#     assert mds.writeCsv() == []


def test_getElement(mock_json):
    assert mds.getElement(mock_json, "aggregateRating", "ratingCount") == 2728903
    assert mds.getElement(mock_json, "name") == "The Dark Knight"
