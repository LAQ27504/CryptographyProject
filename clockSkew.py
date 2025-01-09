import time
from TOTP.secretToDigits import generate_hash, truncate_dynamically, truncated_hash_to_token

def generate_totp_for_time(secret, timestamp):
    # Calculate the counter value based on the timestamp
    VALID_DURATION = 30
    counter_value = timestamp // VALID_DURATION

    hash = generate_hash(secret, counter_value)
    code = truncate_dynamically(hash)
    return truncated_hash_to_token(code)

base_timestamp = 1234567890  # 2009-02-13 23:31:30 UTC
client_time_offsets = [-90, -60, -30, 0, 30, 60, 90]  # in sec
secret = "3N6IXFJWA4HTEL7NXHIG3I2H5BTVVXQDHDZJWRJYW4PGTFWVYBDBQIZ4K5Z66GQU"

# Clock skew window (+-1 time step)
skew_window = 1
table = []

# Generate the TOTP tokens and compare with expected values
for offset in client_time_offsets:
    test_time = base_timestamp + offset  
    client_totp = generate_totp_for_time(secret, test_time)

    # Convert test_time to UTC
    utc_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(test_time))

    # Server generates TOTPs for the base timestamp +- skew window
    accepted = False
    for skew in range(-skew_window, skew_window + 1):
        server_time = base_timestamp + (skew * 30)  
        server_totp = generate_totp_for_time(secret, server_time)
        if client_totp == server_totp:
            accepted = True
            break

    table.append([offset, utc_time, client_totp, "YES" if accepted else "NO"])

print(f"+--------------------+-------------------+-------------------+----------+")
print(f"| Client Time Offset | UTC Time          | Client TOTP       | Accepted |")
print(f"+--------------------+-------------------+-------------------+----------+")
for row in table:
    print(f"| {row[0]:<18} | {row[1]:<17} | {row[2]:<17} | {row[3]:<8} |")
print(f"+--------------------+-------------------+-------------------+----------+")
