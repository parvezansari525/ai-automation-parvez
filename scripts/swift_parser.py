# import pandas as pd
# import json

# # Load CSV
# df = pd.read_csv(r'C:\Users\Parvej\Desktop\ai-automation-parvez\data\swift_messages.csv')

# # Clean messages
# df['message'] = df['message'].str.lower()

# # Classification logic
# def classify(msg):
#     if "payment" in msg:
#         return "Payment"
#     elif "transfer" in msg or "wire" in msg:
#         return "Transfer"
#     elif "salary" in msg:
#         return "Salary"
#     elif "refund" in msg:
#         return "Refund"
#     else:
#         return "Other"

# df['category'] = df['message'].apply(classify)

# # Convert to JSON
# output = df.to_dict(orient='records')

# # Save output
# with open(r'C:\Users\Parvej\Desktop\ai-automation-parvez\data\processed_swift.json', 'w') as f:
#     json.dump(output, f, indent=4)

# print("✅ SWIFT messages processed successfully!")

import pandas as pd
import json
import os

# Base directory
base_dir = os.path.dirname(os.path.dirname(__file__))

# File paths
input_path = os.path.join(base_dir, 'data', 'swift_messages.csv')
output_path = os.path.join(base_dir, 'data', 'processed_swift.json')

# Load data
df = pd.read_csv(input_path)

# Clean messages
df['message'] = df['message'].str.lower()

# Classification
def classify(msg):
    if "payment" in msg:
        return "Payment"
    elif "transfer" in msg or "wire" in msg:
        return "Transfer"
    elif "salary" in msg:
        return "Salary"
    elif "refund" in msg:
        return "Refund"
    else:
        return "Other"

df['category'] = df['message'].apply(classify)

# Save JSON
with open(output_path, 'w') as f:
    json.dump(df.to_dict(orient='records'), f, indent=4)

print("✅ File saved at:", output_path)