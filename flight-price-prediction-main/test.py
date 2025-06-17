import pickle

model = pickle.load(open("c1_flight_rf.pkl", "rb"))

prediction=model.predict([[
            Total_Stops,
            journey_day,
            journey_month,
            dep_hour,
            dep_min,
            arrival_hour,
            arrival_min,
            Duration_hour,
            Duration_mins,
            Airline_AirIndia,
            Airline_GoAir,
            Airline_IndiGo,
            Airline_JetAirways,
            Airline_MultipleCarriers,
            Airline_Other,
            Airline_SpiceJet,
            Airline_Vistara,
            Source_Chennai,
            Source_Kolkata,
            Source_Mumbai,
            Destination_Cochin,
            Destination_Delhi,
            Destination_Hyderabad,
            Destination_Kolkata,
        ]])