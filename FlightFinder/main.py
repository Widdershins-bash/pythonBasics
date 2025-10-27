import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Set your origin airport
ORIGIN_CITY_IATA = "LON"

# ==================== Update the Airport Codes in Google Sheet ====================

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Search for Flights and Send Notifications ====================

# retrieve all emails from sheets
stopover = False
email_list = data_manager.get_customer_emails()
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        if cheapest_flight.price != "N/A":
            stopover = True

        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight is: £{cheapest_flight.price}")    

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")

        if stopover:
            message = f"subject: Low Price Alert!\n\nLow price alert!\nOnly ${cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} with a stopover,\non {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else: 
            message = f"subject: Low Price Alert!\n\nLow price alert!\nOnly ${cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport},\non {cheapest_flight.out_date} until {cheapest_flight.return_date}."

        notification_manager.send_message(message=message, to_emails=email_list)
        


