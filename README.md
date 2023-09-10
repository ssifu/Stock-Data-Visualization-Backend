# Stock Market Data Management

## Overview

This project is a Django-based web application for managing and visualizing stock market data. It includes functionality to load data from JSON files into a MySQL database, provide API endpoints for fetching and paginating stock data, and visualize the data using interactive charts. Additionally, it allows users to edit and delete individual stock data entries.

## Project Features

### Data Loading

- Data can be loaded into the database from JSON files using a custom Django management command.
- The system checks for existing data and only adds new records, preventing duplicates.
- Data files are stored in a separate directory for easy management.

### API Endpoints

- API endpoints are provided for fetching stock data.
- Pagination is implemented to control the number of records returned.
- Filtering and sorting options can be added easily to these endpoints.

### Data Visualization

- The project uses the React Chart.js library to create interactive line and bar charts.
- Charts can be customized to display different aspects of the data.
- A dropdown menu allows users to select which trade codes to display in the charts.

### Editing and Deletion

- Users can edit stock data entries and submit changes to the backend.
- Entries can also be deleted individually.

## Project Setup

1. Clone the repository to your local machine.
2. Create a virtual environment and install the required Python packages using `pip install -r requirements.txt`.
3. Configure your Django settings, including the database connection settings, if necessary.
4. Migrate the database using `python manage.py migrate`.
5. Load initial data or update data from JSON files using the `load_data` management command: `python manage.py load_data path/to/your.json`.
6. Start the Django development server using `python manage.py runserver`.
7. Start the React development server for the frontend using `npm start` (ensure you have Node.js and npm installed).

## Technologies Used

- Django for the backend.
- React for the frontend.
- MySQL database for data storage.
- Chart.js for data visualization.
- Axios for making API requests.

## Lessons Learned

This project allowed me to learn and practice several key concepts and techniques:

- Data loading and management in Django using custom management commands.
- Building API endpoints for data retrieval and pagination.
- Integrating React and Django for a full-stack web application.
- Creating interactive charts and visualizations using Chart.js.
- Handling user authentication and data editing in a web application.

## Challenges Faced

Throughout the project, I encountered a few challenges:

1. **Database Schema Design**: Designing an efficient database schema to store and retrieve stock data while avoiding data duplication was a significant challenge.

2. **Frontend-Backend Integration**: Integrating the React frontend with the Django backend, especially for data editing and deletion, required careful coordination.

3. **Chart Customization**: Configuring and customizing Chart.js to display data according to user preferences and implementing the trade code dropdown menu for chart selection.

4. **Pagination and Filtering**: Implementing pagination and considering potential enhancements like filtering and sorting options for API endpoints.

Feel free to contribute to this project, report issues, or provide feedback to help make it even better!
