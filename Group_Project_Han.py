import pandas as pd
import numpy as np

def forecast():
    
    #Get training dataframe and the list of distinct number of days before departure
    training_file_name = 'airline_booking_trainingData.csv' #training_file_name = input('Enter file name:')
    df_train, distinct_diff_days = get_diff_between_bookingDate_and_departureDate(training_file_name)
    
    #Get the mean of the total number of sold tickets on each day before departure
    cum_bookings_hist_mean = booking_mean(df_train, distinct_diff_days)
    
    #Get the validation dataframe
    valid_file_name = 'airline_booking_validationData.csv' #valid_file_name = input(ter file name:')
    df_valid, diff_days_valid = get_diff_between_bookingDate_and_departureDate(valid_file_name)
    
    #Get the days before departure of each case in validation data
    validation_days_before_departure = df_valid.difference
    
    #Get the mean of the total number of sold tickets on the departure day
    final_ticket_index = distinct_diff_days.index(0)
    final_sold_ticket = cum_bookings_hist_mean[final_ticket_index]
    
    #Predict the result using pure additive method and pure multiplicative respectively
    result_additive = additive_model(distinct_diff_days, cum_bookings_hist_mean, validation_days_before_departure, final_sold_ticket)
    result_multiplicative = multiplicative_model(distinct_diff_days, cum_bookings_hist_mean, validation_days_before_departure, final_sold_ticket)
    
    #Use the results of both additive model and multiplicative model to predict the forecast
    forecast_result = combined_model(validation_days_before_departure, result_additive, result_multiplicative, df_valid)
    df_valid['my_forecast'] = forecast_result
       
    #Calculate MASE
    diff_between_true_naive_forecast = np.absolute(df_valid[df_valid.difference != 0]['naive_forecast'] - df_valid[df_valid.difference != 0]['final_demand'])
    diff_between_true_final_forecast = np.absolute(df_valid[df_valid.difference != 0]['my_forecast'] - df_valid[df_valid.difference != 0]['final_demand'])
    MASE = np.sum(diff_between_true_final_forecast) / np.sum(diff_between_true_naive_forecast)
    
    return MASE

    
    
    
def get_diff_between_bookingDate_and_departureDate(f):
    df = pd.read_csv(f)
    
    #Get the number of difference between departure date and the current date in each case
    difference = (pd.to_datetime(df.departure_date) - pd.to_datetime(df.booking_date)).dt.days
    df['difference'] = difference
    
    #Get the distinct number of difference between departure date and the current date
    distinct_diff_days = list(set(difference))
    
    return df, distinct_diff_days


def booking_mean(df, distinct_diff_days):
    cum_bookings_mean = []
    
    for days_before_departure in distinct_diff_days:
        diff_df = df[df['difference'] == days_before_departure]
        ticket_accum = diff_df['cum_bookings']
        cum_bookings_mean.append(np.mean(ticket_accum))
      
    return cum_bookings_mean   
    

def additive_model(X_train, y_train, target_date, final_ticket):
    result = []
    dic= {}
    
    for i in range(len(X_train)):
        dic[X_train[i]] = final_ticket - y_train[i]
    
    for td in target_date:
        result.append(dic[td])
    
    return result
        

def multiplicative_model(X_train, y_train, target_date, final_ticket):
    result = []
    dic = {}
    
    for i in range(len(X_train)):
        dic[X_train[i]] = y_train[i] / final_ticket
    
    for td in target_date:
        result.append(dic[td])
    
    return result


def combined_model(lyst, additive, multiplicative, df):
    final_result = []
    for i in range(len(lyst)):
        if lyst[i] == 0:
            final_result.append(np.nan)
        elif lyst[i] < 8: #Use additive model result when the difference between current date and departure date is less than 8 days
            final_result.append(additive[i] + df.cum_bookings[i])
        else: #Use multiplicative model result when the difference between current date and departure date is at least 8 days
            final_result.append(df.cum_bookings[i] / multiplicative[i])
    return final_result

print(forecast())