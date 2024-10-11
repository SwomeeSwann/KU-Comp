#examples of user input:
#Max of temperature_max from day 0 to day 6
#Max of wind_speed_max from 2024-03-28 to 2024-04-01
#What is the precipitation_sum on day 5
#What is the weather_code on 2024-03-28


# inputs:
# usertext(string), available dates(list)

# outputs: Desciption(ex. max, min), 
# start of date(either 2024-03-41 or 2 as in day 2)
# end of date(same as start)

keywords = {'weather_code', 'temperature_max', 'temperature_min', 'precipitation_sum',
            'wind_speed_max', 'precipitation_probability_max'}

usertext = input("sdlfkjsdlkfj ")

def translate_user_input(usertext):
    description = None
    start_date = None
    end_date = None
    
    words = usertext.split()
    for pos in range(len(words)):
        word = words[pos]
        if word in keywords:
            description = word
        if word == 'from':
            remaining_words = words[pos+1:]
            s, e = translate_dates(remaining_words, start_date, end_date)
            return(description, s, e)
        elif word == 'on':
            remaining_words = words[pos+1:]
            day = translate_date(remaining_words)
            return(description, day)
    return(description, s, e)

#pass in list of words of dates, returns start_date, end_date
#ex. day 0 to day 6
#ex. 2024-03-28 to 2024-04-01
def translate_dates(datestring, start_date, end_date):
    for words in range(len(datestring)):
        word = datestring[words]
        if word == 'day' and start_date == None:
           start_date = datestring[words+1]
        elif word.isalpha() == False and start_date == None:
            start_date = word
        elif word == 'day':
            end_date = datestring[words+1]
        elif word.isalpha() == False:
              end_date = word
    return(start_date, end_date)


#same as above function, but returns a single date
def translate_date(datestring):
    if len(datestring) == 1:
        return datestring[0]
    return datestring[1]


print(translate_user_input(usertext))