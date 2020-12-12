import json


def get_chrome_bookmarks(username):

    def add_bookmarks(list):
        for item in list:
            try:
                data.append(
                    {
                        'Name': item['name'],
                        'URL': item['url']
                    }
                )
            except KeyError:
                add_bookmarks(item['children'])

    with open('/Users/{}/Library/Application Support/Google/Chrome/Default/'
              'Bookmarks'.format(username), 'r') as f:

        bookmark_bar = json.loads(f.read())['roots']['bookmark_bar']['children']
        data = []
        add_bookmarks(bookmark_bar)

        return data


if __name__ == '__main__':

    for bookmark in get_chrome_bookmarks('ali'):

        print('{name} \n\t {url} \n'.format(
            name=bookmark['Name'], url=bookmark['URL']
        ))
