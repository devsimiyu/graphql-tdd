posts = [
    {
        'id': 1,
        'title': 'post 1',
        'description': 'post desc 1'
    },
    {
        'id': 2,
        'title': 'post 2',
        'description': 'post desc 2'
    }
]

def listPosts_resolver(obj, info):
    return posts

def getPost_resolver(obj, info, id):
    return posts[int(id)]

def createPost_resolver(obj, info, title, description):
    return {
        'id': 3,
        'title': title,
        'description': description
    }
