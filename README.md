# TicketNest

## Executive Summary
**TicketNest** is a comprehensive ticketing system simulating TicketMaster, designed for users, event organizers, and administrators to manage and interact with events, ticketing operations, and each other. **Users** can search for events, purchase tickets, and manage their orders. **Event organizers** can create and manage events, configure various ticket types, and oversee ticket availability. **Administrators** analyze user activities and sales performance to optimize the platform’s operations. To facilitate these processes, the system includes essential entities such as **User**, **Event**, **Ticket**, and **Order**. This project allows for efficient event management, smooth ticket sales, and personalized user experiences.

## User Guide

### 1. Login

#### User Login Credentials
- **Email**: user@gmail.com
- **Password**: UserTest@123

After logging in, Users are redirected to the **Order History** page, where they can view past orders.

#### Order History
- Each order displays essential details, including **Order ID**, **Purchase Date**, **Order Status**, and **Payment Method**.
- To view more details about an order, click the **Order Details** button at the bottom right of the order entry. This opens a detailed view showing:
  - Event information: date, venue, artist names
  - Ticket type and price
  - Total payment amount
- To return to the **Order History** page, click **Go Back** in the bottom right corner.

### 2. Search for Events
Navigate to the **Search** option in the navigation bar to enter the **Events** page. Here, you can find events based on specific criteria:

- **Text Search**: Enter keywords related to the event name, artist name, or venue name in the search bar.
- **Category Filter**: Select an event category from **Concert**, **Festival**, **Sports Event**, or **Theatre**.
- **Status Filter**: Choose an event status from **Active**, **Past**, or **Canceled**.
- **Date Filter**: Choose a date range.

Events matching the criteria will be displayed with details such as **Event Date**, **Artist Name**, **Event Name**, **Venue**, **Category**, and **Event Status**.

#### View Event Details
- Next to each event, click **Find Details** to view the **Event Details** page. This page includes a description of the event, available ticket types, and prices.
- Click **Entity Details** on the **Event Details** page to view specific information about the artists or teams. This includes a bio for artists, achievements and stats for teams, and a Wikipedia link for both artists and teams.

### 3. Search for Entities
Navigate to the **Search** option in the navigation bar to enter the **Entity** page. Here, you can find artists and sports teams based on specific criteria:

- **Text Search**: Enter keywords related to the artist or team name in the search bar.
- **Category Filter**: Select an entity category from **Artist** or **Team**.
- **Genre Filter**: For artists only. Choose a music genre from **Alternative Rock**, **Classical**, **Country**, **Electronic**, **Indie Folk**, **Jazz**, **Opera**, **Pop**, or **Rock**.
- **Sport Filter**: For teams only. Choose a sport type from **Baseball**, **Basketball**, **Cricket**, **Football**, **Hockey**, **Rugby**, **Soccer**, **Swimming**, **Tennis**, or **Volleyball**.

### 4. Buy Tickets
On the **Event Details** page, Users can purchase tickets by following these steps:

- Click **Buy Tickets** at the bottom right.
- Choose the desired **ticket type**, **quantity**, and **payment method**.
- The page will automatically calculate and display the total payment amount.
- Click **Place Order** to complete the purchase.

## Event Organizer Guide

### Login

#### Event Organizer Login Credentials
- **Email**: organizer@gmail.com
- **Password**: Organizer@1

Once logged in, Event Organizers are redirected to their **Dashboard**, which has three primary options:

1. **Manage Events**
2. **Manage Tickets**
3. **Manage Orders**

> **Note**: Event Organizers do not have access to **Order History** or **Buy Tickets** functionality.
### Event Organizer Dashboard
Once logged in, Event Organizers are redirected to their **Dashboard**, which has three primary options:

1. **Manage Events**
2. **Manage Tickets**
3. **Manage Orders**

> **Note**: Event Organizers do not have access to **Order History** or **Buy Tickets** functionality.

## Administrator Guide

### Login

#### Administrator Login Credentials
- **Email**: administrator@gmail.com
- **Password**: Administrator@1

### Administrator Dashboard
Once logged in, Administrators are redirected to their **Homepage**, where they can access the event performance report page:

- **Generate Event Performance Report**: Generate and save a summary report of event performance for a specified date range, including details like total tickets sold, revenue generated, and average rating per event. Export the report as a CSV file based on the date range and selected events.


