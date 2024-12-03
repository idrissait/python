import re
from datetime import datetime

# Define a function to convert French date strings to proper datetime format
def convert_french_datetime(date_str):
    # Dictionary to translate French month names to English equivalents
    month_translation = {
        "janvier": "January", "février": "February", "mars": "March", "avril": "April", 
        "mai": "May", "juin": "June", "juillet": "July", "août": "August", 
        "septembre": "September", "octobre": "October", "novembre": "November", "décembre": "December"
    }

    # Extract day, month, year, and time
    pattern = r"(\d{1,2}) (\w+) (\d{4}) (\d{1,2})h(\d{2})"
    match = re.match(pattern, date_str)
    if match:
        day, month, year, hour, minute = match.groups()
        # Translate month from French to English
        month_english = month_translation[month.lower()]
        # Create a datetime object
        datetime_str = f"{day} {month_english} {year} {hour}:{minute}"
        return datetime.strptime(datetime_str, "%d %B %Y %H:%M")
    else:
        return None

# Apply the conversion function to the column
df['Datetime'] = df['Date de l’entrée'].apply(convert_french_datetime)

# Display the updated dataframe
import ace_tools as tools; tools.display_dataframe_to_user(name="Converted French DateTime Data", dataframe=df)
