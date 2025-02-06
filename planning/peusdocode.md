
PRINT main menu options
GET user input for main menu option

IF user input is 0:
    EXIT app

ELSE IF user input is 1:
    PRINT character menu options
    GET user input for character menu option

    IF user inputs 0:
        RETURN to main

    ELSE IF user input is 1:
        GET all characters in Honkai: Star Rail (CSV to start with, then from character table)
        PRINT products

    ELSE IF user input is 2:
        CREATE new character

        GET user input for character name
        GET user input for character path
        GET user input for character element
        WRITE/INSERT into file/table

ELSE IF user input is 2:
    PRINT banner menu

    IF user inputs 0:
        RETURN to main menu

    ELSE IF user input is 1:
        GET current banners
        PRINT banners

    ELSE IF user input is 2:
        UPDATE current banners
        
        GET user input for gatcha banner name
        GET user input for all character up rates
        CONVERT the input to a string, removing commas

        UPDATE table/file
    
    ELSE IF user input is 3:
        DELETE current banner

        GET user input for gatcha banner name
        IF it matches an entry:
            DELETE the row
        
        UPDATE CSV/database

ELSE IF user input is 3:
    PRINT record gatcha menu

    IF user input 0:
        RETURN to main

    ELSE IF user input 1:
        RECORD gatcha character pulls

        GET user input for gatcha banner they pulled on - usually limited is combined despite having mutliple banners
        GET user input for the amount of pulls they did
        GET user input for the result of the pull
        IF user pulled a 5 star:
            ASK if they won the 50/50
            IF they lost the 50/50:
                UPDATE banner pull to 0
                UPDATE next 5 star to the guaranteed character
            ELSE:
                UPDATE banner pull to 0

        ELSE:
            ASK if they pulled a 4 star
            IF yes:
                GET how many 4 stars they pulled - Doesn't matter if it's a lightcone or otherwise
            ELSE:
                CONTINUE
        LOAD/WRITE data to CSV/database

    ELSE IF user input 2:
        RECORD gatcha lightcones pulls

        GET user input for gatcha banner they pulled on - usually limited is combined despite having mutliple banners
        GET user input for the amount of pulls they did
        GET user input for the result of the pull
        IF user pulled a 5 star:
            ASK if they won the 50/50
            IF they lost the 50/50:
                UPDATE banner pull to 0
                UPDATE next 5 star to the guaranteed lightcone
            ELSE:
                UPDATE banner pull to 0

        ELSE:
            ASK if they pulled a 4 star
            IF yes:
                GET how many 4 stars they pulled - Doesn't matter if it's a lightcone or otherwise
            ELSE:
                CONTINUE
        
        LOAD/WRITE data to CSV/database