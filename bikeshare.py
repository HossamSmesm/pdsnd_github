import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nchoose the city from chicago, new york city, washington\n").lower()
        if city not in ("chicago", "new york city", "washington"):
            print("sorry!, your input is invalid, please try again.. ")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input(
            "\nchoose the month..  January, February, March, April, May, June or type 'all' if you do not have any preference?\n").lower()
        if month not in ("all", "january", "february", "march", "april", "may", "june"):
            print("sorry!, your input is invalid, please try again.. ")
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n choose the day:\n ").lower()
        if day not in ("saturday", "sunday", "monday", "tuesday", "wednisday", "thursday", "friday", "all"):
            print("sorry!, your input is invalid, please try again.. ")
            continue
        else:
            break

    print('-' * 40)
    return city, month, day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("the most common month  is :", popular_month)

    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print("the most common day of week is :", common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("the most popular hour is ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df['common_start_station'] = df['Start Station'].mode()[0]
    print("the most common start station is :", df['common_start_station'])

    # TO DO: display most commonly used end station
    df['common_end_station'] = df['End Station'].mode()[0]
    print("the most common end station is : ", df['common_end_station'])

    # TO DO: display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station'] + df['End Station']
    print ("the most frequent routes is :", df['routes'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['duration'] = df['End Time'] - df['Start Time']
    print("The total travel time is:", df['duration'].sum())

    # TO DO: display mean travel time
    print("The mean travel time is:", df['duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    user_gender = df['Gender'].value_counts()
    print(user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_Year = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_Year)
    except KeyError:
        print("\nEarliest Year:\nNo data available for this month.")

    try:
        Most_Recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
        print("\nMost Recent Year:\nNo data available for this month.")

    try:
        Most_Common_Year = df['Birth Year'].mode()[0]
        print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
        print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    """
    Display contents of the CSV file to the display as requested by
    the user.
    """

    start = 0
    end = 5

    display = input("Do you want to see the raws data ? ").lower()

    if display == 'yes':
        while end <= df.shape[0] - 1:

            print(df.iloc[start:end, :])
            start += 5
            end += 5

            end_display = input("Do you wish to see more data: ").lower()
            if end_display == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        display_data(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
