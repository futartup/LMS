###Routes required for the application

____
| Route Name  | url  | purpose | Method |
| :------------ |:---------------:| -----:| -----: |
| Auth      | /api/v1/get_token | authenticate and get the token | GET |
| Auth       | /api/v1/refresh_token | refresh the token | GET |
| User creation | /api/v1/user        |    create a new user | POST |
| User search catalog | /api/v1/search        |    user can search catalog | POST |
| User cancel registration | /api/v1/user/cancel-registration        |    create cancels registration | PUT |
| User renews a book registration | /api/v1/user/renew-book        |    user can renew a book registration | PUT |
| User deletion | /api/v1/user       |    deletes a user by library admin | DEL |
| User Books | /api/v1/user       |    Gets all the books borrowed by the user | GET |
| User Activities | /api/v1/user/activities       |    get all the activities of the user, basically history  | GET |
| Get the accessibilty of the users| /api/v1/user-accesibility       |    get the accessibilty which a user can have | GET |
| Library creation | /api/v1/library       |    creates a brand new library | POST |
| Subdivision of library | /api/v1/library/subdivision       |    creates a library under a parent library | POST |
| Library activities | /api/v1/library-activities       |    get all the books checkout from library | GET |
| Issue cards to user by librarian | /api/v1/issue-card        |    only library admin can use this api to issue cards | POST |
| Librarian can remove users | /api/v1/manage       |    only librarian can use this api to remove users | POST |
| system notify users | /api/v1/notify        |    system can use this api to notify users | POST |
| Pay fine | /api/v1/pay-fine        |    librarian/admin can use this api to notify users to pay late fine | POST |


**All the APIs which are mentioned in the table will have the GET, POST, DELETE, PUT methods**


###Authentication

We can use various authentication services. The various services which we can use are:

- JWT authentication.
- AWS cognito. If the user has logged in from many devices.

### Valid questions which should be asked to clients.

- How many users will use the system ?
- Will there be sub divisions of libraries ?
- What genre of books will be there in the library ?
- What age groups of users you are targeting ?
- What are the different types of staffs working ?
- How governing body will operate the library ?
- What will be the extra curricular activities done by library ?
- Will there be e-books ?
- Will the data stored in cloud or in local area ?
- When is the product expected to be delivered ?
- Do you want notification services for users ?
