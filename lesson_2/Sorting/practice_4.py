books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

print((sorted(books, key=lambda dict: int(dict['published']))) == # Pretty printed for clarity
[
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800'
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869'
    },
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967'
    }
])
