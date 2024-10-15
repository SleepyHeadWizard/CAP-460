'''
You are managing a movie collection. Each movie has a title, director and year of release. You need to:

Store all movies as a list of tuples.
Allow users to add new movies.
Display all List movies.
take year as input and Find and display relevent movie of all movies in the collection.
'''
movie_list=[('The Shawshank Redemption','Frank Darabont',1994),('The Godfather','Francis Ford Coppola',1972),('The Dark Knight','Christopher Nolan',2008),('The Lord of the Rings: The Return of the King','Peter Jackson',2003)]

choice=0
while choice!=4:
    print('1. Add new movie')
    print('2. Display all movies')
    print('3. Find movie by year')
    print('4. Exit')
    choice=int(input('Enter your choice:'))
    
    if choice==1:
        title=input('Enter movie title:')
        director=input('Enter movie director:')
        year=int(input('Enter movie year:'))
        movie_list.append((title,director,year))
    elif choice==2:
        for i in movie_list:
            print(i)
    elif choice==3:
        year=int(input('Enter year:'))
        for i in movie_list:
            if i[2]==year:
                print(i)
    elif choice==4:
        print('Exiting...')
    else:
        print('Invalid choice. Please try again.')