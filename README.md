# Car Service Platform (Django Project)

This project is a Django-based platform that connects vehicle owners with mechanics and service providers. Vehicle owners can request services such as repairs, car washes, and oil changes, specifying details about their vehicle, their required service, and their budget. Mechanics or service providers can then review these requests, offer advice, and accept jobs if they choose to assist.

## Features

- **Service Request Creation**: Vehicle owners can create a detailed request for services like repairs, car washes, or oil changes. They provide information about their car, the problem or service they need, and their budget.
- **Mechanic Response**: Mechanics specializing in different areas (e.g., repairs, car washes) can review the service requests, offer advice, and choose to accept the job.
- **User Interaction**: Both customers and mechanics can communicate via the platform to discuss service details.
- **Admin Management**: Django’s admin panel is available for managing users, service requests, and responses.
- **User Accounts**: Separate user roles for customers and mechanics, allowing each to manage their services and interactions.

## Data

The system uses the following data fields to manage service requests and vehicle details:

- **Vehicle Information**:
  - Car make and model
  - Year of manufacture
  - Vehicle identification number (VIN)
  
- **Service Request Information**:
  - Service type (e.g., repair, car wash, oil change)
  - Detailed problem or request description
  - Preferred budget range
  - Service location or preferred workshop
  
- **Mechanic Information**:
  - Name
  - Expertise (e.g., engine repair, bodywork, electrical systems)
  - Availability
  
These data fields allow the system to match vehicle owners with the right service providers based on the service request.

## Tech Stack

- **Backend**: Django 4.x (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Bootstrap 5 for responsive design)
- **Database**: SQLite (default Django database)

## Setup Instructions
