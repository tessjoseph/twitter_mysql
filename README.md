# MySQL Twitter Pipeline 🚀

This project is a Twitter-like application built using MySQL as the backend database. It provides basic functionalities such as posting tweets, following other users, and viewing the home timeline.

## 🌟 Features

- **Posting Tweets:** Users can post tweets, which are stored in the MySQL database with a unique tweet ID and timestamp.
- **Following Users:** Users can follow other users, which is implemented by storing user IDs in the database.
- **Viewing Home Timeline:** Users can view their home timeline, which includes tweets from users they follow. Tweets are retrieved from the database and sorted by timestamp.

## 🛠️ Technologies Used

- Python 🐍
- MySQL 🔍

## ▶️ How to Run

1. Clone the repository.
2. Install the required dependencies (`mysql-connector-python` library for Python).
3. Configure your MySQL database credentials in the `TwitterAPI` constructor.
4. Run the application using `python mysql_twitter.py`.
5. Access the application in your web browser at `http://localhost:5000`.

## 🚀 Future Improvements

- Implement user authentication and authorization.
- Add support for direct messaging between users.
- Improve error handling and data validation.

## 🙏 Acknowledgements

This project was inspired by the simplicity and efficiency of MySQL as a relational database for real-time applications like Twitter.
