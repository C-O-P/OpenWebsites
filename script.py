import webbrowser

website_lists = list()
user_choice = input(" 1. Open bookmarks\n 2. Add bookmark\n 3. Open Website\n")

def openBookmark():

    bookmarks_file = open("bookmarks.txt", "r")
    bookmarks_list = []

    ''' print bookmarks list  '''
    for names in bookmarks_file:
	bookmarks_list.append(names)

    count = 0
    bookmarks_dict = {}
    for names in bookmarks_list:
	count+=1
	bookmarks_dict[count] = names
	name = str(count) + '. ' + names
	print name

    user_choice = input("Enter your choice\n")

    ''' print bookmarks_dict '''

    webbrowser.open(bookmarks_dict[user_choice])
    bookmarks_file.close()


def addBookmark():
    bookmarks_file = open("bookmarks.txt", "a")
    name = raw_input("Enter website to add\n")
    bookmarks_file.write(name + '\n')
    bookmarks_file.close()


def openWebsite():
    website = raw_input("Enter full url\n")
   
    if( "www." in website == false ):
	website = "www." + website
    if (website[:4] != "http"):
	website = "http://" + website
    if ( ".com" in website == false):              
	website = website + ".com"

    ''' window_choice = raw_input(" Press 1 for new window else press 2\n")'''

    webbrowser.open(website)


'''    webbrowser.open(website)  ''' 


if __name__ == "__main__":

    if(user_choice == 1):
        openBookmark()
    elif(user_choice == 2):
        addBookmark()
    elif(user_choice == 3):
        openWebsite()

