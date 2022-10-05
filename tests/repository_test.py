from repository import starwars_repo

def test_search_people_repository():
    page = 1
    search = ''
    people = starwars_repo.searchPeople(page, search)
    print(people)