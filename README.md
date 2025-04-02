# Twitter-Clone
Twitter Clone in Python with Tkinter is a social media simulation with posts, likes, friends, notifications, and search. It uses lists for posts, priority queues for ranking, sets for friends/likes, queues for notifications, and hash maps for searching. The Boyer-Moore-Horspool algorithm ensures fast text searches. 


Twitter Clone - Python Project with Tkinter
This project is a simulation of a Twitter-like social media platform built in Python using the tkinter library for the graphical interface. It allows users to perform various actions such as posting messages, adding friends, viewing notifications, and searching.

Project Features
1. Main Screen
View Highlights: Displays the most relevant posts, sorted by the number of "likes."

View All Posts: Shows all posts made by users.

Add Post: Allows users to add a new post by entering their alias and message.

View Friends: Displays the user's added friends.

View Notifications: Shows activity notifications, such as when a user publishes something new.

Search: Enables searching for users and posts using keywords.

2. Add Post
Users can add posts to the social network.

The alias and post content are required. If the alias exists, the post is successfully added.

The post will appear at the top of the post list.

3. View Posts and Highlights
The system displays all available posts or only the most popular ones (those with the most "likes").

Each post includes an "Add Friend" button to add the post's author as a friend.

4. Friends
Users have a list of friends that can be added by clicking "Add Friend" on any post.

The current user's friends can be viewed by clicking "View Friends."

5. Notifications
Automatic activity notifications are generated, such as when a user posts something new.

Notifications can be viewed by clicking "View Notifications."

6. Search
Users can search for posts and users using keywords.

The system uses the Boyer-Moore-Horspool search algorithm to efficiently find matches in post texts and usernames.

7. Likes
Each post has a "Like" button.

Clicking "Like" increases the post’s like counter and updates the interface.

Users must enter their alias to register a like.

Data Structures Used
This project utilizes the following data structures:

Lists: Store all posts.

Priority Queues: Display the most popular posts based on "likes."

Sets: Manage each user's friend list.

Hash Maps: Optimize pattern searching within posts and usernames using Boyer-Moore-Horspool.

String Algorithms: Improve search efficiency with the Boyer-Moore-Horspool algorithm.
