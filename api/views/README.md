# Notes, a Google Docs style note taking App

Designed with google docs style layouts, mobile friendly, and added usability features, like aumatically deleteing empty docs.

### <b> Create a note and type away! Documents auto save when clicking the back button. </b>


## Technologies Used 

### React.js

React.js is a JavaScript library that allows you to build fast and efficient web applications using the minimum amount of code possible. In React.js, you can break the web layout into components - reusable bits of code that return HTML elements. 

- 👉 [JavaScript concepts for React Beginners](https://blog.appseed.us/10-javascript-concepts-for-react-beginners/)

### Chakra UI Library 

Chakra UI is a library that allows you to build stunning and modern web applications using various layout components. It differs from other UI frameworks in that it offers accessibility and dark mode support by default. 

With Chakra UI, you spend less time building responsive and beautiful websites. If you want to create a web application that allows users to switch between different color modes with minimal lines of code, then Chakra UI is an excellent choice.

- 👉 [Chakra UI](https://chakra-ui.com/) - official website  

## Installation instructions
To use this app you will need to install all dependencies needed, and you can do that by running these commands in your command line:

```
$ npm install
```
```
$ npm start
```

This app is designed to work with the backend app, linked here:
https://github.com/tzou2024/noteserver
------------

### MVP User Stories

- As an unregistered user, I would like to sign up with email and password.
- As a registered user, I would like to sign in with email and password.

- As a signed in user, I would like to change password.
- As a signed in user, I would like to sign out.
- As a signed in user, I would like to send a chat message (socket)

- As a signed in user I would like to create a folder with a name a description
  
- As a signed in user I would like to create a note with Title and content
  
- As a signed in user I would like to update my notes

- As a signed in user I would like to update my folders


## Route Table
- ### User Authentication
   | Verb   | URI Pattern         | Controller#Action |
   | ------ | ------------------- | ----------------- |
   | POST   | `/sign-up`          | `users # signup`    |
   | POST   | `/sign-in`          | `users # signin`    |
   | PATCH  | `/change-password/` | `users # changepw`  |
   | DELETE | `/sign-out/`        | `users # signout `  |

 - ### Folders
   | Verb   | URI Pattern | Controller#Action    |
   | ------ | ----------- | -------------------- |
   | GET    | `/folders` | `folders # index` |
   | GET    | `/folders/:folderId` | `folders # show` |
   | GET    | `/myfolders`| `folders # personal show` |
   | POST   | `/folders` | `folder # add` |
   | PATCH  | `/folders/:folderId`  | `folders # update`|
   | DELETE | `/folders/:folderId`  | `folders # destroy`|

 - ### Notes
   | Verb   | URI Pattern | Controller#Action    |
   | ------ | ----------- | -------------------- |
   | GET    | `/foldes/:folderId/notes` | `notes # index` |
   | GET    | `/folders/:folderID/notes/:noteId` | `notes # show` |
   | POST   | `/folders/:folderID/notes` | `note # add` |
   | PATCH  | `/folders/:folderID/notes/:noteId`  | `fnote # update`|
   | DELETE | `/folders/:folderID/notes/:noteId`  | `fnote # destroy`|

## Schema

 - ### User
   - email: string
       - required
       - unique
   - hashedPassword: string
       - required
   - token: string
   - timestamps

 - ### folder
   - name: string
       - required
       - unique
   - description: string 
   - notes: {{ note Schema}}
   - token: string
   - timestamps

 - ### note
   - author: {User}
   - title: String
   - content: String
  