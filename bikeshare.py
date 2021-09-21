import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#############################################################################################

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        # input for filtering by city number 
    cities = {
        '1' : 'chicago',
        '2' : 'new york city',
        '3' :'washington' ,
        }
    i = 1
    while (i >= 1): 
        cityNo = input('Welcome to BIKESHARE  ! \nwould you like to filter by the city name ? \n Enter the number of city you interested in : \n 1-chicago \n 2-new york city \n 3-washington \n\n')
        if cityNo in cities.keys():
            city = cities[cityNo]
            break
        else: 
            print('Please ! Enter a valid city number : ')
            i += 1

    # TO DO: get user input for month (all, january, february, ... , june)
    # input for filtering by month 
    months = { '1' : 'january' , 
                '2' : 'february',
                '3' : 'march' ,
                '4' :  'april', 
                '5' :  'may' ,
                '6' : 'june',
                '7' : 'all'
                }
    i = 1
    while (i >= 1): 
        m = input('would you like to filter by the month ? \n Enter the number of month you interested in or "all" to apply no filter: \n1 - january \n2- february \n3 - march \n4 - april \n5 - may \n6 - june \n7 - all \n\n')
        if m in months.keys():
            month = months[m]
            if(m != 'all'):
                m = int(m)
                break
        else: 
            print('Please ! Enter a valid month number or 7- all  for applying no filter : \n')
            i += 1
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
# input for filtering by day 
    i = 1
    while (i >= 1): 
        day = input('would you like to filter by the day ? \n Enter the day name or "all" to apply no filter: (Ex : sunday ..) \n\n')
        if day.title() in ['Sunday', 'Monday' , 'Tuesday' , 'Wednesday','Thursday','Friday','Saturday']:
            break
        elif(day == 'all'):
            break
        else : 
            print('Please ! Enter a valid day name or all to apply no filter: \n')
            i += 1

    return city,month,m,day

#############################################################################################

def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print('DATA FOR {}  \n'.format(city.upper()))
    df = pd.read_csv(CITY_DATA [city],index_col=[0])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['months'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df["months"]== month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    c = 0
    i = 1
    while (i >= 1): 
        answer = input('would you like to view first 5 rows :  \n Answer with \n 1- yes \n 2- no \n')
        if answer == '1':
            print(df[c:c+5])
            c += 5
        elif answer == '2' :
            break
        else : 
            print('\nPlease ! Enter a valid number')
            i += 1
            
    return df


def time_stats(df):
    #after filteration based on month , day or both displaying stats based on it
    """Displays statistics on the most frequent times of travel."""

    print('\n Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month  if months display else from the main df
    print('the Most common MONTH is : ' , df['months'].mode()[0] )

    # TO DO: display the most common day of week
    print('the Most common DAY is : ' , df['day_of_week'].mode()[0] )

    # TO DO: display the most common start hour
    df['hours'] = df['Start Time'].dt.hour
    print('the Most common STARTING HOUR is : ' , df['hours'].mode()[0] )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    print('The Most Common Start Station : {}'.format(df['Start Station'].mode()[0]))
    
    # TO DO: display most commonly used end station
    print('The Most Common End Station : {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    #concatinating the two columns to get the most frequent start and station
    common_start_end = (df['Start Station']+ ' -- ' + df['End Station']).mode()[0]
    print('The Most Common Comination of Start and End Station : {}'.format(common_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The Total TRAVEL TIME in Seconds  : {} sec'.format(df['Trip Duration'].sum()))
    print('The Total Travel Time in Hours  : {} h'.format((df['Trip Duration'].sum())/3600))

    # TO DO: display mean travel time
    print('The MEAN TRAVEL TIME in Seconds  : {} sec'.format(df['Trip Duration'].mean()))
    print('The MEAN Travel Time in Hours  : {} h'.format((df['Trip Duration'].mean())/3600))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The COUNTS USER TYPE :\n{} '.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if( city == 'chicago' or city == 'new york city' ):
        print('The COUNTS OF GENDER : \n{} '.format(df['Gender'].value_counts()))
        
        # TO DO: Display earliest, most recent, and most common year of birth
        print('The MOST EARLIEST YEAR : {} '.format(int(df['Birth Year'].min())) )
        print('The MOST RECENT  YEAR : {} '.format(int(df['Birth Year'].max())))
        print('The COMMON YEAR : {} '.format(int(df['Birth Year'].mode()[0])))
    else :
        print ('Washington has no GENDER or BIRTH YEAR DATA !')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        #getting input data from user city month and day
        city,month,m,day = get_filters()
        print ('It seems you are interested about :  \n city : {}\n Month : {}\n Month No : {} \n Day is {}\n'.format(city , month,m ,day))
        
        #loading data from csv files 
        #check  for month
        if (month == 'all'):
            df = load_data(city,month, day)
        else:
             df = load_data(city,m, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        #I provided city for user_stats because washington has no data for gender and birth year
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break
if __name__ == "__main__":
	main()
