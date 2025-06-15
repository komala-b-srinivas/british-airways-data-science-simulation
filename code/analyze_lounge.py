import pandas as pd

# Load data
df = pd.read_excel("British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx", engine='openpyxl')

# Create group
df['GROUP'] = df['HAUL'] + " " + df['TIME_OF_DAY'] + " - " + df['ARRIVAL_REGION']
df['TOTAL_PAX'] = df['FIRST_CLASS_SEATS'] + df['BUSINESS_CLASS_SEATS'] + df['ECONOMY_SEATS']

# Group and aggregate
grouped = df.groupby('GROUP').agg({
    'TIER1_ELIGIBLE_PAX': 'sum',
    'TIER2_ELIGIBLE_PAX': 'sum',
    'TIER3_ELIGIBLE_PAX': 'sum',
    'TOTAL_PAX': 'sum'
}).reset_index()

# Calculate percentages
grouped['Tier 1 %'] = (grouped['TIER1_ELIGIBLE_PAX'] / grouped['TOTAL_PAX'] * 100).round(1)
grouped['Tier 2 %'] = (grouped['TIER2_ELIGIBLE_PAX'] / grouped['TOTAL_PAX'] * 100).round(1)
grouped['Tier 3 %'] = (grouped['TIER3_ELIGIBLE_PAX'] / grouped['TOTAL_PAX'] * 100).round(1)

# Add example destinations
examples = {
    "LONG Morning - North America": "New York, Toronto",
    "LONG Afternoon - Asia": "Delhi, Singapore",
    "LONG Afternoon - Middle East": "Doha, Dubai",
    "LONG Afternoon - North America": "Chicago, Boston",
    "LONG Evening - Asia": "Bangkok, Tokyo",
    "LONG Evening - Middle East": "Abu Dhabi, Jeddah",
    "LONG Evening - North America": "Los Angeles, Vancouver",
    "LONG Morning - Asia": "Mumbai, Beijing",
    "LONG Morning - Middle East": "Muscat, Riyadh",
    "SHORT Morning - Europe": "Paris, Amsterdam",
    "SHORT Afternoon - Europe": "Berlin, Rome",
    "SHORT Evening - Europe": "Madrid, Prague",
    "SHORT Lunchtime - Europe": "Copenhagen, Zurich",
    "LONG Lunchtime - Asia": "Kuala Lumpur, Seoul",
    "LONG Lunchtime - Middle East": "Kuwait City, Tel Aviv",
    "LONG Lunchtime - North America": "Atlanta, Dallas"
}
grouped['Example Destinations'] = grouped['GROUP'].map(examples)

# Copy and create final DataFrame before adding Notes
final_df = grouped[['GROUP', 'Example Destinations', 'Tier 1 %', 'Tier 2 %', 'Tier 3 %']].copy()
final_df['Notes'] = ""

# Add custom notes
final_df.loc[final_df['GROUP'] == "LONG Afternoon - Asia", 'Notes'] = "High premium demand; potential Tier 1 opportunity"
final_df.loc[final_df['GROUP'] == "SHORT Evening - Europe", 'Notes'] = "Leisure-heavy traffic; low Tier 1 demand"

# Export final version
final_df.to_excel("lounge_lookup_table.xlsx", index=False)
print("✅ Final table saved with Example Destinations & Notes (no warnings!)")




