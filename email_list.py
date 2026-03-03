# A python example for sets. Manage email lists

# Initialize empty sets
subscribers = set()
unsubscribers = set()


# Function to add an email
def add_email(email, set_name):
    set_name.add(email)
    #    if set_name == subscribers:
    #        subscribers.add(email)
    #    else:
    #        unsubscribers.add(email)
    print(
        f"Email '{email}' added to {'subscribers' if set_name == subscribers else 'unsubscribers'}."
    )


# Function to remove an email
def remove_email(email, set_name):
    if email in set_name:
        set_name.remove(email)
        print(
            f"Email '{email}' removed from {'subscribers' if set_name == subscribers else 'unsubscribers'}."
        )
    else:
        print(
            f"Email '{email}' not found in {'subscribers' if set_name == subscribers else 'unsubscribers'}."
        )


# Function to display emails
def display_emails(set_name):
    if set_name == subscribers:
        for subscriber in subscribers:
            print(subscriber)
    else:
        for unsubscriber in unsubscribers:
            print(unsubscriber)


# Function to find active subscribers. Return the set.
def find_active_subscribers():
    for email in subscribers.difference(unsubscribers):
        print(email)


# Adding emails to subscribers (notice that some people subscribe more than once)
add_email("user1@example.com", subscribers)
add_email("user3@example.com", subscribers)
add_email("user4@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user6@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user8@example.com", subscribers)
add_email("user9@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user10@example.com", subscribers)
add_email("user12@example.com", subscribers)

# Adding emails to unsubscribers
add_email("user6@example.com", unsubscribers)
add_email("user8@example.com", unsubscribers)
add_email("user1@example.com", unsubscribers)
add_email("user10@example.com", unsubscribers)

# Displaying subscribers and unsubscribers
print("All Subscribers:")
display_emails(subscribers)

print("All Unsubscribers:")
display_emails(unsubscribers)

# Remove email from subscribers
remove_email("user2@example.com", subscribers)
display_emails(subscribers)

# Finding active subscribers
print("Active Subscribers:")
find_active_subscribers()
