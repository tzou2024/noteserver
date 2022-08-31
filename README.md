# NotesServer

### Backend for Google Docs Style Notes Client App:
https://github.com/tzou2024/noteclient

### Django Backed

## Routes:

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
   | GET    | `/folders/:folderId` | `folders # show with all notes in folder` |
   | POST   | `/folders` | `folder # add` |
   | PATCH  | `/folders/:folderId`  | `folders # update`|
   | DELETE | `/folders/:folderId`  | `folders # destroy`|

 - ### Notes
   | Verb   | URI Pattern | Controller#Action    |
   | ------ | ----------- | -------------------- |
   | GET    | `/notes` | `notes # index` |
   | GET    | `/notes/:noteId` | `notes # show` |
   | POST   | `/notes` | `note # add` |
   | PATCH  | `/notes/:noteId`  | `note # update`|
   | DELETE | `/notes/:noteId`  | `fnote # destroy`|
------
### ERD
![ERD](erd.png)

